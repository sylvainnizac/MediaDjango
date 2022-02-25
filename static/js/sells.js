$(document).ready(function() {

});

function create_sell() {
    var formValid = document.getElementById("createSellForm").checkValidity();

    if (formValid) {
        $.ajax({
            url: 'create_sell',
            type: 'post',
            headers: {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
            dataType: 'text',
            data:  $('form#createSellForm').serialize(),
            success: function() {
                $('#createSellModal').modal('hide');
                document.getElementById("createSellForm").reset();
                window.location.reload();
            }
        });
    }

}