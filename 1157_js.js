// 단어공부
// https://www.acmicpc.net/problem/1157

let input = require('fs').readFileSync('dev/stdin.txt').toString().split('\n')[0];

// 1. 대문자로 바꾸기
const upper = input.toUpperCase()

// 2. split으로 자르기
const arr = upper.split('')
const dic = {}

// 3. 순회하면서 dic만들기
for(let i=0;i<arr.length;i++){
    const word = arr[i]

    if(Object.keys(dic).includes(word)){
        dic[word] = dic[word]+1
    }else{
        dic[word] = 1
    }
}

// 4. dic 제일 큰 값 출력
let max = -1;
let result = '';
Object.keys(dic).forEach((key)=>{
    if(max<dic[key]){
        max = dic[key]
        result = key;
    }
})

const dup = Object.values(dic).filter((value)=>value===max)


if(dup.length===1){
    console.log(result)
}else{
    console.log('?')
}