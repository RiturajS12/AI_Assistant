# --- Imports ---
from Frontend.GUI import (
    GraphicalUserInterface,
    SetAssistantStatus,
    ShowTextToScreen,
    TempDirectoryPath,
    SetMicrophoneStatus,
    AnswerModifier,
    QueryModifier,
    GetMicrophoneStatus,
    GetAssistantStatus
)
from Backend.Model import FirstLayerDMM
from Backend.RealtimeSearchEngine import RealtimeSearchEngine
from Backend.Automation import Automation, SendWhatsappMessage
from Backend.SpeechToText import SpeechRecognition
from Backend.Chatbot import ChatBot
from Backend.TextToSpeech import TextToSpeech
from dotenv import dotenv_values
from asyncio import run
from time import sleep
import subprocess
import threading
import importlib.util
import json
import sys
import os


def check_and_install_dependencies():
    """
    Checks if required packages are installed and installs them if they are not.
    This is useful for ensuring the environment is set up correctly.
    """
    print("Checking for required packages...")
    package_name = 'opencv-python'
    spec = importlib.util.find_spec('cv2')
    if spec is None:
        print(f"'{package_name}' not found. Installing...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            print(f"'{package_name}' installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing '{package_name}': {e}")
            print("Please install it manually using: pip install opencv-python")
            sys.exit(1)
    else:
        print(f"'{package_name}' is already installed.")


env_vars = dotenv_values('.env')
Username = env_vars.get('Username', 'User')
Assistantname = env_vars.get("Assistantname", 'Assistant')
DefaultMessage = f'''{Username} : Hello {Assistantname}, How are you?
{Assistantname} : Welcome {Username}. I am doing well. How may I help you?'''

automation_functions = ['open', 'close', 'play', 'system', 'content', 'google search', 'Youtube']


def ShowDefaultChatIfNoChats():
    """If the chat log is empty, display a default welcome message."""
    try:
        with open(r'Data\Chatlog.json', 'r', encoding='utf-8') as f:
            if len(f.read()) < 5:
                ShowTextToScreen(DefaultMessage)
    except FileNotFoundError:
        with open(r'Data\Chatlog.json', 'w', encoding='utf-8') as f:
            json.dump([], f)
        ShowTextToScreen(DefaultMessage)

def ChatLogIntegration():
    """Reads the JSON chat log and formats it for display on the GUI."""
    try:
        with open(r'Data\Chatlog.json', 'r', encoding='utf-8') as file:
            chatlog_data = json.load(file)
        
        formatted_chatlog = ""
        for entry in chatlog_data:
            role = entry.get('role', '')
            content = entry.get('content', '')
            if role == "user":
                formatted_chatlog += f"{Username} : {content}\n"
            elif role == 'assistant':
                formatted_chatlog += f"{Assistantname} : {content}\n"
        
        if formatted_chatlog:
            ShowTextToScreen(AnswerModifier(formatted_chatlog))

    except Exception as e:
        print(f"Error reading or processing chat log: {e}")
        ShowDefaultChatIfNoChats()

def InitialExecution():
    """Sets up the initial state of the application on startup."""
    print("Initializing application...")
    SetMicrophoneStatus("False")
    ShowTextToScreen("")
    ChatLogIntegration()
    print("Initialization complete.")


def MainExecution():
    """The core operational loop that processes one full user command."""
    
    SetAssistantStatus("Listening......")
    Query = SpeechRecognition()
    if not Query:
        print("No query received.")
        return

    ShowTextToScreen(f'{Username} : {Query}')
    SetAssistantStatus("Thinking......")
    
    Decision = FirstLayerDMM(Query)
    print(f'Decision : {Decision}')


    for query in Decision:
        if "whatsapp" in query:
            SetAssistantStatus("Sending Message...")
            try:
                parts = query.split(" message ")
                recipient = parts[0].replace("whatsapp", "").strip()
                message = parts[1].strip()
                response = SendWhatsappMessage(recipient, message)
                ShowTextToScreen(f"{Assistantname} : {response}")
                SetAssistantStatus("Answering......")
                TextToSpeech(response)
            except Exception as e:
                print(f"Error processing whatsapp command: {e}")
                error_msg = "I couldn't understand that. Please try again like: 'whatsapp steve message hello'."
                ShowTextToScreen(f"{Assistantname} : {error_msg}")
                TextToSpeech(error_msg)
            return 

    automation_tasks = [cmd for cmd in Decision if any(cmd.startswith(func) for func in automation_functions)]
    if automation_tasks:
        SetAssistantStatus("Performing task...")
        run(Automation(automation_tasks))

    for query in Decision:
        if "generate image" in query:
            with open(r'Frontend\Files\ImageGeneration.data', 'w') as file:
                file.write(f"{query},True")
            try:
                subprocess.Popen([sys.executable, r'Backend\ImageGeneration.py'])
            except Exception as e:
                print(f'Error starting ImageGeneration.py: {e}')

    general_query = " ".join([q.replace("general", "").strip() for q in Decision if q.startswith("general")])
    realtime_query = " ".join([q.replace("realtime", "").strip() for q in Decision if q.startswith("realtime")])

    if realtime_query:
        SetAssistantStatus("Searching......")
        Answer = RealtimeSearchEngine(QueryModifier(realtime_query))
        ShowTextToScreen(f"{Assistantname} : {Answer}")
        SetAssistantStatus("Answering......")
        TextToSpeech(Answer)
    elif general_query:
        SetAssistantStatus("Thinking......")
        Answer = ChatBot(QueryModifier(general_query))
        ShowTextToScreen(f"{Assistantname} : {Answer}")
        SetAssistantStatus("Answering......")
        TextToSpeech(Answer)

    if "exit" in Decision:
        response = "Goodbye, have a great day!"
        ShowTextToScreen(f"{Assistantname} : {response}")
        TextToSpeech(response)
        sleep(2)
        sys.exit()


def Backend_Thread():
    """Thread for running the backend logic loop."""
    InitialExecution()
    while True:
        if GetMicrophoneStatus() == "True":
            MainExecution()
            SetMicrophoneStatus("False") 
        else:
            SetAssistantStatus("Available......")
            sleep(0.2)

def Frontend_Thread():
    """Thread for running the GUI."""
    GraphicalUserInterface()

if __name__ == "__main__":
    check_and_install_dependencies()

    backend_task = threading.Thread(target=Backend_Thread, daemon=True)
    backend_task.start()

    Frontend_Thread()