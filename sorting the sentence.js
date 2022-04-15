/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    let str = s.split(" ");
    let newStr = "";
    for(let i = 0; i < str.length; i++){
        for(let s of str){
            if(s[s.length-1] == String(i+1)){
                newStr += s;
            }
        }
    }
    
    return newStr.replace(/\d/g, " ").trim();
};
