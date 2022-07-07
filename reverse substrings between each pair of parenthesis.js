var reverseParentheses = function(inputString) {
        let str = "";

    let findex = []; 
    for(let i = 0; i < inputString.length; i++){
        if(inputString[i] == '('){
            findex.push(i);
        }
        if(inputString[i] == ')'){
            str = inputString.substring(findex[findex.length-1]+1, i);//the element inside the bracket

            var sub = inputString.substring(0,findex[findex.length-1]);
            sub += str.split("").reverse().join("");
            sub += inputString.substring(i+1,inputString.length);
            inputString = sub;
            findex.pop();
            i-=2;
        }
    }
    return inputString;
};
