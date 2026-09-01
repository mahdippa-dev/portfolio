const animatedContents = [
    {
        title: "Junior Backend Developer",
        description: "Python & Django Developer"
    },
    {
        title: "Python Developer",
        description: "علاقه‌ مند به ساخت اپلیکیشن‌ های وب"
    },
    {
        title: "Future Full Stack Developer",
        description: "در مسیر یادگیری و پیشرفت در دنیای برنامه ‌نویسی"
    }
];


const titleElement = document.getElementById("animated-title");
const descriptionElement = document.getElementById("animated-description");


let currentIndex = 0;


function changeText() {

    titleElement.classList.remove("show");
    descriptionElement.classList.remove("show");


    setTimeout(() => {

        currentIndex =
            (currentIndex + 1) % animatedContents.length;


        titleElement.textContent =
            animatedContents[currentIndex].title;

        descriptionElement.textContent =
            animatedContents[currentIndex].description;


        titleElement.classList.add("show");
        descriptionElement.classList.add("show");

    }, 500);
}


titleElement.textContent =
    animatedContents[currentIndex].title;

descriptionElement.textContent =
    animatedContents[currentIndex].description;


titleElement.classList.add("show");
descriptionElement.classList.add("show");


setInterval(changeText, 4000);