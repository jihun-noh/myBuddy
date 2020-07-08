function requestAjax(method, url, data, callback) {
    $.ajax({
        type: method,
        url: url,
        data: data,
        dataType: "json",
        success: function(response){
            console.log(response);
            callback(response);
        },
        error: function(request, status, error){
            console.log(request.responseText);
            alert(request.responseText);
        }
    });
}
