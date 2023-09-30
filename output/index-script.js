const stories = document.getElementById("short-story");
const poems = document.getElementById("poems");
const other = document.getElementById("other");

makeClickable(stories);
makeClickable(poems);
makeClickable(other);

function makeClickable(element) {
    element.addEventListener('click', event => {
        if(element.parentElement.classList.contains("hidden")) {
            element.parentElement.classList.remove("hidden");
            element.parentElement.classList.add("shown");
        } else {
            element.parentElement.classList.remove("shown");
            element.parentElement.classList.add("hidden");
        }
    });
}