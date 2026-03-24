$(document).ready(function(){
    $('.one-post').hover(
        function(event){
            $(event.currentTarget).find('.one-post-shadow').stop(true, true).animate({opacity: '0.3'}, 300);
        },
        function(event){
            $(event.currentTarget).find('.one-post-shadow').stop(true, true).animate({opacity: '0'}, 300);
        }
    );

    $('.logo').hover(
    function(){
        $(this).stop(true, true).animate({width: '338px'}, 300);
    },
    function(){
        $(this).stop(true, true).animate({width: '318px'}, 300);
    }
);
});