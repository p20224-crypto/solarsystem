import streamlit as st

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
        user_answer = st.radio("정답을 선택하세요:", q["options"], key=f"radio{i}")

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
