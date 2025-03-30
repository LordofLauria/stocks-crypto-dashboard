import random
import time

import streamlit as st


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hey there! Need help? Pepe would be happy to assist you.",
            "Hi! What's up? Don't forget to send a racist Pepe meme today!",
            "Hello! Need assistance? My stock website will make you a trillionaire!",
            "Hey! Got a question?",
            "Hi there! How can Pepe help?",
            "Hello! Looking for help?",
            "Hey! Need assistance? Pepe has gotchu!",
            "Hi! Miss Sleepy Joe yet?",
            "Hello! Need help from a virtual frog?",
            "Hey there! Any questions from a formerly racist dog whistle?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})