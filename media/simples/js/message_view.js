// 
// Javascript code for use on the message view.
//
// $Id: message_view.js 126 2010-11-01 01:16:26Z hguerreiro $
//

var show_details = 0;

$(document).ready(function() {
    $("#show_details").click(function (e) {
        e.preventDefault();
        if (show_details == 1) {
            show_details = 0;
            $("#msg_details").hide()
            $("#details_hr").show()
            $("#show_details").html("Show details")
        } else {
            show_details = 1;
            $("#msg_details").show()
            $("#details_hr").hide()
            $("#show_details").html("Hide details")
            }
        });
    });
