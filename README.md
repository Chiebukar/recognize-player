# recognize-player
![Capture](https://user-images.githubusercontent.com/54807024/123533783-8f7cbb00-d6ab-11eb-98aa-c3c8f07657d8.JPG)
An end to end machine learning project to facially recognize the following players: <br>
Cristiano Ronaldo, Lionel Messi, Son Heung Min, Sadio Mane, Neymar Jr and Mohammed Salah.

Images of the players were webscraped and  and processed by detecting and cropping out the faces using OpenCV<br>
The data was cleaned by manually removing images with limited visible facial features.
The facial features were transformed for training using Pywavelet.
The processed image data was then trained  by hyperparameter tuning it with gridsearchCV to select best model and parameters for training the data.
The data was used to  train a Support Vector Machine (SVM) model and achieved a 77% score on the test set.

The saved model and class attributes were then used to build a web app using streamlit and deployed on Heroku (https://recognize-player.herokuapp.com/)








