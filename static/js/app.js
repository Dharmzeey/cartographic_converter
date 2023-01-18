// THIS SCRIPT IS FOR ( FORM) IT IS USED TO FETCH AND POULATE THE LONGITUDE INPUT
// WHEN USER WANTS TO UPLOAD

if (document.getElementById("lon")) {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    x.value = "Geolocation is not supported by this browser.";
  }

  function showPosition(position) {
    lon.value = position.coords.longitude;
  }
}