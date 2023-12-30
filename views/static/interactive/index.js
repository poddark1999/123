
document.addEventListener('DOMContentLoaded', function () {
	document.getElementById('search').addEventListener('input', function () {
		var searchTerm = this.value.toLowerCase();
		var buckets = document.getElementsByClassName('bucket-card');

		for (var i = 0; i < buckets.length; i++) {
			var bucketName = buckets[i].getElementsByTagName('h2')[0].textContent.toLowerCase();
			if (bucketName.includes(searchTerm)) {
				buckets[i].style.display = 'block';
			} else {
				buckets[i].style.display = 'none';
			}
		}
	});
});

