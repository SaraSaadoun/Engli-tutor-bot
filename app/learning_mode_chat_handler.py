from langchain_core.messages import HumanMessage, AIMessage
from chat_handler import ChatHandler
import streamlit as st
import time

class LearningModeChatHandler(ChatHandler):
    def __init__(self):
        super().__init__()
        self.system_message = """
        You are an expert English teacher. That facilitate information in a simple way. 
        You have strong knowledge about word difinations, grammer and so on. 
        So, The user will ask you some questions, and you will answer it kindly with the context of your chat so far. 
        Please give short and precise answers.""".strip()

        st.session_state.learning_chat_history = [
            ("system", self.system_message)
        ]

    def log_interaction(self, human_message: HumanMessage, ai_message: AIMessage):
        st.session_state.learning_chat_history.append(("human", human_message.content))
        st.session_state.learning_chat_history.append(("assistant", ai_message.content))


    def display_all_messages(self):
        for sender, message in st.session_state.learning_chat_history:
            if sender == "human":
                with st.chat_message('human'):
                    st.markdown(message)
            elif sender == "assistant":
                with st.chat_message('ai'):
                    st.markdown(message)

    def get_response_with_timing(self, user_input):
        chat_history = st.session_state.learning_chat_history
        start_time = time.time()  
        response = self.llm.invoke(chat_history + [("human", user_input)])
        response_time = time.time() - start_time  
        
        self.log_interaction(HumanMessage(user_input), AIMessage(response.content))

        return response.content, response_time
