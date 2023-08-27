// const computerChoice = document.getElementById('computer-choice')

// const humanChoice = document.getElementById('human-choice')

// const result = document.getElementById('result')

// const possibleChoices = document.querySelectorAll('button')

// let userChoice

// let computer

// let displayResult

// // main function
// possibleChoices.forEach(possibleChoice => possibleChoice.addEventListener('click',(e) => {
//     userChoice = e.target.id
//     humanChoice.innerHTML = userChoice //whatever the buttons click will display as human choice
//     displayComputerChoice()
//     getResult()
// }))

// function displayComputerChoice() {
//     const randomNUmber = Math.floor(Math.random() * 3) + 1
//     console.log(randomNUmber)

//     if (randomNUmber === 1){
//         computer = 'rock'
//     }

//     if (randomNUmber === 2){
//         computer = 'scissors'
//     }

//     if (randomNUmber === 3){
//         computer = 'paper'
//     }

//     computerChoice.innerHTML = computer
// }

// function getResult() {
//     if (computerChoice === userChoice) {
//         displayResult = 'It is a draw!'
//     }

//     if (computerChoice === 'Rock' && humanChoice === "Scissors") {
//         displayResult = 'You lost!'
//     }

//     if (computerChoice === 'Paper' && humanChoice === "Scissors") {
//         displayResult = 'You won!'
//     }

//     if (computerChoice === 'Scissors' && humanChoice === "Rock") {
//         displayResult = 'You won!'
//     }

//     if (computerChoice === 'Paper' && humanChoice === "Rock") {
//         displayResult = 'You lost!'
//     }

//     result.innerHTML = displayResult
// }

const computerChoiceDisplay = document.getElementById('computer-choice')
const userChoiceDisplay = document.getElementById('human-choice')
const resultDisplay = document.getElementById('result')
const possibleChoices = document.querySelectorAll('button')
let userChoice
let computerChoice
let result

possibleChoices.forEach(possibleChoice => possibleChoice.addEventListener('click', (e) => {
  userChoice = e.target.id
  userChoiceDisplay.innerHTML = userChoice
  generateComputerChoice()
  getResult()
}))

function generateComputerChoice() {
  const randomNumber = Math.floor(Math.random() * 3) + 1 // or you can use possibleChoices.length
  
  if (randomNumber === 1) {
    computerChoice = 'rock'
  }
  if (randomNumber === 2) {
    computerChoice = 'scissors'
  }
  if (randomNumber === 3) {
    computerChoice = 'paper'
  }
  computerChoiceDisplay.innerHTML = computerChoice
}

function getResult() {
  if (computerChoice === userChoice) {
    result = 'its a draw!'
  }
  if (computerChoice === 'rock' && userChoice === "paper") {
    result = 'you win!'
  }
  if (computerChoice === 'rock' && userChoice === "scissors") {
    result = 'you lost!'
  }
  if (computerChoice === 'paper' && userChoice === "scissors") {
    result = 'you win!'
  }
  if (computerChoice === 'paper' && userChoice === "rock") {
    result = 'you lose!'
  }
  if (computerChoice === 'scissors' && userChoice === "rock") {
    result = 'you win!'
  }
  if (computerChoice === 'scissors' && userChoice === "paper") {
    result = 'you lose!'
  }
  resultDisplay.innerHTML = result
}