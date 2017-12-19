var hasFocus = false;

var xhttp = new XMLHttpRequest();
var that = this;
xhttp.onreadystatechange = function () {
    if(this.readyState == 4 && this.status == 200) {
        // console.log(xhttp.responseText);
        that.pass_reqs = JSON.parse(xhttp.response);
        console.log(that.pass_reqs);
    }
};
xhttp.open("GET", "http://127.0.0.1:8000/api/passreqs/?format=json&"+ window.location.hostname +"=", true);
xhttp.send();

$(':password').on('focus', function () {
    console.log($(this).parent());
    if(!$(this).parent().is('#tooltip')) {
        console.log(that.pass_reqs);
        var string = "Password requirements for " + window.location.hostname + " are; \n" +
            "Minimum Length: " + that.pass_reqs[0].length + "\n" +
            "Capital Required: " + Boolean(parseInt(that.pass_reqs[0].capitals)) + "\n" +
            "Special Characters Required: " + Boolean(parseInt(that.pass_reqs[0].special_characters)) + "\n" +
            "Complexity Required: " + Boolean(parseInt(that.pass_reqs[0].complex));
        $(this).wrap('<div id="tooltip" data-tip="'+ string +'"></div>');
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
            $(':password').unwrap('#tooltip');
        }
    }, 1000);
    hasFocus = false;
});