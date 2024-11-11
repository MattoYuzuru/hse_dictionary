$(document).ready(function () {
    $('#answer-form').submit(function (event) {
        event.preventDefault();

        $.ajax({
            url: $(this).attr('action'),
            method: 'POST',
            data: $(this).serialize(),
            success: function (data) {
                if (data.game_over) {
                    window.location.href = "/gameover";
                } else {
                    let feedbackText = data.message === "Incorrect" ? "Correct translation: " + data.correct_translation : '';
                    $('#feedback').text(data.message);
                    $('#correct-translation').text(feedbackText);
                    $('#word-translation').text("Translation: " + data.new_word.translation);
                    $('input[name="correct_word"]').val(data.new_word.word);
                    $('input[name="answer"]').val('');

                    setTimeout(function () {
                        $('#feedback').text('');
                    }, 2000);
                }
            },
            error: function (xhr, status, error) {
                console.log("Error:", error);
            }
        });
    });
});
