import joblib
import json
import cv2
from base64 import b64decode
import numpy as np
from PIL import Image
from wavelet import wavelet_transform

__model = None
__class_dict = {}
__class_to_player = {}


def classify_images(base64_img, image=None, file_path=None):

    try:
        imgs = get_cropped_image_if_2_eyes(base64_img, image, file_path)
        result = []

        for img in imgs:
            scaled_img = cv2.resize(img, (32, 32))
            wave_trans_img = wavelet_transform(img, 'db1', 5)
            scaled_wave_trans_img = cv2.resize(wave_trans_img, (32, 32))
            combined_img = np.vstack((scaled_img.reshape(32 * 32 * 3, 1), scaled_wave_trans_img.reshape(32 * 32, 1)))
            len_img_arr = 32*32*3 + 32*32
            final = combined_img.reshape(1, len_img_arr).astype(float)
            prediction = (__model.predict(final))[0]
            probability = (np.round(__model.predict_proba(final)*100, 2)).tolist()[0]
            print('probability is : ', probability)
            if probability[prediction] >= 55:
                result.append({

                    #'class': __class_to_player[prediction],
                    'player': prediction,
                    'probability': probability[prediction],
                    #'class_dict': __class_dict

                })
        print(result)
        return result

    except Exception as e:
        print(e)
        return None


def get_cropped_image_if_2_eyes(base64_img, image, file_path):
    if file_path:
        img = cv2.imread(file_path)
    elif image:

            pil_img = Image.open(image).convert('RGB')
            img = np.array(pil_img)
            img = img[:, :, ::-1].copy()
    else:
        img = get_img_from_base64_img(base64_img)

    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier('./opencv/haarcascades/haarcascade_frontalface_default.xml')
    eyes_cascade = cv2.CascadeClassifier('./opencv/haarcascades/haarcascade_eye.xml')
    cropped_faces = []

    face = face_cascade.detectMultiScale(grey_img, 1.3, 5)

    for (x, y, w, h) in face:
        roi_img = img[y:y+h, x:x+w]
        roi_gray = grey_img[y:y+h, x:x+w]

        eyes = eyes_cascade.detectMultiScale(roi_gray)
        if len(eyes) >= 2:
            cropped_faces.append(roi_img)

        return cropped_faces


def get_img_from_base64_img(base64_img):
    data = base64_img.split(',')[1]
    nparr = np.frombuffer(b64decode(data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img


def load_saved_artifacts():
    print('Loading saved artifacts.....start')
    global __model
    global __class_dict
    global __class_to_player

    with open('./fav_footy_face_model.pkl', 'rb') as f:
        __model = joblib.load(f)

    with open('./class_dict.json', 'r') as f:
        __class_dict = json.load(f)

    __class_to_player = {number: player for player, number in __class_dict.items()}

    print('loading saved artifacts....done')


def read_b64_image(path_to_b64):
    with open(path_to_b64) as f:
        return f.read()


if __name__ == '__main__':
    load_saved_artifacts()
    print(classify_images(None, None,'./test_images/Cristiano Ronaldo.jpg'))
    # print(classify_images(None, './test_images/samuel.jpg'))
    # print(classify_images(read_b64_image('./test_images/b64.txt')))
