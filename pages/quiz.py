import streamlit as st

import streamlit as st

st.markdown("""
<style>
@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #8ec5fc, #e0c3fc, #a1c4fd, #c2e9fb);
    background-size: 300% 300%;
    animation: gradientMove 12s ease infinite;
    color: white;
    transition: all 0.5s ease;
}

[data-testid="stSidebar"] {
    background: linear-gradient(135deg, #8ec5fc, #e0c3fc, #a1c4fd, #c2e9fb);
    background-size: 300% 300%;
    animation: gradientMove 12s ease infinite;
    color: #f8faff;
    transition: all 0.5s ease;
}

.stApp h1 {
    color: #dbeafe;
    text-shadow: 2px 2px 5px #000;
    font-weight: 900;

.stApp h3 {
    color: #ffd166;
    text-shadow: 1px 1px 3px #000;
    font-weight: 800;
}

div.stButton > button {
    background: linear-gradient(90deg, #89f7fe, #66a6ff);
    color: #1b2a4e;
    border-radius: 12px;
    height: 3em;
    width: 10em;
    font-weight: bold;
    border: none;
    box-shadow: 0px 0px 10px rgba(102,166,255,0.5);
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #66a6ff, #89f7fe);
    box-shadow: 0px 0px 20px rgba(137,247,254,0.8);
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)
st.title("태양계 퀴즈")

# 퀴즈 데이터
quiz = [
    {
        "question": "태양계에서 가장 큰 행성은?",
        "options": ["지구", "목성", "화성", "금성"],
        "answer": "목성",
    },
    {
        "question": "해왕성의 불규칙한 위성 이름은?",
        "options": ["나이아드", "탈라사", "미란다", "미마스"],
        "answer": "탈라사",
    },
    {
        "question": "화성의 대표적인 위성은?",
        "options": ["포보스", "달", "가니메데", "이오"],
        "answer": "포보스",
    },
    {
        "question": "목성의 가장 큰 위성은?",
        "options": ["이오", "유로파", "가니메데", "칼리스토"],
        "answer": "가니메데",
    },
        {
        "question": "위성이 없는 행성은?",
        "options": ["수성", "지구", "토성", "천왕성"],
        "answer": "수성",
    },
        {
        "question": "달과 크기가 비슷한 위성은?",
        "options": ["세토보스", "유로파", "이오", "포보스"],
        "answer": "이오",
    },
]

# 점수 저장
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = [False] * len(quiz)

# 문제 표시
for i, q in enumerate(quiz):
    st.subheader(f"문제 {i+1}")
    st.write(f"**{q['question']}**")

    if not st.session_state.answered[i]:
        user_answer = st.radio(
    "정답을 선택하세요:", 
    q["options"], 
    key=f"radio{i}", 
    index=None
)

        if st.button("확인", key=f"btn{i}"):
            st.session_state.answered[i] = True
            if user_answer == q["answer"]:
                st.success("정답!")
                st.session_state.score += 1
            else:
                st.error(f"오답! 정답은 {q['answer']}입니다.")
    else:
        st.info("이미 답했습니다.")

st.write(f"총 점수: {st.session_state.score}/{len(quiz)}")
