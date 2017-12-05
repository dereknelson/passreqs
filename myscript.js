var hasFocus = false;

var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function () {
    if(this.readyState == 4 && this.status == 200) {
        console.log(xhttp.responseText);
    }
};
xhttp.open("GET", "http://127.0.0.1:8000/api/passreqs/?format=json&"+ window.location.hostname +"=", true);
xhttp.send();

$(':password').on('focus', function () {
    console.log($(this).parent());
    if(!$(this).parent().is('#tooltip')) {
        $(this).wrap('<div id="tooltip" data-tip="testing tooltip"></div>');
        this.focus();
        hasFocus = true;
    }
});

$(':password').focusout(function () {
    setTimeout(function () {
        var focus = $(document.activeElement);
        if (focus.is(':password') || $(':password').has(focus).length) {
            console.log("still focused");
        } else {
            $(':password').unwrap();
        }
    }, 1000);
    hasFocus = false;
});