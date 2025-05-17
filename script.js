const chatbox = document.getElementById('chatbox');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const typingIndicator = document.getElementById('typing-indicator');
const clearBtn = document.getElementById('clear-btn');

function getTime() {
  const now = new Date();
  return now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

function appendMessage(text, sender) {
  const messageDiv = document.createElement('div');
  messageDiv.classList.add('message', sender);

  // Text content
  const msgText = document.createElement('span');
  msgText.textContent = text;
  messageDiv.appendChild(msgText);

  // Timestamp
  const timeSpan = document.createElement('span');
  timeSpan.classList.add('timestamp');
  timeSpan.textContent = getTime();
  messageDiv.appendChild(timeSpan);

  chatbox.appendChild(messageDiv);

  // Smooth scroll
  chatbox.scrollTo({ top: chatbox.scrollHeight, behavior: 'smooth' });
}

chatForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const message = userInput.value.trim();
  if (!message) return;

  appendMessage(message, 'user');
  userInput.value = '';
  userInput.focus();

  typingIndicator.hidden = false;

  try {
    const response = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message })
    });
    const data = await response.json();

    typingIndicator.hidden = true;
    appendMessage(data.response, 'bot');
  } catch (error) {
    typingIndicator.hidden = true;
    appendMessage('Oops! Something went wrong. Try again later.', 'bot');
    console.error('Error:', error);
  }
});

clearBtn.addEventListener('click', () => {
  chatbox.innerHTML = '';
  userInput.focus();
});
