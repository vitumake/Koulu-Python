'use strict'

const form = document.querySelector('form')
const query = form.querySelector('#query')
const results = document.querySelector('#results')
const dialog = document.querySelector('dialog')
const closeDialog = dialog.querySelector('span')

function createArticle(obj){
    const article = document.createElement('article')
    const figure = document.createElement('figure')
    const figcapt = document.createElement('figcaption')
    const img = document.createElement('img')
    const iframe = document.createElement('iframe')
    const url = document.createElement('a')

    article.className = 'card'
    article.innerHTML += obj.name!=null?`<h2>${obj.name}</h2>`:'<h2><i>no name</i></h2>'
    article.appendChild(figure)
    figure.appendChild(img)
    figure.appendChild(figcapt)
    figcapt.innerHTML = obj.genres.join(' | ')
    img.src = obj.image!=null?obj.image.medium:'./assets/err.svg'
    img.alt = obj.name
    article.innerHTML += obj.summary!=null?obj.summary:'<i>no summary</i><br><br>'
    url.innerHTML = 'Details'
    url.target = 'blank_'
    article.appendChild(url)

    //Iframe event listener
    url.addEventListener('click', e=>{
      iframe.title = obj.name!=null?`<h2>${obj.name}</h2>`:'<h2><i>no name</i></h2>'
      iframe.src = obj.url
      iframe.width = 1000
      iframe.height = 700
      dialog.appendChild(iframe)
      dialog.showModal()
    })
  
    return article
  }

  form.addEventListener('submit', e=>{
    e.preventDefault()
    fetch(`https://api.tvmaze.com/search/shows?q=${query.value}`)
    .then((resp)=>resp.json())
    .then((shows)=>{
        results.innerHTML = ''
        console.log(shows)
        if(shows.length)for(const i of shows) results.appendChild(createArticle(i.show))
        else results.innerHTML = '<i>No results...</i>'
    })
  })

  closeDialog.addEventListener('click', e=>{
    dialog.close()
    dialog.removeChild(dialog.querySelector('iframe'))
  })