const stories = document.getElementById("short-story-header");
const poems = document.getElementById("poem-header");
const other = document.getElementById("other-header");

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