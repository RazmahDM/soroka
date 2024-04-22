let show__menu = document.querySelector("#show__menu");
let hide__menu = document.querySelector("#hide__menu");

let menu = document.querySelector("ul")

show__menu.addEventListener("click", (e) => {
    menu.classList.remove("disabled")
    show__menu.classList.add("disabled")
    hide__menu.classList.remove("disabled")
})

hide__menu.addEventListener("click", (e) => {
    menu.classList.add("disabled")
    show__menu.classList.remove("disabled")
    hide__menu.classList.add("disabled")
})