import streamlit as st
from detector import PrivacyDetector


# Page configuration
st.set_page_config(
    page_title="Shadow AI Privacy Auditor",
    page_icon="🔒"
)

st.title("🔒 Shadow AI Privacy Auditor")
st.write(
    "Identify and remove sensitive information before sharing text with public AI tools."
)


# Create detector
detector = PrivacyDetector()


# User input
text_input = st.text_area(
    "Paste the text you want to check:",
    height=250,
    placeholder="Example: My email is test@example.com"
)


if st.button("Analyze Text"):

    if text_input.strip():

        findings = detector.detect(text_input)

        if findings:

            st.success(f"✅ {len(findings)} sensitive item(s) detected.")
            
            st.subheader("⚠️ Detected Sensitive Information")

            for item in findings:
                st.warning(
                    f"""
                    **{item['label']}**  
                    Found: `{item['text']}`  
                    Category: {item['category']}  
                    Risk: {item['risk']}  
                    Confidence: {item['confidence']}  
                    
                    Explanation: {item['explanation']}
                    """
                )


            st.subheader("🖍️ Highlighted Preview")

            highlighted_text = text_input

            for item in sorted(findings, key=lambda x: len(x["text"]), reverse=True):
                highlighted_text = highlighted_text.replace(
                    item["text"],
                    f"<mark>{item['text']}</mark>"
                )

            st.markdown(highlighted_text, unsafe_allow_html=True)

            st.subheader("🛡️ Safer Redacted Version")

            redacted_text = text_input

            # Replace longer matches first to avoid partial replacements
            for item in sorted(findings, key=lambda x: len(x["text"]), reverse=True):
                redacted_text = redacted_text.replace(
                    item["text"],
                    f"[{item['label']}]"
                )

            st.text_area(
                "Redacted text:",
                redacted_text,
                height=200
            )

        else:

            st.success(
                "✅ No sensitive information detected. Your text appears safe."
            )

    else:
        st.info("Please enter text to analyze.")
