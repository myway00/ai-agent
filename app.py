import streamlit as st
from backend.agent import get_self_intro_feedback
from backend.rag import build_vector_db

st.set_page_config(page_title="AI 자기소개서 코치", layout="wide")
st.title("🤖  코코치")

uploaded_file = st.file_uploader("📄 자기소개서 텍스트 파일 업로드 (.txt)", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    st.text_area("업로드된 자기소개서 내용", value=text, height=300)

    if st.button("분석하기"):
        if text.strip():
            with st.spinner("AI 분석 중..."):
                # 벡터 DB 생성
                build_vector_db(text)
                feedback = get_self_intro_feedback(text)

            st.subheader("📌 분석 결과")
            st.write(feedback)
        else:
            st.warning("자기소개서 내용이 비어있습니다.")
else:
    st.info("파일을 업로드해 주세요.")
