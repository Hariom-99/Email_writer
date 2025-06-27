import streamlit as st
from transformers import pipeline

# Load the Hugging Face model
generator = pipeline("text2text-generation", model="google/flan-t5-large")

def generate_email(email_type, bullet_points):
    prompt = f"Write a {email_type} email using these details:\n{bullet_points}"
    result = generator(prompt, max_length=512)
    return result[0]['generated_text']

# Streamlit app layout
st.title("📧 Email Writing Bot")

st.markdown("""
This bot helps you write professional emails based on bullet points.  
Select the type of email, enter your bullet points, and click **Generate**!
""")

# Dropdown to select the email type
email_type = st.selectbox(
    "Select email type:",
    [
        "apology",
        "leave request",
        "job application",
        "meeting invitation",
        "sales pitch",
        "customer support reply",
        "complaint reply",
        "resignation letter",
        "follow-up"
    ]
)

# Bullet points input box
bullet_points = st.text_area(
    "Enter bullet points for the email:",
    height=250,
    placeholder=(
        "Example:\n"
        "Employee Name: Hariom Patidar\n"
        "Leave Dates: July 10th to July 15th\n"
        "Leave Reason: Family function\n"
        "Tone: Polite and professional"
    )
)

# Generate button
if st.button("Generate Email"):
    if bullet_points.strip() == "":
        st.warning("⚠️ Please enter bullet points before generating.")
    else:
        with st.spinner("Generating your email..."):
            email = generate_email(email_type, bullet_points)
            st.subheader("✅ Generated Email:")
            st.write(email)

