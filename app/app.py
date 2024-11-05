from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import streamlit as st
import time
import uuid
import os
from logger import log_interactions
from learning_mode_chat_handler import LearningModeChatHandler
from practising_mode_chat_handler import PracticeModeChatHandler
from chat_context import ChatContext

load_dotenv()




########################################################################
#                   session state variables                            #
########################################################################
if 'user_id' not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())  

if 'mode' not in st.session_state:
    st.session_state.mode = 'Learning'

if 'learning_chat_history' not in st.session_state:
    st.session_state.learning_chat_history = []

if 'practice_chat_history' not in st.session_state:
    st.session_state.practice_chat_history = []

if 'learning_mode_chat_handler' not in st.session_state:
    st.session_state.learning_mode_chat_handler = LearningModeChatHandler()

if 'practice_mode_chat_handler' not in st.session_state:
    st.session_state.practice_mode_chat_handler = PracticeModeChatHandler()

if 'chat_context' not in st.session_state:
    st.session_state.chat_context = ChatContext(st.session_state.learning_mode_chat_handler)

########################################################################
#               Basic Elements of User Interface                       #
########################################################################
st.title(f'🌐 Enli Tutor Bot  • ')

mode = st.sidebar.selectbox('Chatbot Mode', ['Learning', 'Practice'])

user_query = st.chat_input('Enter your message here.')

st.session_state.mode = mode


if st.session_state.mode == 'Learning':
    st.session_state.chat_context.switch_mode(st.session_state.learning_mode_chat_handler)
else:
    st.session_state.chat_context.switch_mode(st.session_state.practice_mode_chat_handler)

st.subheader(f'{st.session_state.mode} Mode {"🌱" if st.session_state.mode == "Learning" else "💬"}')

########################################################################
#                            Actions                                   #
########################################################################       
st.session_state.chat_context.display_all_messages()

if user_query is not None and user_query != "":

    with st.chat_message('human'):
        st.markdown(user_query)

    with st.chat_message('ai'):
        ai_response, response_time = st.session_state.chat_context.get_response_with_timing(user_query)

        # st.markdown(ai_response)
        st.write_stream(st.session_state.chat_context.stream_response(ai_response))


    # log_interactions(model_name, st.session_state.user_id, mode, user_query, ai_response, response_time)
