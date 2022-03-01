$("#createProductForm").submit(function(e) {
    e.preventDefault();
    $.ajax({
        url: 'create_product',
        type: 'post',
        headers: {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
        dataType: 'text',
        data:  $('form#createProductForm').serialize(),
        success: function() {
            $('#createProductModal').modal('hide');
            document.getElementById("createProductForm").reset();
            window.location.reload();
         }
     });
});

$("#updateProductForm").submit(function(e) {
    e.preventDefault();
    var idProduct = $('#idProductUpdate')[0].value;
    $.ajax({
        url: 'update_product/' + idProduct,
        type: 'patch',
        headers: {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
        dataType: 'text',
        data:  $('form#updateProductForm').serialize(),
        success: function() {
            $('#updateProductModal').modal('hide');
            document.getElementById("updateProductForm").reset();
            window.location.reload();
        }
    });
});

function get_delete_data(it) {
    var idProduct = it.getAttribute('data-idProduct');
    var modalBody = $("#deleteProductModal");
    modalBody.find("#idProductDelete")[0].value = idProduct;
}

function delete_product() {
    var idProduct = $("#idProductDelete")[0].value;
    $.ajax({
        url: 'delete_product/' + idProduct,
        type: 'DELETE',
        headers: {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
        success: function() {
            window.location.reload();
        }
    });
}

function get_update_data(it) {
    var idProduct = it.getAttribute('data-id');
    var name = it.getAttribute('data-name');
    var price = it.getAttribute('data-price');
    var stock = it.getAttribute('data-stock');
    var canBeSold = it.getAttribute('data-canBeSold');
    var modalBody = $('#updateProductModal');
    modalBody.find('#idProductUpdate')[0].value = idProduct;
    modalBody.find('#id_name')[0].value = name;
    modalBody.find('#id_price')[0].value = price;
    modalBody.find('#id_stockpile')[0].value = stock;
    if (canBeSold === "True") {
        modalBody.find('#id_can_be_sold')[0].checked = true;
    } else if (canBeSold === "False") {
        modalBody.find('#id_can_be_sold')[0].checked = false;
    }
}