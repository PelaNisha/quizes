console.log('hello world')

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')

modalBtns.forEach(modalBtn=>modalBtn.addEventListener('click',()=>{
    const pk = modalBtn.getAttribute('data-pk')
    console.log(pk)
}))
