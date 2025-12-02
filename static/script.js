const button = document.getElementById('myBtn');
const result = document.getElementById('result');
const myImage = document.getElementById('myImage');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const hideBtn = document.getElementById('hideBtn');

let currentIndex = 0;

const images = [
    'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Github-desktop-logo-symbol.svg/2048px-Github-desktop-logo-symbol.svg.png',
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQLNTyj7qc5md7ZuQkkJEwYB6E_Pl_hbGba9g&s',
    'https://githubnext.com/assets/images/next-octocat.svg',
]

button.addEventListener('click', function(){
    result.textContent = 'Клик!';
    result.style.color = "green";
});

nextBtn.addEventListener('click', function(){
    currentIndex++;
    if(currentIndex >= images.length){
        currentIndex = 0;
    }
    myImage.src = images[currentIndex];
    console.log(" ", currentIndex + 1)
});


