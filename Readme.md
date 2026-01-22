📝 AI 기반 서술형 평가 및 자동 채점 시스템

이 프로젝트는 Streamlit을 활용하여 학생들의 서술형 답안을 수집하고, OpenAI (GPT) 모델을 통해 실시간으로 채점 및 피드백을 제공하며, 결과를 Supabase 데이터베이스에 영구 저장하는 시스템입니다.

📊 시스템 구조도 (System Architecture)

graph TD
    A[👨‍🎓 학생] -->|1. 답안 입력| B(Streamlit 웹 인터페이스)
    B -->|2. 제출 버튼 클릭| C{유효성 검사}
    C -->|성공| D[✅ 제출 완료 상태]
    D -->|3. 피드백 요청| E[🤖 OpenAI API]
    E -->|4. 채점 및 피드백 생성| F[결과 처리 및 정규화]
    F -->|5. 데이터 저장| G[(🗄️ Supabase DB)]
    F -->|6. 결과 화면 출력| B


🛠️ 주요 기능

학생용 인터페이스 (Step 1-2)

학번 및 서술형 3문항(기체 법칙, 열에너지 등) 답안 입력 폼 제공.

필수 입력값 검증 (학번 누락 방지).

AI 자동 채점 및 피드백 (Step 2)

OpenAI API를 활용하여 교사가 설정한 채점 기준(Guideline)에 따라 분석.

O/X 판정 및 친절한 문장형 피드백 생성.

응답 텍스트 정규화(Normalization)를 통해 일관된 출력 형식을 보장.

데이터베이스 연동 (Supabase)

학생의 답안, AI의 피드백, 당시의 채점 기준을 모두 DB에 저장.

st.secrets를 통한 안전한 API 키 관리.

⚙️ 설치 및 설정 (Setup)

1. 라이브러리 설치

프로젝트 실행을 위해 필요한 Python 패키지를 설치합니다.

pip install streamlit openai supabase


2. 비밀 키 설정 (Secrets)

프로젝트 루트 경로에 .streamlit/secrets.toml 파일을 생성하고 아래 내용을 입력해야 합니다.

# .streamlit/secrets.toml

OPENAI_API_KEY = "sk-..."
SUPABASE_URL = "[https://your-project-id.supabase.co](https://your-project-id.supabase.co)"
SUPABASE_SERVICE_ROLE_KEY = "eyJ..."


주의: SUPABASE_SERVICE_ROLE_KEY는 서버 전용 키이므로 외부에 노출되지 않도록 주의하세요.

📂 코드 상세 설명

1️⃣ Supabase 클라이언트 연결

get_supabase_client() 함수를 통해 DB 연결을 생성하고 @st.cache_resource로 연결 객체를 캐싱하여 성능을 최적화합니다.

2️⃣ UI 구성 및 입력 처리

st.form을 사용하여 학번과 3개의 문항을 그룹화했습니다.

사용자가 제출 버튼을 누르면 입력값을 검증하고 st.session_state에 상태를 저장하여 새로고침 시에도 데이터가 유지되도록 합니다.

3️⃣ AI 채점 로직 (Prompt Engineering)

Prompt 구성: 문항 번호, 채점 기준, 학생 답안을 포함하여 AI에게 역할을 부여합니다.

출력 제어: AI가 반드시 O: ... 또는 X: ... 형식으로 답하도록 프롬프트에 명시했습니다.

후처리 함수 (normalize_feedback): AI가 형식을 지키지 않을 경우를 대비해 코드로 강제 포맷팅 및 글자 수 제한(200자)을 수행합니다.

4️⃣ 데이터 저장 구조

Supabase student_submissions 테이블에 저장되는 데이터 구조는 다음과 같습니다.

필드명

설명

student_id

학생 학번

answer_1~3

학생이 작성한 답안

feedback_1~3

AI가 생성한 피드백

guideline_1~3

채점 당시의 기준 (버전 관리 용도)

model

사용된 AI 모델명 (예: gpt-5-mini)

🚀 실행 방법

터미널에서 아래 명령어를 실행하여 웹 애플리케이션을 시작합니다.

streamlit run app.py


💡 참고 사항

코드 상의 모델명 gpt-5-mini는 예시일 수 있으며, 실제 사용 가능한 모델(gpt-4o, gpt-4o-mini 등)로 변경하여 사용하시기 바랍니다.

Supabase 테이블(student_submissions)이 미리 생성되어 있어야 데이터가 정상적으로 저장됩니다.
