$(document).ready(function() {
  
});

function delete_product(it) {
    var idProduct = it.getAttribute('data-bs-idProduct');
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
    var idProduct = it.getAttribute('data-bs-id');
    var nameProduct = it.getAttribute('data-bs-name');
    var priceProduct = it.getAttribute('data-bs-price');
    var stockProduct = it.getAttribute('data-bs-stock');
    var modalBody = $('#updateProductModal');
    modalBody.find('#idProduct')[0].value = idProduct;
    modalBody.find('#name')[0].value = nameProduct;
    modalBody.find('#price')[0].value = priceProduct;
    modalBody.find('#stockpile')[0].value = stockProduct;
}

function update_product() {
    var formValid = document.getElementById("updateProductForm").checkValidity();
    var idProduct = $('#idProduct')[0].value;
    console.log($('#idProduct'));
    if (formValid) {
        $.ajax({
            url: 'update_product/' + idProduct,
            type: 'post',
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

$("#update_button").click(function () {
    //var name = $("#name").val();
    console.log("here");
    var update_button = document.getElementById("update_button");
    console.log(update_button);

    //$("#modal_body").html(str);
});


//$( '#updateProductModal' ).on
//('show.bs.target' , function(event) {
//    var button = $(event.relatedTarget); // Button that triggered the modal
//    var recipient = button.data('product'); // Extract info from data-* attributes
//    console.log(button)
//    console.log(recipient)
//    //$("#hiddeninputfield").val(recipient);
//})