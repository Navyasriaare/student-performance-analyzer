import streamlit as st
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Student Performance Analyzer",
    page_icon="📊",
    layout="wide"
)

# ---------------- PROFESSIONAL CSS ----------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b, #334155);
    color: white;
}

/* BIG TITLE */
.main-title {
    text-align: center;
    font-size: 64px;
    font-weight: 800;
    color: white;
    margin-bottom: 10px;
}

/* Subtitle */
.sub-title {
    text-align: center;
    font-size: 22px;
    color: #e2e8f0;
    margin-bottom: 35px;
}

/* Make ALL labels WHITE */
label, .stNumberInput label, .stTextInput label {
    color: white !important;
    font-weight: 600 !important;
}

/* Button */
.stButton > button {
    width: 100%;
    background: #2563eb;
    color: white;
    font-size: 18px;
    font-weight: bold;
    padding: 12px;
    border-radius: 10px;
    border: none;
}

.stButton > button:hover {
    background: #1d4ed8;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="main-title">AI STUDENT PERFORMANCE ANALYZER</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="sub-title">Risk Prediction • Placement Analysis • Performance Evaluation</div>',
    unsafe_allow_html=True
)

# ---------------- INPUT SECTION ----------------
st.subheader("Enter Student Details")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Student Name")
    attendance = st.number_input("Attendance (%)", 0, 100, 75)
    internal = st.number_input("Internal Marks (%)", 0, 100, 60)
    assignment = st.number_input("Assignment Score (%)", 0, 100, 70)

with col2:
    semester = st.number_input("Semester Marks (%)", 0, 100, 65)
    communication = st.number_input("Communication Skills (%)", 0, 100, 55)
    coding = st.number_input("Coding Skills (%)", 0, 100, 50)
    backlogs = st.number_input("Number of Backlogs", 0, 20, 0)

analyze = st.button("Analyze Performance")

# ---------------- ANALYSIS ----------------
if analyze:

    avg = (internal + semester + assignment) / 3

    # Risk calculation
    if attendance < 40 or avg < 35 or backlogs >= 5:
        risk_score = 90
        risk_level = "HIGH"
    elif attendance < 65 or avg < 55 or backlogs >= 2:
        risk_score = 60
        risk_level = "MEDIUM"
    else:
        risk_score = 25
        risk_level = "LOW"

    # Placement calculation
    placement_score = (
        semester * 0.35 +
        communication * 0.25 +
        coding * 0.30 +
        attendance * 0.10
    ) - (backlogs * 5)

    placement_score = max(0, min(100, placement_score))

    # Performance score
    performance_score = avg

    # ---------------- SMALL BAR GRAPH ----------------
    st.subheader("Analysis Result (Graph)")

    labels = ["Risk of Failure", "Placement Chances", "Overall Performance"]
    values = [risk_score, placement_score, performance_score]

    # 🔹 SMALLER GRAPH SIZE
    fig, ax = plt.subplots(figsize=(6, 4))  # width, height in inches

    ax.bar(labels, values)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Score (%)")
    ax.set_title("Student Performance Analysis")

    st.pyplot(fig)

    # ---------------- SUMMARY ----------------
    st.subheader("Summary")

    st.write("Name:", name if name else "Student")
    st.write("Risk Level:", risk_level)
    st.write("Placement Score:", f"{placement_score:.1f}%")
    st.write("Overall Average:", f"{avg:.1f}%")

    # ---------------- AI SUGGESTIONS ----------------
    st.subheader("AI Suggestions")

    if attendance < 75:
        st.write("• Improve attendance above 75%")
    if communication < 60:
        st.write("• Improve communication skills")
    if coding < 60:
        st.write("• Practice coding daily")
    if backlogs > 0:
        st.write("• Clear backlogs quickly")
    if attendance >= 75 and communication >= 60 and coding >= 60 and backlogs == 0:
        st.write("• Excellent performance — maintain consistency")

st.markdown("---")
st.write("Developed using Streamlit")