import streamlit as st

st.set_page_config(
    page_title="Owl AI Web Interface",
    page_icon= "🦉",
    layout="centered"
)

st.sidebar.title(" 🦉 Owl AI")
page = st.sidebar.radio("Navigation", ["Home", "About", "Contact"])

if page == "Home":
    st.title("Welcome to Owl AI")
    st.write(
        "This is a simple and interactive web interface created as part of "
        "Task 2 using **Streamlit**."   
        )
    st.subheader("User INput Form")
    name = st.text_input("Enter your name")
    interest = st.selectbox(
        "Select your area of interset",
        ["Python", "AIML", "Web Development", "Data Science"]
    )

    if st.button("Submit"):
        st.success(f"Hello {name}! 👋")
        st.write(f"You are interested in **{interest}**.")


elif page == "About":
    st.title("About Owl AI")
    st.write(
        "Owl AI focuses on providing learning oppurtunities and real-world "
        "projects to help students and interns build strong technical skills."
    )

elif page == "Contact":
    st.title("Contact Us")
    email = st.text_input("Your Email")
    message = st.text_input("Your Message")

    if st.button("Send"):
        st.success("thank you! Your message has been submitted.")