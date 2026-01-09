# RAG 기반 AI 문서 QA 서비스

LLM(대형 언어 모델)에 외부 문서를 결합하여 실제 근거를 바탕으로 답변하는 AI 질의응답 시스템을 구현하는 프로젝트입니다.
이 프로젝트는 Retrieval-Augmented Generation(RAG) 구조를 직접 설계하고 구현하는 것을 목표로 합니다.

---
## 1. 프로젝트 목표

LLM의 한계(환각, 최신 정보 부족)를 RAG 구조로 해결

벡터 검색 기반 문서 검색 시스템 구축

실제 서비스 형태의 API 서버로 구현

포트폴리오 수준의 구조, 문서화, 코드 품질 확보

= 전체 시스템 구조 (Day 1) =

	[사용자 질문]
		↓
	PromptTemplate (프롬프트 규칙)
		↓
	LLM (GPT 계열 모델)
		↓
	답변 출력

Day2 이후 구조에 문서 임베딩 / 벡터DB / 검색기(Retriever) 가 추가될 예정입니다.

---

## 2. 기술 스택

언어: Python 3.10

LLM 프레임워크: LangChain

LLM API: OpenAI API

환경관리: venv, python-dotenv

버전관리: Git

(이후: FAISS/Chroma, FastAPI, Docker, Cloud 배포 예정)

---

## 3. Day 1 구현 내용

1. LLM 체인 구축
   
- LangChain의 파이프라인 구조를 이용해 다음과 같은 체인을 구현했습니다.

- [prompt | llm | parser]

- PromptTemplate로 출력 형식과 규칙을 고정

- ChatOpenAI로 LLM 호출

- StrOutputParser로 응답 정제


2. 프롬프트 분리 및 관리

- 프롬프트를 코드에서 분리하여 파일로 관리합니다.

- 이를 통해 프롬프트 버전 관리와 실험이 용이해졌습니다.


3. 대화형 콘솔 인터페이스
   
- 사용자가 질문을 입력하면 LLM이 즉시 응답하는 대화형 구조로 개선했습니다.

---

## 4. 프로젝트 구조

	rag-qa/
	 ├─ src/
	 │	└─ day1_basic_chain.py
	 ├─ prompts/
	 │	└─ qa_v1.txt
	 ├─ .env
	 ├─ .gitignore
	 ├─ requirements.txt
	 └─ README.md

환경설정

	.\.venv\Scripts\activate
	pip install -r requirements.txt

.env 파일 생성

	OPENAI_API_KEY = 내 API키

실행

	python src/day1_basic_chain.py

---

## 5. 향후 계획

Day2 : 문서 임베딩 및 벡터DB 구축

Day3 : RAG 구조 완성

Day4 : FastAPI 서버화

Day5 : 검색 품질 개선 및 평가

Day6 : 포트폴리오 문서 정리

Day7 : 배포 및 시연 자료 제작

---

## 6. 이 프로젝트에서 검증하려는 역량

LLM 파이프라인 설계 능력

벡터 검색 기반 정보 검색 시스템 구축 능력

RAG 구조 이해 및 실무 적용 능력

서비스형 AI 시스템 설계 경험
