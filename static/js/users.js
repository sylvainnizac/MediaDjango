function login() {
    var formValid = document.getElementById("logInForm").checkValidity();

    if (formValid) {
        $.ajax({
            url: 'login',
            type: 'post',
            headers: {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
            dataType: 'text',
            data:  $('form#logInForm').serialize(),
            success: function(destination) {
                window.location.href = destination;
                document.getElementById("logInForm").reset();
            },
            error: function(xhr, ajaxOptions, thrownError) {
                var errorMsgArea = document.getElementById("error_msg");
                var textToAdd = document.createTextNode(xhr.responseText);
                if (errorMsgArea.hasChildNodes()) {
                    errorMsgArea.removeChild(errorMsgArea.lastChild);
                }
                errorMsgArea.appendChild(textToAdd);
            }
        });
    }
}
