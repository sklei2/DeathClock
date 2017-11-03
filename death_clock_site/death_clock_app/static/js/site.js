window.onclick = function(event) {
    if (!event.target.matches('.dropdown')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++){
            var openDropdown = dropdowns[i];
            if (content.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

function profileImageClick() {
    var dropdownContent = document.getElementById("profile_dropdown_content");
    dropdownContent.classList.add('show');
}
