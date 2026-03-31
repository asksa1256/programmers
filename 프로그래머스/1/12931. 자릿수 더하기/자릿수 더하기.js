function solution(n) {
    let splitArr = String(n).split("");
    return splitArr.map((s) => s*1).reduce((a, b) => a+b)
}