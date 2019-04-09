const up_vote_btn = document.getElementById('js_test');

function voteUp(e) {
    console.log(e.target.dataset)
}

up_vote_btn.addEventListener('click', voteUp);