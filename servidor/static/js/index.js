foto = document.getElementById('foto')
foto.addEventListener('mouseenter',()=>{
    document.documentElement.style.setProperty('--filter','invert(1)')
    
})
foto.addEventListener('mouseout',()=>{
    document.documentElement.style.setProperty('--filter','none')
})
nome = document.getElementById('nome')
nome.addEventListener('mouseenter',()=>{
    foto.src = url_eu
    
})
nome.addEventListener('mouseout',()=>{
    foto.src = url_eu_desenho
    
})