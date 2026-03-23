var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(e) {
        var postBlock = e.target.closest(".one-post");

        if (postBlock.classList.contains("folded")) {
            postBlock.classList.remove("folded");
            e.target.innerHTML = "Свернуть";
        } else {
            postBlock.classList.add("folded");
            e.target.innerHTML = "Развернуть";
        }
    });
}