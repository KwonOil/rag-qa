"""
Day 1: LangChain 기본 체인 만들기

목표:
- .env에서 OPENAI_API_KEY 로드
- PromptTemplate로 프롬프트 구성
- ChatOpenAI(LLM) 호출
- 체인 실행 결과 출력

실행:
python src/day1_basic_chain.py
"""

import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from pathlib import Path

def main() -> None:
    # 1) .env 로드 (OPENAI_API_KEY를 환경변수로 올림)
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY가 없습니다. 프로젝트 루트의 .env에 OPENAI_API_KEY를 설정하세요."
        )

    # 2) LLM 생성
    # - model 이름은 계정/정책에 따라 사용 가능 모델이 다를 수 있습니다.
    # - 아래 모델이 안 되면 에러 메시지에 나온 사용 가능 모델로 바꾸면 됩니다.
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.2,  # 낮을수록 더 일관된 답변
    )

    # 3) 프롬프트 템플릿 만들기
    # - 여기서부터 "서비스의 말투/규칙"이 결정됩니다.
    prompt_text = Path("prompts/qa_v1.txt").read_text(encoding="utf-8")
    prompt = PromptTemplate.from_template(prompt_text)

    # 4) 출력 파서: LLM 결과를 문자열로 깔끔하게 뽑아줌
    parser = StrOutputParser()

    # 5) 체인 구성 (LangChain의 기본 철학: 작은 블록들을 연결)
    chain = prompt | llm | parser

    # 6) 실행
    while True:
        user_question = input("\n질문을 입력하세요 (종료: exit): ").strip()
        if user_question.lower() == "exit":
            break
        if not user_question:
            print("질문이 비어있습니다.")
            continue

        result = chain.invoke({"question": user_question})

        print("\n===== 답변 =====")
        print(result)


if __name__ == "__main__":
    main()
