import streamlit as st
from modules.bug_detector import detect_bugs
from modules.security_checker import check_security
from modules.complexity_checker import analyze_complexity
from modules.documentation_generator import generate_docs
from modules.project_health import calculate_health
from modules.refactoring import get_refactoring_suggestions
from modules.project_summary import generate_summary

st.set_page_config(
    page_title="AI Code Intelligence Platform",
    page_icon="💻",
    layout="wide"
)

st.title("💻 AI Code Intelligence Platform")

uploaded_file = st.file_uploader(
    "Upload Python File",
    type=["py"]
)

if uploaded_file is not None:

    code = uploaded_file.read().decode("utf-8")

    st.subheader("📄 Uploaded Code")
    st.code(code, language="python")

    # Bug Detection
    bugs = detect_bugs(code)

    st.subheader("🐞 Bug Detection")

    if bugs:
        for bug in bugs:
            st.warning(bug)
    else:
        st.success("No Bugs Found")

    # Security
    security = check_security(code)

    st.subheader("🔒 Security Analysis")

    if security:
        for issue in security:
            st.error(issue)
    else:
        st.success("No Security Issues Found")

    # Complexity
    complexity = analyze_complexity(code)

    st.subheader("📊 Complexity Analysis")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Quality Score", complexity["score"])
    c2.metric("Functions", complexity["functions"])
    c3.metric("Loops", complexity["loops"])
    c4.metric("Conditions", complexity["conditions"])

    # Health Score
    health = calculate_health(
        bugs,
        security,
        complexity
    )

    st.subheader("❤️ Project Health Score")

    st.metric(
        "Overall Score",
        f"{health['score']}/100"
    )

    st.success(
        f"Project Grade: {health['grade']}"
    )

    # Documentation
    st.subheader("📝 Documentation Generator")

    docs = generate_docs(code)

    for doc in docs:
        st.code(doc)

    # Refactoring
    st.subheader("🔧 Refactoring Suggestions")

    suggestions = get_refactoring_suggestions(code)

    for suggestion in suggestions:
        st.info(suggestion)

    # Summary
    summary = generate_summary(code)

    st.subheader("📋 Project Summary")

    s1, s2, s3 = st.columns(3)

    s1.metric("Functions", summary["functions"])
    s2.metric("Classes", summary["classes"])
    s3.metric("Imports", summary["imports"])