// 그룹단어체커
// https://www.acmicpc.net/problem/1316

let input = require('fs').readFileSync('dev/stdin.txt').toString().split('\n')
const count = parseInt(input[0])

let result = 0;

for(let i=1;i<=count;i++){
    if(isGroupWord(input[i])){
        result ++;
    }
}

console.log(result)


function isGroupWord(word){

    let result = true;

    const wordArr = word.split('')
    const prevArr = [wordArr[0]]
    wordArr.reduce((prev,cur,i,arr)=>{

        if(prev !== cur){
            if(prevArr.includes(cur)){
                result = false;
                arr.splice(1) //break;
            }else{
                prevArr.push(cur)
            }
        }

        return cur
    })

    return result;


}