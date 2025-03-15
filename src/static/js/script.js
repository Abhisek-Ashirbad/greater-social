const form = document.getElementById("upload-form");

form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    try {
        const response = await fetch("/upload", {
            method: "POST",
            body: formData,
        });
        const result = await response.json();
        if (result.filename) {
            // Redirect to the profile page after successful upload
            window.location.href = "/profile";
        }
    } catch (error) {
        console.error("Error uploading file:", error);
    }
});