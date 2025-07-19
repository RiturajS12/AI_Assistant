# --- Imports ---
from AppOpener import close, open as appopen
from webbrowser import open as webopen
from pywhatkit import search, playonyt
from dotenv import dotenv_values
from bs4 import BeautifulSoup
from rich import print
from groq import Groq
import webbrowser
import subprocess
import requests
import pyautogui
import keyboard
import asyncio
import time
import json
import os
import sys
import importlib.util

# --- Dependency Management ---

def check_and_install_opencv():
    """
    Checks if 'opencv-python' is installed (as 'cv2') and installs it if not.
    This is required for pyautogui's 'confidence' feature.
    """
    package_name = 'opencv-python'
    module_name = 'cv2'
    spec = importlib.util.find_spec(module_name)
    if spec is None:
        print(f"'{package_name}' not found. It is required for UI automation confidence levels.")
        print("Attempting to install it now...")
        try:
            # Use sys.executable to ensure pip installs for the correct Python environment
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            print(f"'{package_name}' installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"ERROR: Failed to install '{package_name}'.")
            print(f"Please install it manually by running: pip install {package_name}")
            print(f"Error details: {e}")
            # Depending on how critical this is, you might want to exit.
            # For now, we'll just print a warning and continue.
        except FileNotFoundError:
            print("ERROR: 'pip' command not found. Is Python installed correctly and in your PATH?")

# Run the check when the module is loaded
check_and_install_opencv()


# --- Configuration ---
env_vars = dotenv_values(".env")
GroqAPIKey = env_vars.get("GroqAPIKey")

Classes = ["ZCbuwd", "h9Ke3f", "L1tq0e SY7ric", "ZCLcJf", "gsrt vk_bk FzvWSb VbwPnf", "pclqee", "tw-Data-text tw-text-small tw-ta", "l7dC6cf", "OsUR6d LTK00c", "vLY2gd", "webanswers-webanswers_table__webanswers_table", "dDoNo ikb4Bb gsrt", "sXLa0e", "LWfK9c", "V0F4g", "qv3Wpe", "kno-rdesc", "SPZz6b"]
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"

client = Groq(api_key=GroqAPIKey)
messages = []
SystemChatBot = [{"role": "system", "content": f"Hello, I am {os.environ.get('Username', 'User')}, You're a content writer. You have to write content like letters,codes,applications,essays,notes,songs,poems etc."}]

# --- Core Automation Functions ---

def GoogleSearch(Topic):
    search(Topic)
    return True

def Content(Topic):
    def OpenNotepad(File):
        default_text_editor = 'notepad.exe'
        subprocess.Popen([default_text_editor, File])

    def ContentWriterAI(prompt):
        messages.append({"role": "user", "content": f"{prompt}"})
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=SystemChatBot + messages,
            max_tokens=2048,
            temperature=0.7,
            top_p=1,
            stream=True,
            stop=None
        )
        Answer = ""
        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content
        Answer = Answer.replace("</s>", "")
        messages.append({"role": "assistant", "content": Answer})
        return Answer

    Topic: str = Topic.replace("Content ", "")
    ContentByAI = ContentWriterAI(Topic)
    file_path = os.path.join("Data", f"{Topic.lower().replace(' ', '')}.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(ContentByAI)
    OpenNotepad(file_path)
    return True

def YouTubeSearch(Topic):
    Url4Search = f"https://www.youtube.com/results?search_query={Topic}"
    webbrowser.open(Url4Search)
    return True

def PlayYoutube(query):
    playonyt(query)
    return True

def OpenApp(app, extra_command=None, sess=requests.session()):
    try:
        appopen(app, match_closest=True, output=True, throw_error=True)
        print(f"Opened app: {app}")
    except Exception as e:
        print(f"Couldn’t open app directly: {e}")
        def extract_links(html):
            if html is None: return []
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.find_all('a', {'jsname': 'UWckNb'})
            return [link.get('href') for link in links]

        def search_google(query):
            url = f"https://www.google.com/search?q={query}"
            headers = {"User-Agent": useragent}
            response = sess.get(url, headers=headers)
            if response.status_code == 200:
                return response.text
            else:
                print("Failed to retrieve search results.")
                return None
        html = search_google(app)
        if html:
            links = extract_links(html)
            if links:
                webopen(links[0])
                print(f"Opened fallback link: {links[0]}")
            else:
                print("No link found in search results.")
    return True

def CloseApp(app):
    if "chrome" in app.lower():
        pyautogui.hotkey('alt', 'f4')
    else:
        try:
            close(app, match_closest=True, output=True, throw_error=True)
        except Exception as e:
            print(f"Could not close app {app}: {e}")
            return False
    return True

def System(command):
    command_map = {
        "mute": "volume mute",
        "unmute": "volume mute",
        "volume up": "volume up",
        "volume down": "volume down",
    }
    action = command_map.get(command)
    if action:
        keyboard.press_and_release(action)
    return True

def SendWhatsappMessage(recipient_name: str, message: str):
    """Finds a contact in WhatsApp Web by name and sends them a message using UI automation."""
    try:
        # --- Define paths to the image assets ---
        graphics_path = os.path.join(os.getcwd(), "Frontend", "Graphics")
        search_icon_path = os.path.join(graphics_path, "whatsapp_search.png")
        textbox_icon_path = os.path.join(graphics_path, "whatsapp_textbox.png")

        # --- Open WhatsApp Web and wait for it to load ---
        webbrowser.open('https://web.whatsapp.com')
        time.sleep(15)  # Wait time for WhatsApp Web to load completely

        # --- Find and click the search bar ---
        search_bar_pos = pyautogui.locateCenterOnScreen(search_icon_path, confidence=0.8)
        if not search_bar_pos:
            return "Could not find the WhatsApp search bar on the screen. Make sure WhatsApp Web is open and visible."
        
        pyautogui.click(search_bar_pos)
        time.sleep(1)
        
        # --- Type the recipient's name and press enter ---
        pyautogui.write(recipient_name, interval=0.1)
        time.sleep(2) # Wait for search results
        pyautogui.press('enter')
        time.sleep(2) # Wait for chat to open

        # --- Find and click the message text box ---
        text_box_pos = pyautogui.locateCenterOnScreen(textbox_icon_path, confidence=0.8)
        if not text_box_pos:
            return "Could not find the message text box. The chat may not have opened correctly."
        
        pyautogui.click(text_box_pos)
        time.sleep(1)

        # --- Type the message and send it ---
        pyautogui.write(message, interval=0.1)
        pyautogui.press('enter')
        time.sleep(2)

        # --- Close the WhatsApp tab ---
        pyautogui.hotkey('ctrl', 'w')
        
        return f"Message sent to {recipient_name}."

    except Exception as e:
        print(f"Error in SendWhatsappMessage: {e}")
        return "Sorry, I encountered an error trying to send the message through the user interface."

# --- Asynchronous Task Execution ---
async def TranslateAndExecute(commands: list[str]):
    funcs = []
    for command in commands:
        if command.startswith("open "): funcs.append(asyncio.to_thread(OpenApp, command.removeprefix("open ")))
        elif command.startswith("close "): funcs.append(asyncio.to_thread(CloseApp, command.removeprefix("close ")))
        elif command.startswith("play "): funcs.append(asyncio.to_thread(PlayYoutube, command.removeprefix("play ")))
        elif command.startswith("content "): funcs.append(asyncio.to_thread(Content, command.removeprefix("content ")))
        elif command.startswith("google search "): funcs.append(asyncio.to_thread(GoogleSearch, command.removeprefix("google search ")))
        elif command.startswith("Youtube "): funcs.append(asyncio.to_thread(YouTubeSearch, command.removeprefix("Youtube ")))
        elif command.startswith("system "): funcs.append(asyncio.to_thread(System, command.removeprefix("system ")))
        # Note: 'whatsapp' is handled directly in main.py, not here.
        else: print(f"No automation function found for: {command}")

    await asyncio.gather(*funcs)

async def Automation(commands: list[str]):
    await TranslateAndExecute(commands)
    return True