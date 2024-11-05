from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from abc import ABC, abstractmethod
import os
import time

class ChatHandler(ABC):
    def __init__(self):
        google_api_key = os.getenv("GOOGLE_API_KEY")
        if not google_api_key:
            print("Warning: GOOGLE_API_KEY not found. Ensure that your environment variables are set correctly.")
        os.environ["GOOGLE_API_KEY"] = google_api_key
        
        self.model_name = "gemini-1.5-flash"
        self.llm = ChatGoogleGenerativeAI(model=self.model_name)

    @abstractmethod
    def display_all_messages(self):
        """Display all chat messages in the current session."""
        pass

    @abstractmethod
    def log_interaction(self, human_message: HumanMessage, ai_message: AIMessage):
        """Log an interaction by appending human and AI messages to the current history."""
        pass

    @abstractmethod
    def get_response_with_timing(self, user_input):
        """Generate a response for user input and measure the time taken."""
        pass

    def stream_response(self, response, delay=0.1):
        """Simulates streaming the output by yielding one word at a time."""
        print("from streeeeem", response)
        for word in response.split():
            yield word + ' '
            time.sleep(delay)  



    
    