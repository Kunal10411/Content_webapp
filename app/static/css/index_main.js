document.addEventListener("DOMContentLoaded", function () {
    const videoElements = document.querySelectorAll(".video");

    videoElements.forEach(video => {
        video.addEventListener("click", function () {
            const videoId = video.getAttribute("data-video-id");
            console.log(`Video ID: ${videoId}`);
            if (videoId) {
                // Open the video in a new tab
                window.open(`https://www.youtube.com/watch?v=${videoId}`, "_blank");
            }
        });
    });
});
