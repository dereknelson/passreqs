chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
    if(changeInfo.status === "complete") {
        console.log("alert from background.js");
        console.log(changeInfo);

        chrome.tabs.executeScript(null, { file: "node_modules/jquery/dist/jquery.js" }, function() {
            console.log('jQuery loaded');
            chrome.tabs.insertCSS(null, {file: "tooltip.css"}, function () {
                console.log('css loaded');
                chrome.tabs.executeScript(null, { file: "myscript.js" }, function (result) {
                    console.log('content loaded')
                });
            });
        });
    }
});