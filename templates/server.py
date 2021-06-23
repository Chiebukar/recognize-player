from flask import Flask, jsonify, request, render_template
import util

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('app.html')


@app.route('/classify_images', methods=['GET', 'POST'])
def classify_images():

    base64_img = request.form['image_data']
    print('step 1')
    response = jsonify({
        'predicted_player': util.classify_images(base64_img)
    })
    print('step 2')
    response.headers.add('Access-Allow-Control-Origin', '*')

    return response


if __name__ == '__main__':
    print('Starting Python Server')
    util.load_saved_artifacts()
    app.run(port=5000)
