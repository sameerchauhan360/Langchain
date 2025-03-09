from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

chat_history = []

system_message = SystemMessage(content="You are a helpful AI Assistant")
chat_history.append(system_message)

while True:

    query = input("You: ")

    if query.lower() == "exit":
        break

    chat_history.append(HumanMessage(content=query))

    result = model.invoke(chat_history)
    response = result.content

    chat_history.append(AIMessage(content=response))

    print(f"AI: {response}")

print("----History Message----")
print(chat_history)