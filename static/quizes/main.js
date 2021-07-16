console.log('hello world')

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')
const url = window.location.href


modalBtns.forEach(modalBtn=>modalBtn.addEventListener('click',()=>{
    const pk = modalBtn.getAttribute('data-pk')
    
    const name = modalBtn.getAttribute('data-quiz')
    const numQuestions = modalBtn.getAttribute('data-questions')
    const difficulty = modalBtn.getAttribute('data-difficulty')
    const  scoreToPass= modalBtn.getAttribute('data-pass')
    const time = modalBtn.getAttribute('data-time')

    modalBody.innerHTML = "<li>Subject:" + name +'<br/>'+"<li>Number of questions: "
        +numQuestions+'<br/><li>Difficulty Level:'+difficulty+'<br/><li>Score to Pass '
        +scoreToPass+'<br/><li>Time:'+ time
    
    startBtn.addEventListener('click',()=>
    {
        window.location.href = url +pk;
    })

        
}))
