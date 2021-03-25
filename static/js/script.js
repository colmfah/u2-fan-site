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

function upVote(event, song) {
    event.stopPropagation()
    console.log('upVoted')
}

function changeRating(newRating) {
    rating = newRating
    console.log('rating', rating)
}