// 9012 괄호
// https://www.acmicpc.net/problem/9012

let input = require('fs').readFileSync('dev/stdin.txt').toString().split('\n');

input.shift()

input.forEach((bracket,idx)=>{
    console.log(idx)
    const bracketArray = bracket.split('')

    const stack = []
    while(bracketArray.length>0){
        // (이면 stack에 넣기

        if(bracketArray[0] === ')' && stack[stack.length-1] === '('){
           console.log('gg')
        }

        stack.push(bracketArray.shift())

    }
    console.log(stack)

})