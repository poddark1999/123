function checkPassword() {
	var password = document.getElementById('password').value;

	// Check length
	if (password.length >= 8 && password.length <= 30) {
		document.getElementById('length').innerHTML = "✅ Must contain between 8-30 characters";
	} else {
		document.getElementById('length').innerHTML = "❌ Must contain between 8-30 characters";
	}

	// Check uppercase
	if (/[A-Z]/.test(password)) {
		document.getElementById('uppercase').innerHTML = "✅ Must contain at least an uppercase letter";
	} else {
		document.getElementById('uppercase').innerHTML = "❌ Must contain at least an uppercase letter";
	}

	// Check lowercase
	if (/[a-z]/.test(password)) {
		document.getElementById('lowercase').innerHTML = "✅ Must contain at least a lowercase letter";
	} else {
		document.getElementById('lowercase').innerHTML = "❌ Must contain at least a lowercase letter";
	}

	// Check number
	if (/\d/.test(password)) {
		document.getElementById('number').innerHTML = "✅ Must contain at least a number";
	} else {
		document.getElementById('number').innerHTML = "❌ Must contain at least a number";
	}

	// Check special character
	if (/[!@#$%^&*()_+{}[\]:;<>,.?~\\-]/.test(password)) {
		document.getElementById('special').innerHTML = "✅ Must contain at least a special character (!@#$%{}[]&*<>?+=,./)";
	} else {
		document.getElementById('special').innerHTML = "❌ Must contain at least a special character (!@#$%{}[]&*<>?+=,./)";
	}
}

function checkPasswordMatch() {
	var password = document.getElementById('password').value;
	var password2 = document.getElementById('password2').value;

	if (password === password2) {
		document.getElementById('passwordMatch').innerHTML = "✅ Passwords match";
	} else {
		document.getElementById('passwordMatch').innerHTML = "❌ Passwords must match";
	}
}

function checkLengthEmoji() {
	var emoji = document.getElementById('emoji-input');

	// Remove the old constraints list, if it exists
	var oldConstraints = document.getElementById('emoji-constraints');
	if (oldConstraints) {
		oldConstraints.remove();
	}

	// Add the new constraints list
	emoji.insertAdjacentHTML('afterend', '<ul id="emoji-constraints">\
<li id="length">❌ Can up to 1-2 symbols</li>\
</ul> ');
	emoji = emoji.value;
	// Check length
	if (emoji.length > 0 && emoji.length <= 4) {
		document.getElementById('length').innerHTML = "✅ Contains 1-2 symbols";
	}
	else {
		document.getElementById('length').innerHTML = "❌ Must contain 1-2 symbols";
	} // Check uppercase if
}

function updateGoalInput(val) {
	document.getElementById('goalInput').value = parseInt(val).toLocaleString();
}

function updateGoalSlider(val) {
	val = val.replace(/,/g, '');
	document.getElementById('goalSlider').value = val;
}
