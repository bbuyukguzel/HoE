/**
 * Created by roland on 1.10.2016.
 */

var page = require('webpage').create();

// http://phantomjs.org/api/webpage/handler/on-console-message.html
page.onConsoleMessage = function (msg, lineNum, sourceId) {
    console.log('CONSOLE: ' + msg + ' (from line #' + lineNum + ' in "' + sourceId + '")');
};

page.open('http://phantomjs.org/api/webpage/method/evaluate.html', function (status) {

    if (status === "success") {
        if (page.injectJs('inspector.js')) {
            var title = page.evaluate(function () {
                return document.elementFromPoint(107, 216).click();
            });
            console.log(title);
        }
    }
    phantom.exit();

});