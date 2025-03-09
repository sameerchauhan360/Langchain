from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

messages = [
    SystemMessage(content="Solve the followin math problem"),
    HumanMessage(content="what is the square root of 49?"),
]


# ------------ Anthropic Chat Model ----------------
model = ChatAnthropic(model="claude-2.1")

result = model.invoke(messages)
print(result.content)

# -------------- Google Chat Model -----------------
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

result = model.invoke(messages)
print(result.content)
