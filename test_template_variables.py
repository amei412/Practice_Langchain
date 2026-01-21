from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

# 1. 환경 설정
load_dotenv()

# 2. 모델(뇌) 준비
llm = ChatOpenAI(model=os.getenv("MODEL_NAME"), temperature=0.2)

# 3. 템플릿(틀) 만들기
# 나중에 바뀔 부분만 {중괄호}로 구멍을 뚫어줍니다.
prompt = PromptTemplate.from_template(
    "주제: {topic}\n"
    "형식: {style}\n"
    "요청: 한국어 3행시로 만들어줘"
)

# 4. 체인(파이프라인) 조립
# [재료 들어옴] -> [프롬프트 틀에 채움] -> [AI가 생각함] -> [글자로 다듬음] -> [결과]
chain = prompt | llm | StrOutputParser()

# 5. 실행 및 출력 (재료 투입!)
# 틀에 뚫어놓은 구멍 이름(key)과 넣을 내용(value)을 짝지어 줍니다.
result = chain.invoke({"topic": "AI", "style": "블랙코미디"})

print(result)