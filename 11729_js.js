// 11729 하노이 탑
// https://www.acmicpc.net/problem/11729

let input = require('fs').readFileSync('dev/stdin.txt').toString().split('\n');

const top = Number(input[0])

function hanoi(n,start,end){
    if(n===1){
        console.log(start,end)
        return;
    }

    hanoi(n-1,start,6-start-end)
    console.log(start,end)
    hanoi(n-1,6-start-end,end)


}

console.log(2**top-1)
hanoi(top,1,3)

