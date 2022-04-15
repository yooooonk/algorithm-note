// Fly me to the Alpha Centauri
// https://www.acmicpc.net/problem/1011

let input = require('fs').readFileSync('dev/stdin.txt').toString().split('\n')
const testCase = parseInt(input[0])

for(let i=1;i<=testCase;i++){
    const [x,y] = input[i].split(' ')
    solution(parseInt(y)-parseInt(x))
}

function solution(distance){

    if(distance<=3){
        console.log(distance)
        return;
    }

    const n = Math.floor(distance**0.5);

    if(distance === n**2){
        console.log(2*n-1)
    }else if(distance>n**2 && distance<=n**2+n){
        console.log(2*n)
    }else{
        console.log(2*n+1)
    }

}
