// selectors
const closeNavbar=document.querySelector(".navbar-mobile-close");
const navbarMobile=document.querySelector(".navbar-mobile");
const navbarToggler=document.querySelector(".navbar-toggler");
const headerTitle=document.querySelector(".header-title")
const loading=document.querySelector(".loading")
const mediaQuery = window.matchMedia('(max-width: 1007px)')
const mediaQueryCard= window.matchMedia('(min-width: 850px) and (max-width: 1007px)')
let lengthCardProjects=false;
let lengthCardProjects2=false;
// end selectors
// events
closeNavbar.addEventListener("click",navbarClose)
navbarToggler.addEventListener("click",navbarToggle)
window.addEventListener("load",load)
// end events
// functions
// navbar mobile
function navbarClose(){
    navbarMobile.style.left="100%"
}
function navbarToggle(){
    navbarMobile.style.left="0"
}
function load(){
    loading.style.display="none"
}
if (mediaQuery.matches) {
    lengthCardProjects=true
}
if(mediaQueryCard.matches){
    lengthCardProjects2=true;
}
// end navbar mobile
// typewriter title
const typewriter=new Typewriter(headerTitle,{
    loop:true,
    autoStart:true,
    strings:['اینجا قراره با تیم قدرتمند ما اشنا شوید','ما میتوانیم در زمینه های مختلفی به شما کمک کنیم','طراحی سایت','فرانت اند','بک اند','ui ux','طراحی اپلیکیشن','کاتلین','پایتون','جاوا اسکریپت']
})
// end typewriter title
// swiper slide
new Swiper(".swiper1",{
    // loop: true,
    pagination:{
        el: ".swiper-pagination1",
        clickable: true,
    },
    slidesPerView:lengthCardProjects==true?lengthCardProjects2==true?2:1:3,
    autoplay: true,
})
new Swiper(".carousel-sampleas",{
    loop: true,
    autoplay: true,
    pagination:{
        el: ".carousel-sampleas-pagination",
        clickable: true,
    },
    slidesPerView:1.5,
    navigation:{
        nextEl:".carousel-sampleas-next",
        prevEl:".carousel-sampleas-prev"
    },
})
// end swiper slide
// end functions

