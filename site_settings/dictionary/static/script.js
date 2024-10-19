$(document).ready(function () {
    $('#answer-form').submit(function (event) {
        event.preventDefault();

        $.ajax({
            url: $(this).attr('action'),
            method: 'POST',
            data: $(this).serialize(),
            success: function (data) {
                if (data.game_over) {
                    window.location.href = "/dictionary/gameover/";
                } else {
                    $('#feedback').text(data.message);

                    if (data.message === "Incorrect") {
                        $('#correct-translation').text("Correct translation: " + data.correct_translation);
                    } else {
                        $('#correct-translation').text('');
                    }

                    $('#word-translation').text("Translation: " + data.new_word.translation);

                    $('input[name="correct_word"]').val(data.new_word.word);

                    $('input[name="answer"]').val('');

                    setTimeout(function () {
                        $('#feedback').text('');
                    }, 2000);  // 2 seconds
                }
            },
            error: function (xhr, status, error) {
                console.log("Error:", error);
            }
        });
    });
});
