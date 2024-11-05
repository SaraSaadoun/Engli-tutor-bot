from langchain_core.messages import HumanMessage, AIMessage
from chat_handler import ChatHandler
import streamlit as st
import time

class PracticeModeChatHandler(ChatHandler):
    def __init__(self):
        super().__init__()
        self.system_message = """
        You are an English conversation partner. Your goal is to help the user practice
        English by engaging in natural, interactive conversation on any topic they choose.
        Maintain a friendly, encouraging tone, and provide feedback on their language use if needed.
        If asked, you can introduce new vocabulary or correct grammar gently. Please give short and precise answers.
        """.strip()

        st.session_state.practice_chat_history = [
            ("system", self.system_message)
        ]

    def log_interaction(self, human_message: HumanMessage, ai_message: AIMessage):
        st.session_state.practice_chat_history.append(("human", human_message.content))
        st.session_state.practice_chat_history.append(("assistant", ai_message.content))


    def display_all_messages(self):
        for sender, message in st.session_state.practice_chat_history:
            if sender == "human":
                with st.chat_message('human'):
                    st.markdown(message)
            elif sender == "assistant":
                with st.chat_message('ai'):
                    st.markdown(message)

    def get_response_with_timing(self, user_input):
        chat_history = st.session_state.practice_chat_history
        start_time = time.time()  
        response = self.llm.invoke(chat_history + [("human", user_input)])
        response_time = time.time() - start_time  
        
        self.log_interaction(HumanMessage(user_input), AIMessage(response.content))

        return response.content, response_time
    