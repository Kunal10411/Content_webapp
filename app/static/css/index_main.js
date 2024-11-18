document.addEventListener("DOMContentLoaded", () => {
    // Get all video elements in the trending section
    const videos = document.querySelectorAll(".video");
    const modal = document.getElementById("video-modal");
    const modalClose = document.getElementById("close-modal");
    const videoFrame = document.getElementById("video-frame");

    // Add click event listener to each video
    videos.forEach(video => {
        video.addEventListener("click", () => {
            const videoUrl = video.getAttribute("data-video-url");
            if (videoUrl) {
                // Display the modal
                modal.style.display = "block";
                // Set the video URL to the iframe in the modal
                videoFrame.src = videoUrl;
            }
        });
    });

    // Close modal when the close button is clicked
    modalClose.addEventListener("click", () => {
        modal.style.display = "none";
        // Stop the video playback
        videoFrame.src = "";
    });

    // Close modal when clicking outside the modal content
    modal.addEventListener("click", (event) => {
        if (event.target === modal) {
            modal.style.display = "none";
            // Stop the video playback
            videoFrame.src = "";
        }
    });
});
