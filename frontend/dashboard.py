import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Job Application",
    page_icon="🤖",
    layout="wide"
)

# ------------------ CSS ------------------
st.markdown("""
<style>
body { background-color: #F5F7FF; }
.section { 
    background: white; padding: 25px; border-radius: 16px; 
    box-shadow: 0 4px 20px rgba(0,0,0,0.08); 
    margin-bottom: 25px;
}
.header {
    background: linear-gradient(90deg, #6C63FF, #A594F9);
    color: white;
    padding: 35px;
    border-radius: 12px;
    text-align: center;
    font-size: 35px;
    font-weight: bold;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown("<div class='header'>🤖 AI Job Application System</div>", unsafe_allow_html=True)
st.write("<p style='text-align:center;'>Automatically apply to Naukri jobs</p>", unsafe_allow_html=True)

# ------------------ LAYOUT ------------------
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("<div class='section'>", unsafe_allow_html=True)

    st.subheader("🔍 Job Details")

    job_title = st.text_input("Job Title", placeholder="Python Developer")
    location = st.text_input("Location", placeholder="Pune, Bangalore")
    resume_path = st.text_input("Resume Path", placeholder="C:/resume.pdf")
    job_count = st.slider("Number of jobs to apply", 1, 25, 5)

    if st.button("🚀 Apply Automatically", use_container_width=True):
        if job_title and location and resume_path:
            payload = {
                "job_title": job_title,
                "location": location,
                "resume_path": resume_path,
                "job_count": job_count
            }
            with st.spinner("Applying to jobs... ⏳"):
                response = requests.post(f"{API_URL}/apply-job", json=payload)
            st.success("🎉 Started job applications!")
            st.json(response.json())
        else:
            st.error("⚠️ Fill all fields.")

    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.subheader("📄 Logs")

    if st.button("Load Latest Logs", use_container_width=True):
        logs = requests.get(f"{API_URL}/logs").json()
        if logs["status"] == "success":
            st.text_area("Log Output", logs["log"], height=350)
        else:
            st.warning("No logs found.")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='section'>", unsafe_allow_html=True)
st.subheader("📊 Applied Jobs")

if st.button("Load Applied Jobs", use_container_width=True):
    data = requests.get(f"{API_URL}/applied-jobs").json()
    if data["status"] == "success":
        st.table(data["data"])
    else:
        st.warning("No applied job history.")
st.markdown("</div>", unsafe_allow_html=True)
