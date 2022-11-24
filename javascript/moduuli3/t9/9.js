const btn = document.getElementById('start')
const result = document.getElementById('result')

function doMath(vals, opr){
    let result
    switch(opr){
        case '+':
            result = +vals[0] + +vals[1]
            break
        case '-':
            result = +vals[0] - +vals[1]
            break
        case '/':
            result = +vals[0] / +vals[1]
            break
        case '*':
            result = +vals[0] * +vals[1]
    }
    console.log(result)
    return result
}

btn.addEventListener('click', a=>{
    const calc = document.getElementById('calculation').value
    const vals = calc.split(/\+|-|\/|\*/g)
    const opr = calc.match(/\+|-|\/|\*/g)
    result.innerHTML = doMath([vals[0], vals[1]], opr[0])
})