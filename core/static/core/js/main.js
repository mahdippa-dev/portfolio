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


// animation-work-status
const workStatusTitle = document.getElementById("work-status-title");
const workStatusMessage = document.getElementById("work-status-message");

if (workStatusTitle) {

    const titleText = workStatusTitle.textContent.trim();
    const messageText = workStatusMessage
        ? workStatusMessage.textContent.trim()
        : "";

    workStatusTitle.textContent = "";

    if (workStatusMessage) {
        workStatusMessage.textContent = "";
    }

    let titleIndex = 0;
    let messageIndex = 0;


    function typeTitle() {

        if (titleIndex < titleText.length) {

            workStatusTitle.textContent += titleText[titleIndex];

            titleIndex++;

            setTimeout(typeTitle, 100);

        } else {

            setTimeout(typeMessage, 500);

        }
    }


    function typeMessage() {

        if (!workStatusMessage) {
            setTimeout(startTyping, 2000);
            return;
        }

        if (messageIndex < messageText.length) {

            workStatusMessage.textContent += messageText[messageIndex];

            messageIndex++;

            setTimeout(typeMessage, 60);

        } else {

            setTimeout(startTyping, 3000);

        }
    }


    function startTyping() {

        titleIndex = 0;
        messageIndex = 0;

        workStatusTitle.textContent = "";

        if (workStatusMessage) {
            workStatusMessage.textContent = "";
        }

        typeTitle();
    }


    typeTitle();
}
// ********