console.log('connected')

let rating = 0

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems);
});

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems);
});

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems);
});

let reviewLinks = document.getElementsByClassName("review-flex");

let myFunction = function () {
    var attribute = this.getAttribute("data-myattribute");
    console.log(attribute);
};

Array.from(reviewLinks).forEach((e, i) => { reviewLinks[i].addEventListener('click', stopPropagation, false); })



function stopPropagation(event) {
    event.stopPropagation()
}

function changeRating(newRating) {
    rating = newRating
}