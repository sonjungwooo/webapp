import streamlit as st
st.title('손정우')
st.write('qwerfijnfqewbkjl')

# MBTI별 추천 직업 및 전공 데이터
mbti_data = {
    "ISTJ": {
        "jobs": ["회계사", "데이터 분석가", "군인"],
        "majors": ["경영학과", "통계학과", "군사학과"]
    },
    "ISFJ": {
        "jobs": ["간호사", "사회복지사", "교사"],
        "majors": ["간호학과", "사회복지학과", "교육학과"]
    },
    "INFJ": {
        "jobs": ["심리상담사", "작가", "인권운동가"],
        "majors": ["심리학과", "문예창작과", "사회학과"]
    },
    "INTJ": {
        "jobs": ["연구원", "데이터 사이언티스트", "전략기획가"],
        "majors": ["공학계열", "컴퓨터공학과", "경영학과"]
    },
    "ISTP": {
        "jobs": ["엔지니어", "기계 설계자", "응급 구조사"],
        "majors": ["기계공학과", "전기전자과", "응급구조학과"]
    },
    "ISFP": {
        "jobs": ["디자이너", "요리사", "플로리스트"],
        "majors": ["디자인학과", "조리학과", "원예학과"]
    },
    "INFP": {
        "jobs": ["작가", "심리치료사", "예술가"],
        "majors": ["문예창작과", "심리학과", "미술학과"]
    },
    "INTP": {
        "jobs": ["AI 개발자", "이론물리학자", "게임 개발자"],
        "majors": ["컴퓨터공학과", "물리학과", "소프트웨어학과"]
    },
    "ESTP": {
        "jobs": ["소방관", "기업 영업", "운동선수"],
        "majors": ["소방행정학과", "경영학과", "체육학과"]
    },
    "ESFP": {
        "jobs": ["연예인", "이벤트 기획자", "뷰티 스타일리스트"],
        "majors": ["연극영화과", "문화콘텐츠학과", "미용학과"]
    },
    "ENFP": {
        "jobs": ["광고기획자", "작가", "기획자"],
        "majors": ["광고홍보학과", "문예창작과", "문화기획학과"]
    },
    "ENTP": {
        "jobs": ["창업가", "변호사", "기술 컨설턴트"],
        "majors": ["경영학과", "법학과", "공학계열"]
    },
    "ESTJ": {
        "jobs": ["경찰관", "공무원", "프로젝트 매니저"],
        "majors": ["행정학과", "법학과", "경영학과"]
    },
    "ESFJ": {
        "jobs": ["초등교사", "간호사", "HR 담당자"],
        "majors": ["교육학과", "간호학과", "심리학과"]
    },
    "ENFJ": {
        "jobs": ["상담교사", "정치가", "사회운동가"],
        "majors": ["교육학과", "정치외교학과", "사회학과"]
    },
    "ENTJ": {
        "jobs": ["CEO", "경영 컨설턴트", "기획 전문가"],
        "majors": ["경영학과", "경제학과", "산업공학과"]
    },
}

# Streamlit 웹앱 UI 구성
st.set_page_config(page_title="MBTI 직업 추천기", layout="centered")
st.title("💼 MBTI 기반 직업 & 전공 추천기")
st.write("당신의 MBTI를 선택하면 적합한 직업과 관련 전공을 추천해드립니다.")

# 사용자 입력
selected_mbti = st.selectbox("👉 MBTI를 선택하세요", list(mbti_data.keys()))

if selected_mbti:
    st.subheader(f"🔍 {selected_mbti} 유형의 추천 직업")
    for job in mbti_data[selected_mbti]["jobs"]:
        st.markdown(f"- {job}")

    st.subheader("🎓 추천 전공 (학과)")
    for major in mbti_data[selected_mbti]["majors"]:
        st.markdown(f"- {major}")
