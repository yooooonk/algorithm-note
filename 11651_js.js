// 11651 좌표 정렬하기2
// https://www.acmicpc.net/problem/11651

let input = require('fs').readFileSync('dev/stdin.txt').toString().split('\n');
input.shift()

const xy = input.map(cords=>cords.split(" ").map(num=>Number(num)))

xy.sort((a,b)=>{
    if(a[0]!==b[0]){
        return a[0]-b[0]
    }
    return a[1]-b[1]
})

xy.forEach((i) => {
    //정렬된 좌표들 각각에 대해 answer에 담기
    answer += `${i[0]} ${i[1]}\n`;
});

console.log(answer)

//
//     .sort((a,b)=>{
//    // if(a[0] !== b[0]) return return a[0]-b[0]
// }).forEach(xy=>{
//     console.log(...xy)
// })

