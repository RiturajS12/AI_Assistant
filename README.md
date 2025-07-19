<div align="center">
<img src="https://raw.githubusercontent.com/RiturajS12/AI-Assistant/main/Frontend/Graphics/logo.png" alt="Logo" width="120">
<h1 align="center">🤖 AI Assistant 🤖</h1>
<p align="center">
A versatile desktop AI assistant with a graphical user interface, featuring real-time conversation, speech synthesis, web search, image generation, and automation capabilities.
<br />
<a href="#-key-features"><strong>Explore the features »</strong></a>
<br />
<br />
<a href="https://github.com/RiturajS12/AI-Assistant/issues">Report Bug</a>
·
<a href="https://github.com/RiturajS12/AI-Assistant/issues">Request Feature</a>
</p>
</div>

<!-- Table of Contents -->

<details>
<summary>Table of Contents</summary>
<ol>
<li>
<a href="#-about-the-project">About The Project</a>
<ul>
<li><a href="#-built-with">Built With</a></li>
</ul>
</li>
<li>
<a href="#-getting-started">Getting Started</a>
<ul>
<li><a href="#prerequisites">Prerequisites</a></li>
<li><a href="#installation">Installation</a></li>
</ul>
</li>
<li><a href="#-usage">Usage</a></li>
<li><a href="#-project-structure">Project Structure</a></li>
<li><a href="#-contributing">Contributing</a></li>
<li><a href="#-license">License</a></li>
<li><a href="#-contact">Contact</a></li>
</ol>
</details>

✨ About The Project
(Pro-tip: Replace this link with a GIF showing your app in action! It's a great way to showcase your work.)

This project is a sophisticated AI Assistant built in Python by RiturajS12. It provides a seamless interactive experience through a dedicated graphical user interface (GUI). The assistant is designed to be a multi-purpose tool, capable of understanding voice commands, responding with a synthesized voice, performing real-time searches, generating images based on prompts, and even automating tasks.

At its core, it uses a custom decision-making model to interpret user queries and route them to the appropriate module, whether it's the chatbot, the image generator, or the web search engine.

🚀 Key Features
🗣️ Voice Interaction: Real-time speech-to-text and text-to-speech for hands-free operation.

💬 Conversational AI: An integrated chatbot for natural, human-like conversations.

🌐 Real-time Web Search: Fetches up-to-date information from the internet to answer your questions.

🎨 AI Image Generation: Creates unique images from your text descriptions.

🤖 Task Automation: Capable of performing automated tasks.

🖥️ Graphical User Interface: A clean and intuitive GUI for easy interaction and visual feedback.

🧠 Smart Decision Making: A multi-layered model to understand intent and delegate tasks effectively.

🛠️ Built With
This project leverages the power of modern Python libraries and frameworks.

Python 3.x

Asyncio

CustomTkinter (for the GUI)

SpeechRecognition

pyttsx3

Pillow (PIL)

(Add other key libraries here)

🏁 Getting Started
Follow these instructions to get a copy of the project up and running on your local machine.

Prerequisites
You need to have Python and pip installed on your system.

Python 3.8+

python --version

Installation
Clone the repository

git clone https://github.com/RiturajS12/AI-Assistant.git
cd AI-Assistant

Create and activate a virtual environment

On Windows:

python -m venv venv
.\venv\Scripts\activate

On macOS/Linux:

python3 -m venv venv
source venv/bin/activate

Install the required packages

pip install -r requirements.txt

Set up environment variables

Create a file named .env in the root directory.

Add the necessary API keys and configuration variables to this file. For example:

OPENAI_API_KEY="your_api_key_here"
ANOTHER_SERVICE_API_KEY="your_other_key"

🎈 Usage
Once the installation is complete, you can run the AI Assistant from the root directory:

python Main.py

This will launch the GUI. From there, you can interact with the assistant.

📁 Project Structure
The project is organized into the following structure:

AI-ASSISTANT/
├── Backend/
├── Data/
├── Frontend/
│   ├── GUI.py
│   └── Graphics/
├── Main.py
└── requirements.txt

🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📜 License
Distributed under the MIT License. See LICENSE file for more information.

📧 Contact
RiturajS12 - @RiturajS12

Project Link: https://github.com/RiturajS12/AI-Assistant
