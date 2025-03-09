from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model = 'gpt-4o-mini')

result = llm.invoke('What is root of 49')

print(result.co
      ntent)


