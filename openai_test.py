from openai import OpenAI 
from dotenv import load_dotenv
import os 
from langchain_openai import ChatOpenAI

load_dotenv()

# 1) 환경변수 + load_dotenv 혼합방식  
# client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

# response = client.responses.create(
#     model = "gpt-5-nano",
#     input = "대한민국으로 4행시 지어줘",
#     store = True
# )

# print(response.output_text)

# 2) invoke 방식

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
result = llm.invoke("AI를 주제로한 3줄짜리 평론 작성해주세요.")
print(result.content)

