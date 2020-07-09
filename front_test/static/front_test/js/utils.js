function requestAjax(method, url, data, callback) {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: method,
        url: url,
        data: data,
        dataType: "json",
        beforeSend: function(request){
            request.setRequestHeader("X-CSRFToken", csrftoken);
        },
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

var setCookie = function(name, value, exp) {
    var date = new Date();
    date.setTime(date.getTime() + exp*24*60*60*1000);
    document.cookie = name + '=' + value + ';expires=' + date.toUTCString() + ';path=/';
};

var getCookie = function(name) {
    var value = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    return value? value[2] : null;
};

var delCookie = function(name) {
    document.cookie = name + '=; expires=Thu, 01 Jan 1999 00:00:10 GMT;';
};
