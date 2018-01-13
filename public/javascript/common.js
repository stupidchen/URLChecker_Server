//A function to set cookie of 'name = value', expires in timeout days with the specific domain
function setCookie(name, value, timeout) {
    var expireStr;
    if (timeout) {
        var time = new Date();
        time.setTime(time.getTime() + timeout * 24 * 60 * 60 * 1000);
        expireStr = '; expires=' + time.toGMTString(); 
    }
    else {
        expireStr = '';
    }

    var cookieStr = name + '=' + value + expireStr + ';';
    document.cookie = cookieStr;
};

//A function to get the cookie with specific name
function getCookie(name) {
    var cname = name + '=';
    var decodedCookie = decodeURIComponent(document.cookie).split(';');

    for (var i = 0; i < decodedCookie.length; i++) {
        var pair = decodedCookie[i];
        var tmp = pair.indexOf(cname);
        if (tmp != -1) {
            return pair.substring(tmp + cname.length, pair.length); 
        }
    }

    return undefined;
}

//Convert the form data to JSON object
$.fn.serializeObject = function () {
    var o = {};
    var sa = this.serializeArray();
    $.each(sa, function () {
        if (o[this.name] !== undefined) {
            if (!o[this.name].push) {
                o[this.name] = [o[this.name]];
            }
            o[this.name].push(this.value || '');
        }
        else {
            o[this.name] = this.value || '';
        }
    });
    return o;
};

function showNoticeDialog(title, msg, confirmEvent) {
    $('#notice-title').text(title);
    $('#notice-msg').text(msg);
    $('#notice-show-btn').click();
    if (confirmEvent) {
        $('#notice-ok-btn').click(confirmEvent);
    }
}

function showConfirmDialog(title, msg, confirmEvent, cancelEvent) {
    $('#confirm-title').text(title);
    $('#confirm-msg').text(msg);
    $('#confirm-show-btn').click();
    if (confirmEvent) {
        $('#confirm-confirm-btn').click(confirmEvent);
    }
    if (cancelEvent) {
        $('#confirm-cancel-btn').click(cancelEvent);
    }
}

function ajax(method, path, msg, asyn, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open(method, path, asyn);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    //xhr.timeout = 2000;
    xhr.onerror = function () {
        alert("XMLHttpRequest error!");
    }
    xhr.ontimeout = function () {
        alert("Timeout!");
    };
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4) {
            if (xhr.status == 200) {
                callback(JSON.parse(xhr.responseText));
            }
            else {
                alert('Connection failed! Status: ' + xhr.status);
            }
        }
    };
    xhr.send(msg);
}

function redirect(url) {
    window.location = url;
}

function validateToken(callback) {
    var token = getCookie('dsys_token');
    ajax('GET', 'json/user?token=' + token, JSON.stringify(token), true, function (response) {
        if (response.error == 0) {
            $('#dropdown-username').text(response.data.username);
            callback(response.data);
        }
        else {
            redirect('login.html');
        }
    });
}

$('#notice-show-btn').hide();
$('#confirm-show-btn').hide();
