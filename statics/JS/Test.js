    const wrapperCountry = document.querySelector(".wrapper-country");
    const selectBtnCountry = wrapperCountry.querySelector(".select-btn");
    const searchInpCountry = wrapperCountry.querySelector("input");
    const optionsCountry = wrapperCountry.querySelector(".options-country");

    const wrapperJob = document.querySelector(".wrapper-job");
    const selectBtnJob = wrapperJob.querySelector(".select-btn");
    const searchInpJob = wrapperJob.querySelector("input");
    const optionsJob = wrapperJob.querySelector(".options-job");

    let countries = ["آذربایجان شرقی", "آذربایجان غربی", "اردبیل",   "اصفهان" ,
                    "البرز", "ایلام", "بوشهر",   "تهران" ,
                    "چهارمحال و بختیاری", "خراسان جنوبی", "خراسان رضوی",   "خراسان شمالی" ,
                    "خوزستان", "زنجان", "سمنان",   "سیستان و بلوچستان" ,
                    "فارس", "قزوین", "قم",   "کردستان" ,
                    "کرمان", "کرمانشاه", "کهگیلویه و بویراحمد",   "گلستان" ,
                    "گیلان", "لرستان", "مازندران",   "مرکزی" ,
                    "هرمزگان", "همدان", "یزد" ];

    let jobs = ["هوش مصنوعی و داده",
                "شبکه",
                "امنیت",
                "طراحی",
                "برنامه نویسی و توسعه"];

    function addItems(items, selected, optionsElement) {
    optionsElement.innerHTML = "";
    items.forEach(item => {
    let isSelected = item === selected ? "selected" : "";
    let li = `<li onclick="updateSelection(this, '${optionsElement.id}')" class="${isSelected}">${item}</li>`;
    optionsElement.insertAdjacentHTML("beforeend", li);
});
}

    addItems(countries, "", optionsCountry);
    addItems(jobs, "", optionsJob);

    function updateSelection(selectedLi, optionsId) {
    const searchInp = document.querySelector(`#${optionsId}`).previousElementSibling.querySelector("input");
    searchInp.value = "";
    if (optionsId === "options-country") {
    addItems(countries, selectedLi.innerText, optionsCountry);
    selectBtnCountry.firstElementChild.innerText = selectedLi.innerText;
    wrapperCountry.classList.remove("active");
} else if (optionsId === "options-job") {
    addItems(jobs, selectedLi.innerText, optionsJob);
    selectBtnJob.firstElementChild.innerText = selectedLi.innerText;
    wrapperJob.classList.remove("active");
}
}

    function filterItems(items, searchWord, optionsElement) {
    let arr = [];
    let searchWordLower = searchWord.toLowerCase();
    arr = items.filter(data => {
    return data.toLowerCase().startsWith(searchWordLower);
}).map(data => {
    let isSelected = data === optionsElement.previousElementSibling.firstElementChild.innerText ? "selected" : "";
    return `<li onclick="updateSelection(this, '${optionsElement.id}')" class="${isSelected}">${data}</li>`;
}).join("");
    optionsElement.innerHTML = arr ? arr : `<p style="margin-top: 10px;font-size: 20px;"> نتیجه ای یافت نشد</p>`;
}

    searchInpCountry.addEventListener("keyup", () => {
    filterItems(countries, searchInpCountry.value, optionsCountry);
});

    searchInpJob.addEventListener("keyup", () => {
    filterItems(jobs, searchInpJob.value, optionsJob);
});

    selectBtnCountry.addEventListener("click", () => wrapperCountry.classList.toggle("active"));
    selectBtnJob.addEventListener("click", () => wrapperJob.classList.toggle("active"));
    function selectOption(selectedLi, optionsElement) {
    optionsElement.querySelectorAll("li").forEach(li => {
        li.classList.remove("selected");
    });
    selectedLi.classList.add("selected");
}

    // تابع انتخاب گزینه کشور
    optionsCountry.addEventListener("click", (event) => {
    const selectedLi = event.target;
    if (selectedLi.tagName === "LI") {
    selectOption(selectedLi, optionsCountry);
    selectBtnCountry.firstElementChild.innerText = selectedLi.innerText;
    wrapperCountry.classList.remove("active");
}
});

    // تابع انتخاب گزینه شغل
    optionsJob.addEventListener("click", (event) => {
    const selectedLi = event.target;
    if (selectedLi.tagName === "LI") {
    selectOption(selectedLi, optionsJob);
    selectBtnJob.firstElementChild.innerText = selectedLi.innerText;
    wrapperJob.classList.remove("active");
}
});



