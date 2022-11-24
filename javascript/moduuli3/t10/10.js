'use strict'
const form = document.getElementById('source')
const vals = form.querySelectorAll('input')
const result = document.getElementById('target')

form.addEventListener('submit', e=>{
    e.preventDefault()
    result.innerHTML = `You'r name is ${vals[0].value} ${vals[1].value}`
})