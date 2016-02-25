var csrftoken = Cookies.get('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


$('#execute').click(function () {
    var form = $('#default_form');
    $.ajax({
        method: 'POST',
        url: 'execute/',
        data: form.serialize()
    }).done(function(html) {
        $('#plots').empty();
        $('#plots').append(html)
    })
});
