$("#createSellForm").submit(function(e) {
    e.preventDefault();
    var formValid = document.getElementById("createSellForm").checkValidity();
    if (formValid) {
        $.ajax({
            url: "create_sell",
            type: "post",
            headers: {"X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken")[0].value},
            dataType: "text",
            data:  $("form#createSellForm").serialize(),
            success: function() {
                $("#createSellModal").modal("hide");
                document.getElementById("createSellForm").reset();
                window.location.reload();
            }
        });
    } else {
        var errorMsgArea = document.getElementById("error_msg_create");
        var textToAdd = document.createTextNode("You need to add a name and a product to your sell.");
        if (errorMsgArea.hasChildNodes()) {
            errorMsgArea.removeChild(errorMsgArea.lastChild);
        }
        errorMsgArea.appendChild(textToAdd);
    }
});

$("#updateSellForm").submit(function(e) {
    e.preventDefault();
    var formValid = document.getElementById("updateSellForm").checkValidity();
    var idSell = $("#idSellUpdate")[0].value;
    if (formValid) {
        $.ajax({
            url: "update_sell/" + idSell,
            type: "patch",
            headers: {"X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken")[0].value},
            dataType: "text",
            data:  $("form#updateSellForm").serialize(),
            success: function() {
                $("#updateSellModal").modal("hide");
                document.getElementById("updateSellForm").reset();
                window.location.reload();
            }
        });
    } else {
        var errorMsgArea = document.getElementById("error_msg_update");
        var textToAdd = document.createTextNode("Your sell needs a name and a product.");
        if (errorMsgArea.hasChildNodes()) {
            errorMsgArea.removeChild(errorMsgArea.lastChild);
        }
        errorMsgArea.appendChild(textToAdd);
    }
});

function get_update_data(it) {
    var idSell = it.getAttribute("data-id");
    var clientName = it.getAttribute("data-client-name");
    var idProduct = it.getAttribute("data-product");
    var quantity = it.getAttribute("data-quantity");
    var modalBody = $("#updateSellModal");
    modalBody.find("#idSellUpdate")[0].value = idSell;
    modalBody.find("#id_client_name")[0].value = clientName;
    modalBody.find("#id_product")[0].value = idProduct;
    modalBody.find("#id_quantity")[0].value = quantity;
}

function get_delete_data(it) {
    var idSell = it.getAttribute("data-idSell");
    var modalBody = $("#deleteSellModal");
    modalBody.find("#idSellDelete")[0].value = idSell;
}

function delete_sell() {
    var idSell = $("#idSellDelete")[0].value;
    $.ajax({
        url: "delete_sell/" + idSell,
        type: "DELETE",
        headers: {"X-CSRFToken": document.getElementsByName("csrfmiddlewaretoken")[0].value},
        success: function() {
            window.location.reload();
        }
    });
}
