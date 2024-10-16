$(document).ready(function () {
    $('#answer-form').submit(function (event) {
        event.preventDefault();
        $.ajax({
            url: $(this).attr('action'),
            method: 'POST',
            data: $(this).serialize(),
            success: function (data) {
                $('#feedback').text(data.message);
                setTimeout(function () {
                    window.location.reload();
                }, 500);
            }
        });
    });
});
