$(document).ready(function(){
    $(".user-form").submit(function(event) {
        var newRow =    "<tr><td>" + $("#firstName").val() + "</td>" +
                        "<td>" + $("#lastName").val() + "</td>" +
                        "<td>" + $("#email").val() + "</td>" +
                        "<td>" + $("#phone").val() + "</td></tr>";

        $(".user-table").append(newRow);
        return false;
    });
});
