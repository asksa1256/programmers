function solution(n) {
    const arr = String(n).split("");  // ["1", "1", "8", "3", "7", "2"]
    const numArr = arr.map(a => a*1); // [1, 1, 8, 3, 7, 2]
    const descNumArr = numArr.sort((a,b) => b-a);
    return descNumArr.join("")*1;
}