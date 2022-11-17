'use strict'

const element = document.getElementById('target')
const arr = ['First', 'Second', 'Third']
for(const i of arr){
    const node = document.createElement('LI')
    element.appendChild(node)
    node.innerHTML = `${i} item`
}
element.className = 'my-item'