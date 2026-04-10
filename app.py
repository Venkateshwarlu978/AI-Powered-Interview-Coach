import streamlit as st
from utils import generate_question, evaluate_answer
from streamlit_mic_recorder import speech_to_text

# 1. Page Configuration
st.set_page_config(page_title="AI Interview Coach", layout="centered")
st.title("🤖 AI Interview Coach")

# 2. Session State Initialization
if "question" not in st.session_state:
    st.session_state.question = ""

# 3. Sidebar / Selection
role = st.selectbox("Select Job Role", 
                    ["Data Analyst", "ML Engineer", "Software Developer"])

col1, col2 = st.columns(2)

with col1:
    if st.button("Start Interview"):
        st.session_state.question = generate_question(role)
        st.rerun() # Refresh to show the new question

with col2:
    if st.button("Next Question") and st.session_state.question:
        st.session_state.question = generate_question(role)
        st.rerun()

# 4. Interview Logic
if st.session_state.question:
    st.subheader("Interview Question:")
    st.info(st.session_state.question)

    st.write("---")
    
    # --- VOICE INPUT SECTION ---
    st.write("### 🎤 Option 1: Answer with Voice")
    text_from_voice = speech_to_text(
        language='en', 
        start_prompt="Start Recording", 
        stop_prompt="Stop Recording", 
        key='stt_recorder' # Unique key
    )

    # --- TEXT INPUT SECTION ---
    st.write("### ⌨️ Option 2: Type your Answer")
    text_from_input = st.text_area("Type here...", placeholder="Your answer goes here...")
    submit_text = st.button("Submit Typed Answer")

    # 5. Handling the Response (Voice or Text)
    final_answer = None
    
    if text_from_voice:
        final_answer = text_from_voice
        st.success(f"Captured Voice: {text_from_voice}")
    elif submit_text and text_from_input:
        final_answer = text_from_input

    # 6. Evaluation Logic
    if final_answer:
        with st.spinner("🤖 AI is evaluating your response..."):
            feedback = evaluate_answer(st.session_state.question, final_answer)
            
            st.subheader("📊 Feedback Results")
            st.markdown(feedback)
else:
    st.write("Click 'Start Interview' to begin your session.")