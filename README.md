
# AI 업무 문서 코치 (AI Document Coach)

## 프로젝트 개요  
본 프로젝트는 사용자가 업로드한 업무 문서 텍스트를 AI가 분석하고 맞춤형 피드백을 제공하는 AI 기반 코칭 서비스입니다.  
LangChain과 Azure OpenAI API를 활용한 RAG (Retrieval-Augmented Generation) 및 멀티 에이전트 구조를 적용하여 실무에서 활용 가능한 완결형 AI Agent를 구현했습니다.

---

## 주요 기능  
- **텍스트 파일 업로드**: 업무 문서 텍스트(.txt) 파일 업로드 지원  
- **벡터 데이터베이스 생성**: 입력 텍스트를 분할하고 임베딩하여 FAISS 기반 벡터 DB 구축  
- **유사 문서 검색**: 벡터 DB에서 유사 자기소개서 문서 검색  
- **RAG 기반 피드백 생성**: 검색된 문서를 참고하여 AI가 논리적이고 상세한 피드백 제공  
- **멀티 에이전트 구조**: 입력 분석, 검색, 생성 각 역할별 에이전트를 구성하여 협업 처리  
- **Streamlit UI**: 직관적이고 간편한 웹 UI를 통해 파일 업로드 및 분석 결과 확인 가능

---

## 기술 스택  
- Python 3.13  
- Streamlit (웹 UI)  
- LangChain (멀티 에이전트, 프롬프트 엔지니어링)  
- Azure OpenAI (GPT-4o, 임베딩)  
- FAISS (벡터 데이터베이스)  
- dotenv (환경 변수 관리)

---

## 환경 변수 설정 (.env)  
```env
LANG=ko_KR.UTF-8
AOAI_ENDPOINT=https://skcc-atl-dev-openai-01.openai.azure.com/
AOAI_API_KEY=YOUR_API_KEY_HERE
AOAI_DEPLOY_GPT4O_MINI=gpt-4o-mini
AOAI_DEPLOY_GPT4O=gpt-4o
AOAI_DEPLOY_EMBED_3_LARGE=text-embedding-3-large
AOAI_DEPLOY_EMBED_3_SMALL=text-embedding-3-small
AOAI_DEPLOY_EMBED_ADA=text-embedding-ada-002
AOAI_API_VERSION=2023-07-01-preview
````

---

## 실행 방법

1. 필수 라이브러리 설치

```bash
pip install -r requirements.txt
```

2. `.env` 파일에 Azure OpenAI 관련 환경 변수 설정

3. Streamlit 앱 실행

```bash
streamlit run app.py
```

4. 웹 브라우저에서 `http://localhost:8501` 접속 후, 자기소개서 텍스트 파일 업로드 및 분석

---

## 프로젝트 구조

```
├── app.py                 # Streamlit 웹 앱 메인
├── backend
│   ├── agent.py           # AI 피드백 생성 및 멀티 에이전트 로직
│   ├── rag.py             # RAG 관련 벡터 DB 생성 및 검색 모듈
│   └── prompts.py         # 프롬프트 템플릿 정의
├── data
│   └── embeddings_faiss   # 생성된 벡터 DB 저장 폴더
├── .env                   # 환경 변수 파일 (API 키 등)
├── requirements.txt       # 의존성 목록
└── README.md              # 프로젝트 설명 파일
```

---
