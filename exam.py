# Step 1‑1 – 서술형 문제 1개 포맷 (Streamlit)
# --------------------------------------------------
# 새 문항을 추가할 때는 QUESTION_2 / answer_2 블록을 복사‑붙여넣고
# answers.append(answer_2) 만 추가하면 별도 수정 없이 동작합니다.
# --------------------------------------------------

import streamlit as st

# ── 1. 수업 제목 ──
st.title("외계 행성계 탐사 방법")  # ← 교과별 제목으로 자유롭게 수정하세요.

# ── 2~4. 입력 + 제출을 form 안에 묶기 ──
with st.form("submit_form"):

    # ── 2. 학번 입력 ──
    student_id = st.text_input("학번", help="학생의 학번을 작성하세요. (예: 10130)")

    # ── 3. 서술형 문제 1 표시 ──
    QUESTION_1 = "기체 입자들의 운동과 온도의 관계를 서술하세요."  # ← 교사가 원하는 서술형 문제로 변경

    st.markdown("#### 서술형 문제 1")
    st.write(QUESTION_1)

    answer_1 = st.text_area("답안을 입력하세요", key="answer1", height=150)

    # 답안을 리스트로 모아 향후 문제 추가 시 재사용하기
    # 답안(answers)가 2,3 문항으로 확장되면 [answer_1, answer_2, answer_3] 형태로 변경
    # 현재는 1문항이므로 단일 리스트로 유지
    answers = [answer_1]

    # ── 4. 제출 버튼 ──
    submitted = st.form_submit_button("제출")


# ── 제출 처리 로직(제출 버튼을 눌렀을 때만 실행) ──
if submitted:
    if not student_id.strip():
        st.warning("학번을 입력하세요.")
    elif any(ans.strip() == "" for ans in answers):
        st.warning("모든 답안을 작성하세요.")
    else:
        st.success(f"제출 완료! 학번: {student_id}")
        # ⚠️ Step 2에서 GPT 채점 및 DB(Supabase) 저장 로직을 여기에 추가할 예정입니다.
