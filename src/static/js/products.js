$(document).ready(function() {
  
});

function delete_product(it) {
    var idProduct = it.getAttribute('data-idProduct');
    $.ajax({
        url: 'delete_product/' + idProduct,
        type: 'DELETE',
        headers: {'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value},
        success: function() {
            window.location.reload();
        }
    });
}

function create_product() {
    var formValid = document.getElementById("createProductForm").checkValidity();

    if (formValid) {
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
    }
}

function get_update_data(it) {
    var idProduct = it.getAttribute('data-id');
    var name = it.getAttribute('data-name');
    var price = it.getAttribute('data-price');
    var stock = it.getAttribute('data-stock');
    var modalBody = $('#updateProductModal');
    modalBody.find('#idProduct')[0].value = idProduct;
    modalBody.find('#id_name')[0].value = name;
    modalBody.find('#id_price')[0].value = price;
    modalBody.find('#id_stockpile')[0].value = stock;
}

function update_product() {
    var formValid = document.getElementById("updateProductForm").checkValidity();
    var idProduct = $('#idProduct')[0].value;
    if (formValid) {
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
    }
}
