// console.log($);
console.log('you\'re in the world of content.js');

// console.log($(':password').is(':focus'));

var hasFocus = false;

$(':password').on('focus', function () {
    console.log($(this).parent());
    if(!$(this).parent().is('#tooltip')) {
        console.log($(this));
        $(this).wrap('<div id="tooltip" data-tip="testing tooltip"></div>');
        this.focus();
        console.log('password box has focus');
        hasFocus = true;
    }
});

$(':password').focusout(function () {
    setTimeout(function () {
        var focus = $(document.activeElement);
        console.log(focus);
        if(focus.is('#tooltip')) {
            console.log('test');
        }
        if (focus.is(':password') || $(':password').has(focus).length) {
            console.log("still focused");
        } else {
            // console.log(".focusout");
            $(':password').unwrap();
        }
    }, 1000);
    console.log('focus lost');
    hasFocus = false;
});

// var ans = {};
//
// ans.createSidebar = function() {
//
//     return {
//         init: function(){
//             console.log('init func');
//         }
//     }
// }();
//
// ans.createSidebar.init();