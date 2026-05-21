import streamlit as st
import PyPDF2

# Page Config
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

# Title
st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get AI-based analysis 😄")

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# Skills Database
skills = [
    "Python",
    "Java",
    "SQL",
    "HTML",
    "CSS",
    "JavaScript",
    "Machine Learning",
    "Data Science",
    "Communication",
    "React",
    "Node.js",
    "C",
    "C++"
]

# Recommended Skills
recommended_skills = [
    "Python",
    "SQL",
    "Projects",
    "Communication",
    "Machine Learning"
]

# When File Uploaded
if uploaded_file is not None:

    # Read PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    # Resume Content
    st.subheader("📜 Resume Content")

    with st.expander("View Resume Text"):
        st.write(text)

    # Detect Skills
    st.subheader("✅ Detected Skills")

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    if found_skills:

        cols = st.columns(3)

        for index, skill in enumerate(found_skills):
            cols[index % 3].success(skill)

    else:
        st.error("No skills detected")

    # Resume Score
    score = len(found_skills) * 10

    if score > 100:
        score = 100

    st.subheader("📊 Resume Score")

    st.progress(score)

    st.metric(
        label="Resume Score",
        value=f"{score}/100"
    )

    # Missing Skills
    st.subheader("❌ Missing Recommended Skills")

    missing_skills = []

    for skill in recommended_skills:
        if skill not in found_skills:
            missing_skills.append(skill)

    if missing_skills:
        for skill in missing_skills:
            st.warning(skill)

    else:
        st.success("All important skills available!")

    # Suggestions
    st.subheader("💡 Suggestions")

    if score < 50:
        st.error(
            "Add more technical skills, projects, and certifications."
        )

    elif score < 80:
        st.warning(
            "Good resume. Add more projects and achievements."
        )

    else:
        st.success(
            "Excellent Resume! 😄"
        )

    # Job Recommendation
    st.subheader("💼 Suggested Job Role")

    if "Machine Learning" in found_skills:
        st.info("Machine Learning Engineer")

    elif "Java" in found_skills:
        st.info("Java Developer")

    elif "Python" in found_skills:
        st.info("Python Developer")

    else:
        st.info("Software Developer")