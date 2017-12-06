
window.onclick = function (event) {
    if (!event.target.matches('.dropdown-toggle')) {
        var dropdowns = document.getElementsByClassName("dropdown");
        for (var i = 0; i < dropdowns.length; i++) {
            var dropdown = dropdowns[i];
            if (dropdown.classList.contains('open')) {
                dropdown.classList.remove('open');
            }
        }
    }
}

function profileImageClick() {
    var dropdownContent = document.getElementById("menuLogin");
    dropdownContent.classList.add('open');
}
