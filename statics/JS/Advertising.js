const allOptions = Array.from(document.querySelectorAll('.option'));
const selectedItems = new Set();

function toggleDropdown(dropdown) {
    dropdown.classList.toggle('active');
}

function toggleOption(option) {
    const item = option.textContent.trim();
    if (selectedItems.has(item)) {
        selectedItems.delete(item);
    } else {
        selectedItems.add(item);
    }

    updateSelectedOptions();
}

function updateSelectedOptions() {
    const selectedOptionsDiv = document.getElementById('selectedOptions');
    selectedOptionsDiv.innerHTML = '';

    selectedItems.forEach(item => {
        const selectedOption = document.createElement('div');
        selectedOption.className = 'selected-option';
        selectedOption.textContent = item;
        selectedOptionsDiv.appendChild(selectedOption);
    });
}

function filterOptions(searchTerm) {
    const filteredOptions = allOptions.filter(option => option.textContent.toLowerCase().includes(searchTerm.toLowerCase()));

    allOptions.forEach(option => {
        if (filteredOptions.includes(option)) {
            option.style.display = 'block';
        } else {
            option.style.display = 'none';
        }
    });
}


// ##############################################################################################################

const optionsList = document.getElementById('options-list');
const newOptionInput = document.getElementById('new-option');

const suggestedOptions = ['جنگو', ' پایتون', ' گیت', ' وردپرس'];

function addOption() {
    const newOption = newOptionInput.value.trim();
    if (newOption !== '') {
        const optionItem = document.createElement('li');
        optionItem.textContent = newOption;
        optionsList.appendChild(optionItem);
        newOptionInput.value = '';
    }
}

newOptionInput.addEventListener('input', () => {
    const inputText = newOptionInput.value.trim();
    const suggestionsContainer = document.getElementById('suggestions');
    suggestionsContainer.innerHTML = '';

    if (inputText !== '') {
        const filteredSuggestions = suggestedOptions.filter(option =>
            option.includes(inputText)
        );

        filteredSuggestions.forEach(suggestion => {
            const suggestionItem = document.createElement('div');
            suggestionItem.textContent = suggestion;
            suggestionItem.classList.add('suggestion');
            suggestionItem.addEventListener('click', () => {
                newOptionInput.value = suggestion;
                suggestionsContainer.innerHTML = '';
            });
            suggestionsContainer.appendChild(suggestionItem);
        });
    }
});

optionsList.addEventListener('click', (event) => {
    const clickedOption = event.target;
    if (clickedOption.tagName === 'LI') {
        clickedOption.classList.toggle('selected');
    }
});

