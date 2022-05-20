// 나무자르기
// https://www.acmicpc.net/problem/2805

let input = require('fs').readFileSync('dev/stdin.txt').toString().split('\n')

const n = Number(input[0].split(' ')[1])
const treeArr = input[1].split(' ').map((tree)=>Number(tree))
console.log(solution(n,treeArr))

function solution(need,trees){

    let min = 0;
    let max = Math.max(...trees)
    let answer = 0;

    while(min<=max){
        let h = Math.ceil((min+max)/2)

        let tree = trees.reduce((acc,tree)=> tree>h? acc + (tree - h):acc,0)

        if(tree>=need){
            answer = h;
            min = h+1;
        }else{
            max = h-1
        }


    }

   return answer;
}
