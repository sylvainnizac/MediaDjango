function logout() {
    $.ajax({
        url: '../users/logout',
        type: 'get',
        success: function(destination) {
            window.location.href = destination;
        }
    });

}