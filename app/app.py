import streamlit as st

st.title("AI-Powered Resume Screening (Demo)")
st.write("Upload a resume (TXT or PDF converted to text) and compare against a job description.")
resume = st.text_area("Paste Resume Text")
jd = st.text_area("Paste Job Description")
if st.button("Compute Fit Score"):
    if not resume or not jd:
        st.warning("Please paste both resume and job description.")
    else:
        # Simple demo scoring: keyword overlap
        r_tokens = set(resume.lower().split())
        jd_tokens = set(jd.lower().split())
        overlap = len(r_tokens & jd_tokens)
        denom = max(len(jd_tokens), 1)
        fit = round(100 * overlap / denom, 2)
        st.metric("Estimated Fit Score", f"{fit}%")
        st.caption("Demo computation for portfolio purposes. Replace with your trained model inference.")