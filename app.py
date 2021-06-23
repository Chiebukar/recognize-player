import streamlit as st
import base64
import util


st.spinner('Loading saved artifacts')
util.load_saved_artifacts()

ronaldo_jpg = "Cristiano Ronaldo.jpg"
messi_jpg = "Lionel Messi.jpg"
salah_jpg = "Mohammed Salah.jpg"
neymar_jpg = "Neymar Jr.jpg"
son_jpg = "Son Heung Min.jpg"
mane_jpg = "Sadio Mane.jpg"
ext = "jpg"


st.title('Football Player Recognizer')

image_html = f"""
<head>
<style>
* {{
   box-sizing: border-box;
}}
img {{
    border-radius: 20%;
    width: 100%;
    height: 80%;
}}
.column {{
   border-radius: 50%;
   float: left;
   width: 33.33%;
   padding: 1.5px;
}}


</style>
</head>
<div class="row">
	<div class="column">
		<img src= 'data:image/jpg;base64,{base64.b64encode(open(messi_jpg,"rb").read()).decode()}' alt="messi" style="width:100%">	
	</div>
	<div class="column">
		<img src= 'data:image/jpg;base64,{base64.b64encode(open(ronaldo_jpg,"rb").read()).decode()}' alt="ronaldo" style="width:100%">	
	</div>
	<div class="column">
		<img src= 'data:image/jpg;base64,{base64.b64encode(open(salah_jpg,"rb").read()).decode()}' alt="salah" style="width:100%">	
	</div>
	<div class="column">
		<img src= 'data:image/jpg;base64,{base64.b64encode(open(neymar_jpg,"rb").read()).decode()}' alt="junior" style="width:100%">	
	</div>
	<div class="column">
		<img src= 'data:image/jpg;base64,{base64.b64encode(open(son_jpg,"rb").read()).decode()}' alt="son" style="width:100%">	
	</div>
	<div class="column">
		<img src= 'data:image/jpg;base64,{base64.b64encode(open(mane_jpg,"rb").read()).decode()}' alt="mane" style="width:100%">	
	</div>

</div>                          
"""

st.header('''This web app facially recognizes the following footballers:
        Lionel Messi, Cristiano Ronaldo, Mohammed Salah,
        Neymar Junior, Son Heung Min and Sadio Mane.
          
  You can use this app to recognize these players by uploading any image of the player
  .''')

st.markdown('<hr>', unsafe_allow_html=True)
st.markdown(image_html, unsafe_allow_html=True)
# st.image(images, names, width=115, channels='BGR')

file = st.file_uploader('Upload image here')
if file:
    st.image(file)

if st.button('Classify'):
    result = util.classify_images(base64_img=None, image=file)
    players = ['Cristiano Ronaldo', 'Heung Min_Son', 'Lionel Messi', 'Mohammed Salah', 'Neymar_jr', 'sadio_mane']

    # st.text_area('Player', result[0]['prediction'])
    st.text_area('Player', players[result[0]['player']])
    st.text_area('Probability', str(result[0].get('probability')) + '%')




# def get_players():
#     names = []
#     images = []
#     for player in os.listdir(path):
#         name = player.split('.')[0]
#         names.append(name)
#         image_path = path + player
#         image = cv2.imread(image_path)
#         image = imutils.resize(image, height=400)
#         centerY, centerX = image.shape[0]//2, image.shape[1]//2
#         radius = round((centerY**2 + centerX**2)**0.5)
#         image = cv2.circle(image, (centerX, centerY), radius, (0, 0, 0), 100)
#         images.append(image)
#     return names, images


