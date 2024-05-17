const switchBtn = document.getElementById("checkbox");
                                                //switch-btn-toggler
//Event handler
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
