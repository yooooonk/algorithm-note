// 4948 베르트랑 공준
// https://www.acmicpc.net/problem/4948

let input = require('fs').readFileSync('dev/stdin.txt').toString().split('\n');

for(let i=0;i<input.length-1;i++){
    solution(parseInt(input[i]))
}

function solution(n){
    // console.log(n)
    // 1. n-2n 배열만들기
    const arr = []
    for(let i=1;i<=2*n;i++){
        // arr[i] = true;
        arr[i] = i;
    }

    // 2. 에라토스테네스의 체
    // 전체 순회
    for(let i=2;i<=Math.floor(2*n*0.5);i++){
        // true면 j+i를 false로 바꾸기
        if(arr[i]){
            // console.log(i)
            for(let j=i+i;j<= Math.floor(2*n);j+=i){
                arr[j] = false;
            }
        }
    }

    //3. 갯수 구하기
    let result = 0;
    for(let i=n+1;i<=2*n;i++){
        if(arr[i]) result++;

    }

    console.log(result)
}


