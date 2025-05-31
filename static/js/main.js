document.addEventListener("DOMContentLoaded", function () {
	const form = document.querySelector("form");
	if (form) {
		form.addEventListener("submit", function (e) {
			const inputs = form.querySelectorAll("input[type='number']");
			let valid = true;

			inputs.forEach(input => {
				if (!input.value.trim()) {
					alert("All fields are required.");
					e.preventDefault();
					valid = false;
					return false;
				}
			});

			return valid;
		});
	}
});

// static/js/main.js
document.addEventListener("DOMContentLoaded", function () {
	const toggleBtn = document.getElementById("toggle-info");
	const infoContent = document.getElementById("info-content");

	if (toggleBtn && infoContent) {
		toggleBtn.addEventListener("click", function () {
			infoContent.classList.toggle("hidden");
		});
	}
});

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