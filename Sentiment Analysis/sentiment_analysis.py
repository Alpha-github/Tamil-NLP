import streamlit as st
st.title("Sentiment Analysis")
st.write("---")
message = st.text_input("Enter the message")
def submit(message):
    st.success("Hey this is the message passed {}".format(message))
if st.button("Submit"):
    submit(message)