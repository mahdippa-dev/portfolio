const contactForm = document.getElementById('contact-form');
const contactMessage = document.getElementById('contact-message');

const emailError = document.getElementById('email-error');
const phoneError = document.getElementById('phone-error');
const formError = document.getElementById('form-error');


if (contactForm) {

    contactForm.addEventListener('submit', function (event) {

        event.preventDefault();

        // پاک کردن خطاهای قبلی
        emailError.textContent = '';
        phoneError.textContent = '';
        formError.textContent = '';

        emailError.classList.remove('show');
        phoneError.classList.remove('show');
        formError.classList.remove('show');

        const formData = new FormData(contactForm);

        fetch(window.location.href, {
            method: 'POST',
            body: formData
        })

            .then(response => response.json())

            .then(data => {

                if (data.success) {

                    // نمایش پیام موفقیت
                    contactMessage.textContent = data.message;

                    contactMessage.classList.add('success');

                    // خالی کردن فرم
                    contactForm.reset();

                    // حذف پیام بعد از 4 ثانیه
                    setTimeout(() => {

                        contactMessage.classList.remove('success');

                    }, 4000);

                } else {

                    // خطای کلی فرم
                    if (data.errors.__all__) {

                        formError.textContent = data.errors.__all__[0];

                        formError.classList.add('show');
                    }


                    // خطای ایمیل
                    if (data.errors.email) {

                        emailError.textContent = data.errors.email[0];

                        emailError.classList.add('show');
                    }


                    // خطای شماره موبایل
                    if (data.errors.phone) {

                        phoneError.textContent = data.errors.phone[0];

                        phoneError.classList.add('show');
                    }

                    // پاک شدن خطاها بعد از 4 ثانیه
                    setTimeout(() => {

                        formError.classList.remove('show');
                        emailError.classList.remove('show');
                        phoneError.classList.remove('show');

                    }, 4000);


                }

            })

            .catch(error => {

                console.error('Error:', error);

            });

    });

}