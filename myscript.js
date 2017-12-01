var hasFocus = false;

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

console.log(window.location.hostname);