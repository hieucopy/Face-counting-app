document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    const photoInput = document.getElementById('photoInput');
    const preview = document.getElementById('preview');

    if (photoInput.files && photoInput.files[0]) {
        const reader = new FileReader();

        reader.onload = function(e) {
            preview.innerHTML = `<img src="${e.target.result}" alt="Uploaded Photo">`;
        }

        reader.readAsDataURL(photoInput.files[0]);
    } else {
        preview.innerHTML = `<p>No photo uploaded yet.</p>`;
    }
});
