import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI
from backend.prompts import SELF_INTRO_FEEDBACK_PROMPT
from backend.rag import load_vector_db

load_dotenv()

def get_self_intro_feedback(user_text):
    # RAG에서 관련 자료 검색
    db = load_vector_db()
    docs = db.similarity_search(user_text, k=2)
    context = "\n".join([doc.page_content for doc in docs])

    # 프롬프트 구성
    prompt_template = PromptTemplate(
        input_variables=["user_input"],
        template=SELF_INTRO_FEEDBACK_PROMPT
    )

    # Azure Chat 모델 사용 (api_version 반영)
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
