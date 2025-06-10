# from webscout import PhindSearch as brain
# from rich import print
# from webscout.AIutel import RawDog

# rawdog = RawDog()
# intro_prompt = rawdog.intro_prompt

# ai = brain(
#     is_conversation=True,
#     max_tokens=800,
#     timeout=30,
#     intro=intro_prompt,
#     filepath=r"D:\Jarvis\AI Jarvis\chat_history.txt",
#     update_file=True,
#     proxies={},
#     history_offset=10250,
#     act=None,

# )



# def Main_Brain(text):
#     response = ai.chat(text)
#     rawdog_feedback = rawdog.main(response)
#     if rawdog_feedback:
#         ai.chat(rawdog_feedback)
#     return response



from webscout import LLAMA3 as brain
from rich import print
import os

history_file = r"D:\Jarvis\AI Jarvis\chat_history.txt"

def load_history():
    if os.path.exists(history_file):
        with open(history_file, 'r') as file:
            return file.read()
        return ""
    
def save_history(history):
    with open(history_file, 'w') as file:
        file.write(history)

conversation_history = load_history()

ai = brain(
    is_conversation=True,
    max_tokens=800,
    timeout=30,
    intro=None,
    filepath=None,
    update_file=False,
    proxies={},
    history_offset=10250,
    act=None,
    model="llama3-8b",
    system="You are a Helpful AI"

)

def Main_Brain(text):
    conversation_history = load_history()

    conversation_history += f"\nUser: {text}"

    full_prompt = conversation_history + "\nAI:"

    response_chunks = []
    for chunk in ai.chat(full_prompt):
        response_chunks.append(chunk)
        print(chunk, end="", flush=True)

    response_text = "".join(response_chunks)

    conversation_history += f"\nAI: {response_text}"

    if "remember this" in text.lower():
        save_history(conversation_history)

    return response_text
