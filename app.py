import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def generate_email(email_topic, sender, recipient, style, tone, urgency, subject_matter):
    llm = CTransformers(
        model='../models/llama-2-7b-chat.Q5_K_M.gguf',
        model_type='llama',
        config={
            'max_new_tokens': 256,
            'temperature': 0.01
        }
    )

    email_template = """
    Write an email with {style} style and {tone} tone on the subject matter of {subject_matter} with {urgency} urgency. Topic: {email_topic}.\n\nSender: {sender}\nRecipient: {recipient}
    \n\nEmail Text:
    """

    prompt = PromptTemplate(
        input_variables=["style", "email_topic", "sender", "recipient", "tone", "urgency", "subject_matter"],
        template=email_template,
    )
    
    email_response = llm(prompt.format(
        email_topic=email_topic,
        sender=sender,
        recipient=recipient,
        style=style,
        tone=tone,
        urgency=urgency,
        subject_matter=subject_matter
    ))
    return email_response

def main():
    st.set_page_config(
        page_title="Email Generator",
        page_icon="✉️",
        layout="centered",
        initial_sidebar_state='expanded'
    )
    
    st.sidebar.header("Input Parameters ✉️")
    email_topic = st.sidebar.text_area('Enter the email topic', height=100)
    email_sender = st.sidebar.text_input('Sender Name')
    email_recipient = st.sidebar.text_input('Recipient Name')
    email_style = st.sidebar.selectbox(
        'Writing Style',
        ('Formal', 'Appreciating', 'Not Satisfied', 'Neutral', 'Informal', 'Urgent', 'Casual', 'Professional'),
        index=0
    )
    email_tone = st.sidebar.selectbox(
        'Tone',
        ('Serious', 'Light-hearted', 'Respectful', 'Disappointed', 'Excited', 'Calm', 'Assertive', 'Friendly'),
        index=0
    )
    email_urgency = st.sidebar.selectbox(
        'Urgency Level',
        ('High', 'Medium', 'Low', 'Not Urgent'),
        index=0
    )
    email_subject_matter = st.sidebar.selectbox(
        'Subject Matter',
        ('Business', 'Personal', 'Technical', 'General Inquiry', 'Complaint', 'Appreciation', 'Update', 'Request'),
        index=0
    )

    if st.sidebar.button("Generate"):
        email_output = generate_email(email_topic, email_sender, email_recipient, email_style, email_tone, email_urgency, email_subject_matter)
        st.write(email_output)

if __name__ == "__main__":
    main()
