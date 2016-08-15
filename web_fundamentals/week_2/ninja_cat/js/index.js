$(document).ready(function(){
    // store image sources based on index
    $(".img-corral__img").each(function(index, obj){
        var sources = {
            "ninja": "./img/ninja" + index + ".png",
            "cat": "./img/cat" + index + ".png"
        }
        $(this).data(sources);
    });

    // swap image source
    $(".img-corral__img").click(function(){
        var sources = $(this).data();
        var currentSource = $(this).attr('src');
        var rexp = new RegExp(/ninja/);
        var newSource = rexp.test(currentSource) ? sources.cat : sources.ninja;

        $(this).attr('src', newSource);
    });
});
