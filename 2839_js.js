// 설탕 배달
// https://www.acmicpc.net/problem/2839

let input = require('fs').readFileSync('dev/stdin.txt').toString().split('\n')
const sugar = parseInt(input[0])

console.log(solution(sugar))

function solution(sugar){
    let count = 0;
    let rSugar = sugar;
    while(rSugar>=0){


        if(rSugar%5===0){
            const n = Math.floor(rSugar/5)

            count += n
            console.log('break',count)
            rSugar -= 5*n;
            break;
        }

        rSugar -=
        count ++;

    }

    if(rSugar!==0){
        count = -1;
    }

    return count;
}
