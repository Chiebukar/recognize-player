# recognize-player
![Capture](https://user-images.githubusercontent.com/54807024/123533783-8f7cbb00-d6ab-11eb-98aa-c3c8f07657d8.JPG)
![Capture2](https://user-images.githubusercontent.com/54807024/123533840-1af64c00-d6ac-11eb-8cdb-37b776cf1f9d.JPG)<br>
The recognize-player project is an end to end machine learning test project to facially recognize the following players: <br>
Cristiano Ronaldo, Lionel Messi, Son Heung Min, Sadio Mane, Neymar Jr and Mohammed Salah.

Images of the players were webscraped and  and processed by detecting and cropping out the faces using OpenCV<br>
The data was cleaned by manually removing images with limited visible facial features.
The facial features were transformed for training using Pywavelet.
The processed image data was then trained  by hyperparameter tuning it with gridsearchCV to select best model and parameters for training the data.
The data was used to  train a Support Vector Machine (SVM) model and achieved a 77% score on the test set.

The saved model and class attributes were then optimize to build a web app that recognizes the players in real time using streamlit and deployed on Heroku (https://recognize-player.herokuapp.com/)

The app achieves high probabilty in recognizing the aforementioned players in real time.<br>

![Capture5](https://user-images.githubusercontent.com/54807024/123534065-9d334000-d6ad-11eb-996d-c066b49bc36c.JPG)
![Capture4](https://user-images.githubusercontent.com/54807024/123534016-331a9b00-d6ad-11eb-811c-bc35dbade54b.JPG)





