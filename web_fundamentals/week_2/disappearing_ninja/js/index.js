$(document).ready(function(){
    $(".img-corral__img").click(function(){
        $(this).hide();
    });

    $(".restore-btn").click(function(){
        $(".img-corral__img").each(function(){
            $(this).show();
        });
    });
});
