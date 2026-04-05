import streamlit as st

from google import genai

# ===== ตั้งค่า =====

st.set_page_config(page_title="Gemini Chat", page_icon="🤖")

# โหลด API Key

gemini_api_key = st.secrets["gemini_api_key"]

gmn_client = genai.Client(api_key=gemini_api_key)

# ===== ฟังก์ชันเรียก Gemini =====

def generate_gemini_answer(prompt):

    try:

        response = gmn_client.models.generate_content(

            model="gemini-2.5-flash-lite",

            contents=prompt

        )

        return response.text

    except Exception as e:

        return f"❌ Error: {e}"

# ===== สร้าง memory chat =====

if "messages" not in st.session_state:

    st.session_state.messages = []

# ===== แสดงข้อความย้อนหลัง =====

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

# ===== รับ input =====

# st.chat_input แสดงกล่องพิมพ์ด้านล่าง

if prompt := st.chat_input("Message to Gemini..."):

    # 1. เก็บข้อความ user

    st.session_state.messages.append({

        "role": "user",

        "content": prompt

    })

    # 2. แสดงข้อความ user

    with st.chat_message("user"):

        st.markdown(prompt)

    # 3. เรียก AI และแสดงผล

    with st.chat_message("assistant"):

        with st.spinner("กำลังคิด..."):

            response = generate_gemini_answer(prompt)

            st.markdown(response)

    # 4. เก็บคำตอบ AI

    st.session_state.messages.append({

        "role": "assistant",

        "content": response

    })
 
