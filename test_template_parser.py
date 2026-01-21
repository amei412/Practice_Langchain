from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

llm = ChatOpenAI(model = os.getenv("MODEL_NAME"), temperature = 0.2)

prompt = PromptTemplate.from_template(
    "AI를 주제로한 5줄 논평을 작성하세요."
)

chain = prompt | llm | StrOutputParser()

result = chain.invoke({})
print(result)