/*
 * https://www.codeeval.com/open_challenges/2/
 *
 */

var fs = require("fs");

var strings = fs.readFileSync(process.argv[2]).toString().split('\n');

var answer = strings.slice(1).sort(function(a,b){ return  b.length - a.length; });

for (var i = 0; i < strings[0]; i++) {
    console.log(answer[i]);
}
