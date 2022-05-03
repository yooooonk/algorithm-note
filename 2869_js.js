// 달팽이는 올라가고 싶다
// https://www.acmicpc.net/problem/2869

let input = require('fs').readFileSync('dev/stdin.txt').toString().split('\n')[0].split(' ')

const a = Number(input[0])
const b = Number(input[1])
const v = Number(input[2])

console.log(solution(a,b,v))
function solution(a,b,v){


    return Math.ceil((v-b)/(a-b))
}
