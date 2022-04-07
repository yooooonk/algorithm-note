// 크로아티아 알파벳
// https://www.acmicpc.net/problem/2941

let input = require('fs').readFileSync('dev/stdin.txt').toString().split('\n')[0];

const pattern = [/c=/g,/c-/g,/dz=/g,/d-/g,/lj/g,/nj/g,/s=/g,/z=/g];

pattern.forEach(reg => {
    input = input.replace(reg, 'Q')
})

console.log(input.length)