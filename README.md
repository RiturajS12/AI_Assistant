<div align="center">
  <img src="https://raw.githubusercontent.com/RiturajS12/AI-Assistant/main/Frontend/Graphics/logo.png" alt="Logo" width="120">
  <h1>🤖 AI Assistant</h1>
  <p>
    A powerful and intelligent desktop AI Assistant built with Python.<br>
    Featuring real-time voice interaction, smart decision-making, automation, web search, image generation, and more — all in an intuitive GUI.
  </p>
  <br />
</div>

---

## ✨ About The Project

**AI Assistant** is a multi-functional desktop assistant developed by [RiturajS12](https://github.com/RiturajS12). It leverages the power of modern AI to understand voice commands, perform web searches, generate images, automate tasks, and carry out natural human-like conversations.

This assistant uses a smart decision-making engine to route queries efficiently to the appropriate module — whether it's for chatting, searching, or creating AI images.

---

## 🚀 Key Features

* 🎙️ **Voice Interaction** – Real-time speech recognition and speech synthesis.
* 💬 **Conversational AI** – Chatbot for human-like conversations.
* 🌐 **Web Search** – Real-time information retrieval from the internet.
* 🎨 **AI Image Generation** – Generate images from text prompts.
* ⚙️ **Task Automation** – Execute predefined automated tasks.
* 🖥️ **GUI Interface** – A sleek, modern interface powered by `CustomTkinter`.
* 🧠 **Smart Routing** – Decision-making model to interpret and delegate tasks.

---

## 💪 Built With

Here are the key technologies and libraries that power this assistant:

### 🔹 Core Technologies

* **Python 3.x**
* **Asyncio** – Asynchronous programming
* **CustomTkinter** – Modern GUI framework

### 🎙️ Voice & Audio

* **SpeechRecognition** – Convert speech to text
* **pyttsx3** – Text to speech
* **edge-tts** – Neural voice TTS
* **pygame** – Audio playback

### 🖼️ Image & GUI Handling

* **Pillow (PIL)** – Image processing
* **opencv-python** – Computer vision
* **PyQt5** – Additional GUI support

### 🌐 Web & Automation

* **selenium**, **webdriver-manager** – Browser automation
* **googlesearch-python** – Google search integration
* **requests**, **bs4**, **rich** – Web scraping & formatting
* **pywhatkit**, **AppOpener**, **keyboard** – Local automation

### 🤖 AI & Language

* **cohere**, **groq**, **mtranslate** – AI APIs and translation
* **python-dotenv** – Environment configuration

---

## 🏁 Getting Started

### 🔧 Prerequisites

* Python 3.10 or above
  Check installation:

  ```bash
  python --version
  ```

### 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/RiturajS12/AI_Assistant.git
   cd AI_Assistant
   ```

2. **Create & activate a virtual environment**

   **Windows:**

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

   **macOS/Linux:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**

   Create a `.env` file in the root directory:

   ```env
   CohereAPIKey=your_cohere_key
   Username=Your Name
   Assistantname=Assistant Bot
   GroqAPIKey=your_groq_key
   InputLanguage=en
   AssistanceVoice=en-US-EricNeural
   HuggingFaceAPIKey=your_huggingface_key
   ```

---

## 🎈 Usage

Once set up, run the application:

```bash
python Main.py
```

The assistant's GUI will launch. You can now speak commands, chat, and explore all features interactively!

---

## 📁 Project Structure

```
AI-ASSISTANT/
├── Backend/              # Core processing and logic
├── Data/                 # Data and resources
├── Frontend/             # GUI components
│   ├── GUI.py
│   └── Graphics/         # Logos and images
├── Main.py               # Entry point
├── requirements.txt      # Dependencies
└── .env.example          # Sample environment config
```

---

## 🤝 Contributing

Contributions are what make the open-source community so great! 🙌
If you have ideas or improvements:

1. **Fork the repository**
2. **Create your feature branch**
   `git checkout -b feature/AmazingFeature`
3. **Commit your changes**
   `git commit -m 'Add some AmazingFeature'`
4. **Push to the branch**
   `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

---

## 📭 Contact

**Rituraj Singh**
GitHub: [@RiturajS12](https://github.com/RiturajS12)
Project Link: [AI Assistant Repository](https://github.com/RiturajS12/AI_Assistant)

---
