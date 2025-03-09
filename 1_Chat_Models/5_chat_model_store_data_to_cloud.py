from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory
from dotenv import load_dotenv

load_dotenv()

# Setup the firebase firestor
PROJECT_ID = "langchain-e9b8f"
SESSION_ID = "user_session_new"
COLLECTION_NAME = "chat_history"

# Initialize Firestore Client
print("Initializing the Firestore Client...")
client = firestore.Client(project=PROJECT_ID)

# Initialize Firestore Chat Message History
print("Initializing Firestore Chat Message History")
chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client
)

print("chat history initialized")
print(f"Current Chat History: {chat_history.messages}")


model = ChatOpenAI(model="gpt-4o-mini")

while True:

    query = input("You: ")

    if query.lower() == "exit":
        break

    chat_history.add_user_message(query)
    results = model.invoke(chat_history.messages)
    response = results.content

    chat_history.add_ai_message(response)
    print(f"Assistant: {response}")