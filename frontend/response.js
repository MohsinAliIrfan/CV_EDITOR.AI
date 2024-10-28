
function showNotification(message, isSuccess = false) {
    const notification = document.getElementById("notification");
    notification.textContent = message;
    notification.className = isSuccess ? "success" : "";
    notification.style.top = "20px";

    setTimeout(() => {
        notification.style.top = "-100px";
    }, 3000);
}

function processCV() {
    const urlInput = document.getElementById("url").value;
    const cvUploadInput = document.getElementById("cv-upload").files[0];
    const formData = new FormData();

    if (!urlInput && !cvUploadInput) {
        showNotification("Please provide either a CV URL or upload a CV file.", false);
        return;
    }

    if (urlInput) {
        formData.append("url", urlInput);
    }
    if (cvUploadInput) {
        formData.append("cv", cvUploadInput);
    }

    fetch("http://127.0.0.1:8001/process-cv/", {
        method: "POST",
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        showNotification(data.message, true);
        if (data.message === "CV UPDATED SUCCESSFULLY") {
            const downloadButton = document.getElementById("download-cv");
            downloadButton.style.display = "inline-block";
        }
    })
    .catch(error => {
        showNotification("Error: " + error.message, false);
    });
}

document.querySelector(".magic-button").addEventListener("click", processCV);

function processChat() {
    const chatInput = document.getElementById("chat-input").value;
    const messageDisplay = document.getElementById("messageDisplay");
    
    if (!chatInput) {
        showNotification("Please type a message before sending.", false);
        return;
    }

    document.getElementById("chat-input").value = '';

    fetch("http://127.0.0.1:8001/chat_bot/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_query: chatInput }),
    })
    .then(response => response.json())
    .then(data => {
        const agentMessage = document.createElement("div");
        agentMessage.className = "message agent-message";
        agentMessage.textContent = data.message;
        messageDisplay.appendChild(agentMessage);

        messageDisplay.scrollTop = messageDisplay.scrollHeight;
    })
    .catch(error => {
        showNotification("Error: " + error.message, false);
    });
}

document.querySelector(".chat-button").addEventListener("click", processChat);

function downloadCV() {
    const filename = "final_output.docx";  
    const downloadUrl = `http://127.0.0.1:8001/download-cv/?filename=${filename}`;
    
    window.location.href = downloadUrl;
}

document.getElementById("download-cv").addEventListener("click", downloadCV);
