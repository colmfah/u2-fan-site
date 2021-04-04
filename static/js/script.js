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

function loaded(userRating) {
    let elms = document.querySelectorAll("input")
    for (i = 0; i < elms.length; i++) {
        if (userRating >= elms[i].value) {
            elms[i].checked = true
            break
        }
    }
}

function submitReview(event) {

    if (rating === 0 && !warnedAboutZeroVote) {
        event.preventDefault()
        document.getElementsByClassName('warning')[0].style.display = "block"
        document.querySelectorAll("fieldset")[0].style.border = "3px solid tomato"
    }
}