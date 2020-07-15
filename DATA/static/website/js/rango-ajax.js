$(document).ready(function() {
    var is_subscrived = $('#subs_func').attr("sub_stat") === 'True';
    //console.log(is_subscrived);
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
            }else {
                $('#subs_func').removeClass("btn-outline-primary").addClass("btn-primary");
                $('#subs_func').html('<i class="fa fa-plus"></i>&nbsp; Subscrive');
                $('#description_sub').show();
            }
        });
        
         
    });


});