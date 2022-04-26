// 영화감독 숌
// https://www.acmicpc.net/problem/1316https://www.acmicpc.net/problem/1436

let input = require('fs').readFileSync('dev/stdin.txt').toString().split('\n')
const count = Number(input[0])

console.log(solution(count))

function solution(cnt){
    let n = cnt;
    let number = 665;
    while(n){
        number++;

        if(number.toString().includes('666')){
            n--;
        }
    }

    return number;
}
