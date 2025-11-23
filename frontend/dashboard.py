import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="JobPilot AI",
    page_icon="🛠️",
    layout="wide"
)

# -----------------------------------------------------------
# PREMIUM MODERN UI (GLASSMORPHISM + GRADIENT)
# -----------------------------------------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #17153B, #2E236C, #433D8B, #C8ACD6);
    background-attachment: fixed;
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* Centered title */
.header-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-top: 20px;
    color: #FFFFFF;
}

.subtitle {
    text-align:center;
    color:#E8E8F9;
    font-size:20px;
    margin-top:-10px;
    margin-bottom:35px;
}

/* Card style */
.card {
    background: rgba(255,255,255,0.12);
    padding: 25px;
    border-radius: 18px;
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.25);
    margin-bottom: 35px;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #6C63FF, #8C52FF);
    border: none;
    color: white;
    padding: 12px 25px;
    border-radius: 10px;
    font-size: 18px;
    font-weight: 600;
    transition: 0.2s ease-in-out;
}

.stButton > button:hover {
    transform: scale(1.07);
    background: linear-gradient(90deg, #8C52FF, #6C63FF);
}

/* Input & sliders */
.stTextInput>div>div>input {
    background-color: rgba(255,255,255,0.25);
    color: white;
}

.stSlider > div > div > div {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------
# HEADER
# -----------------------------------------------------------
st.markdown("<h1 class='header-title'>🚀 JobPilot AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Your intelligent job application assistant — fully automated, fully AI-powered.</p>", unsafe_allow_html=True)

# -----------------------------------------------------------
# MAIN LAYOUT — JOB SETTINGS + LOGS
# -----------------------------------------------------------
col1, col2 = st.columns([2, 1])

# -----------------------------------------------------------
# LEFT SIDE: Job Settings (Input Panel)
# -----------------------------------------------------------
with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("🛠️ Job Application Settings")

    job_title = st.text_input("Job Title", placeholder="Python Developer / Software Engineer")
    location = st.text_input("Preferred Location", placeholder="Pune, Bangalore, Remote, Germany")
    resume_path = st.text_input("Resume File Path", placeholder="C:/Users/YourName/resume.pdf")

    experience = st.slider("Experience Level (Years)", 0, 10, 1)
    job_count = st.slider("Number of Jobs to Apply", 1, 25, 5)

    if st.button("🚀 Start Auto-Apply", use_container_width=True):
        if job_title and location and resume_path:
            payload = {
                "job_title": job_title,
                "location": location,
                "resume_path": resume_path,
                "job_count": job_count,
                "experience": experience
            }
            with st.spinner("JobPilot AI is applying to jobs for you… ⏳"):
                response = requests.post(f"{API_URL}/apply-job", json=payload)

            st.success("🎉 Auto-application started successfully!")
            st.json(response.json())
        else:
            st.error("⚠️ Please complete all fields to continue.")

    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------------
# RIGHT SIDE: Logs Panel
# -----------------------------------------------------------
with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.subheader("📄 Latest JobPilot Logs")

    if st.button("📥 Load Logs", use_container_width=True):
        logs = requests.get(f"{API_URL}/logs").json()

        if logs["status"] == "success":
            st.text_area("JobPilot AI Logs", logs["log"], height=350)
        else:
            st.warning("No job logs found yet!")

    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------------
# APPLIED JOBS SECTION (Full Width)
# -----------------------------------------------------------
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📊 Applied Jobs History")

if st.button("📥 Load Applied Jobs", use_container_width=True):
    response = requests.get(f"{API_URL}/applied-jobs").json()

    if response["status"] == "success":
        st.table(response["data"])
    else:
        st.warning("No applied job records yet. Start applying above!")

st.markdown("</div>", unsafe_allow_html=True)
