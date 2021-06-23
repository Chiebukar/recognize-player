function getImage() {
  var image_data = document.getElementById("image").value;
  return image_data
}



function onClickPredictPlayer() {
  console.log("Predict Player button clicked");
  var image_data = getImage();
  {console.log(image_data)}
  var predictPlayer = document.getElementById("result");
 
  console.log('gotten image')

  var entry = {
      image_data: image_data,
      
  }

  fetch('/classify_images', {
        method: 'POST',
        body : JSON.stringify(entry),
        headers: {
          "content-type": "application/json"
        }
      }).then(function(response){
        if (response.status !==200){
          console.log('There was a problem. Status code : ',response.status);
        }
        return response.json();
      }).then(function(data){
        console.log('POST response: ', data);
        value = data.predicted_player
        
        predictPlayer.innerHTML = value.class +'/n' + value.probability;
      console.log(status);
      })
    }