// Get modal element
const modal = document.getElementById('applyModal');

// Get open modal button
const btn = document.getElementById('applyBtn');

// Get close button
const span = document.getElementsByClassName('close')[0];

// Open the modal
btn.onclick = function() {
    modal.style.display = 'block';
}

// Close the modal when the user clicks on <span> (x)
span.onclick = function() {
    modal.style.display = 'none';
}

// Close the modal when the user clicks anywhere outside of the modal
window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
}