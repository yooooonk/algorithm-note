// 셀프넘버
// https://www.acmicpc.net/problem/4673

// 생성자가 있는 수
function d(number){
    return parseInt(number)+number.toString().split('').reduce((acc,cur)=>acc+parseInt(cur),0)
}

// 100000까지 arr 만들기
const range = 10000;
const arr = new Array(range+1).fill(true)

// 셀프넘버 아닌거 지우기
for(let i=1;i<=range;i++){
    arr[d(i)] = false;
}

// 셀프넘버 출력하기
for(let i=1;i<=range;i++){
    if(arr[i]){
        console.log(i)
    }
}


