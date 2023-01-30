from revChatGPT.ChatGPT import Chatbot
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env
token = os.getenv("TOKEN")

chatbot = Chatbot({
  "session_token": token
}, conversation_id=None, parent_id=None) # You can start a custom conversation

response = chatbot.ask("""when i type a sentence you should reply with the percentage of how cringe that sentence is. for example if i type "dabs away in epic style" you could reply with '91%' reply only with the percentage.
my first sentence is 'i love running in the rain'""", conversation_id=None, parent_id=None) # You can specify custom conversation and parent ids. Otherwise it uses the saved conversation (yes. conversations are automatically saved)
parent_id = response['parent_id']
print(response)

while(True):
 
  print("Enter a phrase to see how cringe it is:")
  phrase = input()

  response = chatbot.ask(phrase, conversation_id=None, parent_id=parent_id)

  print(response['message'])
  parent_id = response['parent_id']
# {
#   "message": message,
#   "conversation_id": self.conversation_id,
#   "parent_id": self.parent_id,
# }