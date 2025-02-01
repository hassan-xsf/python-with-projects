# from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage , HumanMessage , AIMessage

import streamlit as st

with st.sidebar:
    "## Features\n1. Answers your queries with ease.\n2. Provides you a well structured roadmap and resources."

st.title("💬 AI Roadmap Expert")
st.caption("🚀 A simple AI Expert Roadmap chatbot powered by Gemini API")


# load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
systemPrompt = "You are an AI Roadmap Expert, Your goal is to guide a user on learning X hobby, The hobby can be specific such as Learning Python or Learning a language.\
Your goal is to make an expert roadmap in a well structured manner, From 0 to 100 progress."

def callLLM(query: str):
    messages = [SystemMessage(content = systemPrompt)]
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            messages.append(HumanMessage(content = msg["content"]))
        else:
            messages.append(AIMessage(content = msg["content"]))

    response = llm.invoke(messages)
    return response

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "What are you planning to learn today?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Enter your queries")

if user_input:
    msg = user_input

    st.session_state["messages"].append({"role" : "user", "content" : msg})
    st.chat_message("user").write(msg)
    with st.spinner("Thinking..."):
        response = callLLM(msg)

    st.chat_message("assistant").write(response.content)
    st.session_state["messages"].append({"role" : "assistant", "content" : response.content})





