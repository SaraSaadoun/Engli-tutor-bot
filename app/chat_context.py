from langchain_core.messages import HumanMessage, AIMessage
from chat_handler import ChatHandler

import streamlit as st

class ChatContext:
    def __init__(self, chatHandler: ChatHandler):
        self.chat_handler = chatHandler

    def switch_mode(self, chatHandler: ChatHandler):
        """Switches the chat mode based on the handler class passed."""
        self.chat_handler = chatHandler
    
    def get_response_with_timing(self, user_input: str):
        """Gets a response from the current handler."""
        return self.chat_handler.get_response_with_timing(user_input)
    
    def display_all_messages(self):
        """Displays all messages from the current handler."""
        self.chat_handler.display_all_messages()
    
    def stream_response(self, response, delay=0.1):
        return self.chat_handler.stream_response(response, delay)

    