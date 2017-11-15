console.log($);
console.log('you\'re in the world of content.js');
var ans = {};

ans.createSidebar = function() {

    return {
        init: function(){
            alert("why hello there");
        }
    }
}();

ans.createSidebar.init();