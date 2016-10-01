var args = require('system').args;
var page = require('webpage').create();

if (args.length < 3 || args.length > 3) {
    console.log('Usage: capture.js URL filename sizeX sizeY');
    phantom.exit();
} 

var url = args[1];
var save = args[2];
var width = 1024;
var height = 768;

page.viewportSize = { width: width, height: height };
page.open(url, function (status) {
    if (status !== 'success') {
            console.log('Unable to load the address!');
        } else {
            window.setTimeout(function () {
                page.render(save);
                phantom.exit();
            }, 200);
        }
});