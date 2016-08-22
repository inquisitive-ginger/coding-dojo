$(document).ready(function() {

    // add event listeners to dynamic buttons
    function addBtnListeners(elem) {
        elem.children(".contact-card__flip-btn").click(function(event) {
            elem.children(".cc_back").toggle();
            elem.children(".cc_front").toggle();
        });
    }

    // toggle visibility of card backs
    $(".cc_back").toggle();
    addBtnListeners($(".contact-card").last());

    // add new contact card
    $(".add-contact").click(function(event){
        var newContact =
            '<div class="contact-card">'
            +    '<h1 class="contact-card__name cc_front">' + $(".first-name").val() + ' ' + $(".last-name").val() + '</h1>'
            +    '<input type="button" class="contact-card__flip-btn cc_front btn btn-success" value="Show Description">'
            +    '<p class="contact-card__description cc_back">' + $(".description").val() + '</p>'
            +    '<input type="button" class="contact-card__flip-btn cc_back btn btn-success" value="Hide Description">'
            + '</div>'

        $(".contact-container").append(newContact);
        $(".contact-card").last().children(".cc_back").toggle(); // toggle back side of card without affect others in list
        addBtnListeners($(".contact-card").last());
    });

});
