/*
 * https://www.codeeval.com/open_challenges/31/
 *
 */

var fs = require("fs");

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
    if (line !== "") {

        var arr = line.split(",");

        console.log(arr[0].lastIndexOf(arr[1]));
    }
});
