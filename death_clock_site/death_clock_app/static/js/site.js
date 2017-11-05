
window.onclick = function (event) {
    if (!event.target.matches('.dropdown')) {
        var dropdowns = document.getElementsByClassName("dropdown_content");
        for (var i = 0; i < dropdowns.length; i++) {
            var dropdown = dropdowns[i];
            if (dropdown.classList.contains('show')) {
                dropdown.classList.remove('show');
            }
        }
    }
}

function profileImageClick() {
    var dropdownContent = document.getElementById("dropdown_content");
    dropdownContent.classList.add('show');
}
