from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

messages = [
    SystemMessage("You are an expert in social media content strategy"),
    HumanMessage("Give me a short tip to create engaging posts on Instagram"),
]

result = llm.invoke(messages)

print(result.content)