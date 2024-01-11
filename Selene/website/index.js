function toggleChatBox() {
    var chatButton = document.querySelector(".chat-section");
    var chatBox = document.getElementById("chatBox");
    
    chatButton.classList.toggle("rotated"); // Toggle the "rotated" class
    
    if (chatBox.style.display === "none") {
        chatBox.style.display = "block";
    } else {
        chatBox.style.display = "none";
    }
}