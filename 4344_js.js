let input = require('fs').readFileSync('dev/stdin.txt').toString().split('\n');
let count = Number(input[0]);

const arr = []

for(let i = 1;i<=count;i++){
    const point = input[i].split(' ')

    const students = parseInt(point[0]);
    const sum = point.reduce((acc,cur)=> parseInt(acc)+parseInt(cur),0)-students
    const avg = sum/students


    const overAvg = point.reduce((acc,cur)=> cur>avg?acc+1:acc,0)
    console.log(Math.round(overAvg/students*100000)/1000)
}



// 350/5 70