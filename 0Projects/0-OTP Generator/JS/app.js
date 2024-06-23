const switchBtn = document.getElementById("checkbox");
const generatedOTP = document.getElementById("generate-otp-codeID");
const otpInputList = document.getElementById("otp-input-listID");
                                                
//Event handler - switch-btn-toggler
switchBtn.addEventListener("click", function (){
    let root = document.querySelector(":root");
    let rootStyle = getComputedStyle(root);
    const isWhite = rootStyle.getPropertyValue("--theme-bg-white");

    if (isWhite === "#e0e0e0"){
        root.style.setProperty("--theme-bg-white", "#4e4a4a");
    }
    else {
        root.style.setProperty("--theme-bg-white", "#e0e0e0");
    }
});


function displayOTP(){
    generatedOTP.innerHTML = `
        <div>OTP code is</div>
        <button class="reset-btn">reset</button>
        <div>expire in 0s</div>
    `;
}

setTimeout(displayOTP, 1000);

const checkOTP = (elem) => {
    const currElem = elem.target;
    const currVal = elem.target.value;

    const nextChild = currElem.nextElementSibling;

    //Forword to next
    if (nextChild){
        nextChild.focus();
    }
};

otpInputList.addEventListener("input", checkOTP);