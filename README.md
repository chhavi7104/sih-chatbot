# Sih-Chatbot  (Smart India Hackathon)
<p> A chatbot based on ganga river and its culture. </p>


# 🧳 Chacha Chaudhary Ganga Tour Guide Chatbot

Welcome to the **Chacha Chaudhary Ganga Tour Guide Chatbot**!  
This friendly assistant, inspired by the legendary Indian comic character **Chacha Chaudhary**, helps tourists explore the beauty, culture, and attractions along the **Ganga River across Indian states**.
---

## 🌟 Features

- 🤖 **Role-based interaction**: Chacha Chaudhary as your witty, knowledgeable guide  
- 🌊 **Regional coverage**: Tourist spots near the Ganga in *Uttarakhand, Uttar Pradesh, Bihar, Jharkhand, and West Bengal*  
- 🏞️ **Supports queries** about weather, places to visit, local time, and general help  
- 📚 **Context-aware responses** (e.g., follow-up questions on weather)


---

## 📁 Dataset Structure

Each intent in the dataset is structured like this:

```json
{
  "tag": "ask_weather",
  "patterns": ["What's the weather like in Haridwar?", "Is it raining in Varanasi?"],
  "responses": ["Chacha says: Looks like a sunny day in Haridwar!", "No rain in Varanasi today, enjoy your trip!"],
  "context_set": "weather"
}
```

- tag: Unique ID for the intent

- patterns: Example user inputs

- responses: Chacha-style chatbot replies

**context_set & context_filter: Enable contextual dialogue**

🚀 Setup Instructions
Clone this repo:

```bash
git clone https://github.com/chhavi7104/sih-chatbot.git
cd chatbot
```
Install dependencies (Python example):

```bash
pip install nltk tensorflow flask numpy kesar
```
Train the model (if using an ML backend):

```bash
python bot.py
python chat.py
```
Run the chatbot:


```bash
python app.py
```
Access via browser at: http://127.0.0.1:5000

**🧠 Future Enhancements**
- Integrate real-time weather APIs

- Add multilingual support (Hindi, Bengali, Bhojpuri)

- Voice-enabled interaction with Chacha Chaudhary's tone

- Expand tourist guides to Yamuna, Brahmaputra rivers

**👳 About the Character**
Chacha Chaudhary – the iconic Indian comic hero with a brain faster than a computer – guides users with humor, wisdom, and regional insights. He’s everyone's favorite “chacha” with answers for everything!

