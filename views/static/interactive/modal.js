function deleteBucket() {
	var deleteUrl = document.body.getAttribute('data-delete-url');
	location.href = deleteUrl;
}

function deleteIncome() {
	var deleteUrl = document.body.getAttribute('data-delete-url');
	location.href = deleteUrl;
}

function openModal() {
	document.getElementById("myModal").style.display = "block";
}

function closeModal() {
	document.getElementById("myModal").style.display = "none";
}
