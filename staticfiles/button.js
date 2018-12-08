// Grid e List
let show = false;

document.getElementById("grid").addEventListener('click', toggleMenuGrid);
document.getElementById("list").addEventListener('click', toggleMenuList);

function toggleMenuGrid() {
    if (show){
        document.getElementById("card-block").classList.remove("show-list");
        document.getElementById("card-block").classList.add("show-grid");

        show = false;
    } 
}

function toggleMenuList() {
    if (!show){
        document.getElementById("card-block").classList.remove("show-grid");
        document.getElementById("card-block").classList.add("show-list");

        show = true;
    }
}