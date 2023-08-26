

let currentIndex = 0;

function showImage(indexChange) {
    currentIndex = (currentIndex + indexChange + images.length) % images.length;
    const imageElement = document.getElementById("image");
    const titleElement = document.getElementById("image-title");

    imageElement.src = images[currentIndex].src;
    imageElement.alt = "تصویر " + (currentIndex + 1);

    titleElement.textContent = images[currentIndex].title;
}

showImage(0);