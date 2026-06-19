import speech_recognition as sr
import pyttsx3
from datetime import datetime



# Speak Function
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# Save Conversation
def save_log(user, bot):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("conversation_log.txt", "a", encoding="utf-8") as file:
        file.write(f"\n[{timestamp}]\n")
        file.write(f"User: {user}\n")
        file.write(f"Bot: {bot}\n")

# Voice Input
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=15
            )

    try:
        text = recognizer.recognize_google(audio)
        return text

    except:
        return "Sorry, I could not understand."

# Chatbot Logic
def get_response(text):

    text = text.lower()

    if "hello" in text:
        return "Hello! How can I help you?"

    elif "time" in text:
        return f"The current time is {datetime.now().strftime('%H:%M')}"

    elif "calculate" in text:
        try:
            expression = text.replace("calculate", "")
            result = eval(expression)
            return f"The answer is {result}"
        except:
            return "Invalid calculation"

    elif "date" in text:
        return datetime.now().strftime("%d-%m-%Y")

    elif "your name" in text:
        return "I am Jarvis."

    else:
        return f"You said: {text}"

# Main Loop
while True:

    print("\n===== JARVIS =====")
    print("1. Text Input")
    print("2. Voice Input")
    print("Type 'bye' to exit.")

    choice = input("Choose option: ")

    if choice == "1":
        user_input = input("You: ")

    elif choice == "2":
        user_input = listen()
        print("You:", user_input)

    elif choice.lower() == "bye":
        print("Jarvis: Goodbye.")
        speak("Goodbye.")
        break
    else:
        print("Invalid option")
        continue

    response = get_response(user_input)

    print("Jarvis:", response)

    speak(response)

    save_log(user_input, response)

    if "bye" in user_input.lower():
        break