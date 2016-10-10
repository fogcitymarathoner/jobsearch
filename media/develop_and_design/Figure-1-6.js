
$(document).ready(function () {
$(".original").each(function() {
    $(this).click(function() {
        $(this).fadeOut(200, function() {
                        $(this).css("display", "none");
        });
    });
});        
$(".checked").each(function(){
    $(this).click(function(){
        $(this).children().fadeIn(500);
    });
});
});
