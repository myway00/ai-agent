import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI
from backend.prompts import SELF_INTRO_FEEDBACK_PROMPT
from backend.rag import load_vector_db

load_dotenv()

def classify_user_request(user_text: str) -> str:
    """Agent 1: 사용자 입력 분석, 요청 분류"""
    llm = AzureChatOpenAI(
        deployment_name=os.getenv("AOAI_DEPLOY_GPT4O"),
        api_key=os.getenv("AOAI_API_KEY"),
        azure_endpoint=os.getenv("AOAI_ENDPOINT"),
        api_version=os.getenv("AOAI_API_VERSION"),
        temperature=0
    )
    prompt = f"사용자 입력을 분석해서 간단한 카테고리를 한 단어로 알려주세요:\n\n{user_text}"
    category = llm.predict(prompt)
    return category.strip()

def retrieve_relevant_docs(user_text: str):
    """Agent 2: RAG 검색 에이전트"""
    db = load_vector_db()
    docs = db.similarity_search(user_text, k=3)
    return docs

def generate_feedback(user_text: str, context_docs) -> str:
    """Agent 3: 최종 피드백 생성 에이전트"""
    context = "\n".join([doc.page_content for doc in context_docs])

    prompt_template = PromptTemplate(
        input_variables=["user_input"],
        template=SELF_INTRO_FEEDBACK_PROMPT
    )

    llm = AzureChatOpenAI(
        deployment_name=os.getenv("AOAI_DEPLOY_GPT4O"),
        api_key=os.getenv("AOAI_API_KEY"),
        azure_endpoint=os.getenv("AOAI_ENDPOINT"),
        api_version=os.getenv("AOAI_API_VERSION"),
        temperature=0.7
    )

    prompt = prompt_template.format(user_input=user_text + "\n\n참고자료:\n" + context)
    response = llm.predict(prompt)
    return response

def multi_agent_pipeline(user_text: str) -> str:
    """최종 Multi-Agent 파이프라인 함수"""
    # 1. 분류
    category = classify_user_request(user_text)

    # (필요 시 카테고리별 분기 가능, 현재는 단순 무시)
    print(f"[Agent 1] 분류 결과: {category}")

    # 2. RAG 검색
    docs = retrieve_relevant_docs(user_text)

    # 3. 피드백 생성
    feedback = generate_feedback(user_text, docs)

    return feedback
