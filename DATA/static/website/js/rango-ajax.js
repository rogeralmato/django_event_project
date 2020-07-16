$(document).ready(function() {
    var is_subscrived = $('#subs_func').attr("sub_stat") === 'True';
    if (is_subscrived) {
        $('#subs_func').removeClass("btn-primary").addClass("btn-outline-primary");
        $('#subs_func').html('<i class="fa fa-minus"></i>&nbsp; Unsubscrive');
        $('#description_sub').hide();
    }

    $('#subs_func').click(function(){
        var eventid;
        eventid = $(this).attr("data-eventid");
        var is_subscrived =  $(this).hasClass( "btn-outline-primary" ) === true;
        var subscription_comment = $('#description_sub').val()
        $.get("subscription", {event_id: eventid, subs_status:is_subscrived,subs_comment:subscription_comment}, function(data){
            console.log(data);
            $('#subs_count').html(data.num_subs);
            if (data.sub_status) {
                $('#subs_func').removeClass("btn-primary").addClass("btn-outline-primary");
                $('#subs_func').html('<i class="fa fa-minus"></i>&nbsp; Unsubscrive');
                $('#description_sub').hide();
                $( `<div class=\"card-body\" id=\"assistant_card\"><div class=\"stat-text\"><p><strong>Email: </strong>${data.email}</p></div><div class=\"stat-text\"><p><strong>Comment: </strong>${subscription_comment}</p></div></div>` ).insertAfter( "#assistant_card" );
            }else {
                $('#subs_func').removeClass("btn-outline-primary").addClass("btn-primary");
                $('#subs_func').html('<i class="fa fa-plus"></i>&nbsp; Subscrive');
                $('#description_sub').show();
            }
        });
        
         
    });

    $('#not_logged_subs').click(function(){
        console.log("HEYU");
        var eventid;
        eventid = $(this).attr("data-eventid");
        var subscription_comment = $('#description_not_log').val()
        var email = $('#email_not_log').val()
        console.log(email);
        $.get("subscription_not_logged", {event_id: eventid, subs_email:email,subs_comment:subscription_comment}, function(data){
            $('#subs_count').html(data.num_subs);
            $('#description_not_log').hide();
            $('#not_logged_subs').hide();
            $('#email_not_log').hide();

        });
        $( `<div class=\"card-body\" id=\"assistant_card\"><div class=\"stat-text\"><p><strong>Email: </strong>${email}</p></div><div class=\"stat-text\"><p><strong>Comment: </strong>${subscription_comment}</p></div></div>` ).insertAfter( "#assistant_card" );
         
    });


});