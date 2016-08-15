$(document).ready(function(){
    // .click()
    $("._click").click(function(){
        alert("Hey, you did a good job just there...when you clicked that button. I was like 'Whaaaa, that is such a good click that just took place.'");
    })

    // .focus()
    $("._focus").focus(function(){
        $("._focus-target").html("<span class=\"_bold\">focused</span>");
    })

    // .focusout()
    $("._focus").focusout(function(){
        $("._focus-target").html("<span class=\"_bold\">unfocused</span>");
    })

    // .addclass()
    $("._add-class").click(function(){
        $("#add-class").removeClass().addClass("function-block panel " + $(this).val());
    })

    // .hide()
    $("._hide").click(function(){
        $(".he-man").show().hide();
    })

    // .show()
    $("._show").click(function(){
        $(".he-man").hide().show();
    })

    // .toggle()
    $("._toggle").click(function(){
        $(".he-man").toggle();
    })

    // .fadeIn()
    $("._fadeIn").click(function(){
        $(".he-man").hide().fadeIn(1000);
    })

    // .fadeOut()
    $("._fadeOut").click(function(){
        $(".he-man").show().fadeOut(1000);
    })

    // .slideDown()
    $("._slideDown").click(function(){
        $(".he-man").hide().slideDown("slow");
    })

    // .slideUp()
    $("._slideUp").click(function(){
        $(".he-man").show().slideUp("slow");
    })

    // .slideUp()
    $("._slideToggle").click(function(){
        $(".he-man").slideToggle("slow");
    })

    // .attr(), .text(), .data()
    $("._btn-hover").hover(function(){
        $(".secret-info").html(
            "<p>This button's classes are: " + $(this).attr("class") + "</p>"
        );

        $(".text-info").html(
            "<p>" + $('#' + $(this).attr("name")).text() + "</p>"
        );

        $('#' + $(this).attr("name")).data("button", $(this).attr("value"));
    })

    // .append(), .before(), .after()
    $("._btn-place").click(function(){
        var text = $("#txt-append").val();
        var position = $(".radio-wrapper > input[type=radio]:checked").val();

        if (position === 'append') {
            $("._target-div").append("<p class='_append'>" + text + "</p>");
        } else if (position === 'before') {
            $("._target-element").before("<p class='_before'>" + text + "</p>");
        } else {
            $("._target-element").after("<p class='_after'>" + text + "</p>");
        }
    })
});
