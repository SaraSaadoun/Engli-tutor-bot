# 🌐 Engli Tutor Chatbot
DEPI Microsoft Machine Learning Track final project.

## 1. Overview

This project develops a conversational chatbot, initially based on the **LLaMA model**. Due to deployment constraints on Azure, we transitioned to an alternative solution using the **Google Generative AI API**, showcased in a **Streamlit** application. The chatbot integrates **MLflow** to track interactions, enabling evaluation and analysis of AI responses and overall performance.

### Chatbot Modes

The chatbot application operates in two distinct modes, each with a unique system prompt to guide the model's role:

1. **Learning Mode**: The chatbot acts as an **expert English teacher**, providing explanations, corrections, and guidance on grammar and vocabulary.

2. **Practice Mode**: The chatbot functions as a **conversational partner**, helping users improve their English through casual conversation practice, encouraging natural language use.
<div align="center">
  <img src="https://github.com/user-attachments/assets/23ec1532-3755-4d90-867d-983d163bf496" alt="Chatbot Modes" />
</div>

---

Each mode uses a structured prompt template to maintain clarity and consistency in responses, as shown in the images below:

- **Prompt Template**:  
  <div align="center">
    <img src="https://github.com/user-attachments/assets/11d61815-5154-407d-ab86-48bd3e69d785" alt="Prompt Template" />
  </div>

- **Streamlit Flow**:  
  The flow of the Streamlit application is shown below, providing a seamless user experience:
  
<div align="center">
  <img src="https://github.com/user-attachments/assets/2df9f6ad-ca0b-44a4-9fe8-5e9619c6b3da" alt="Streamlit Flow" />
</div>

## 2. Methodology

### 2.1. Datasets & preprocessing

- **Grammar Correction Dataset**  
  - Cleaned data, handled missing values, applied filtering, and performed sentiment scoring with the VADER lexicon.

- **English Dictionary Dataset**  
  - Performed some analysis including frequency distribution analysis to enhance understanding of word usage patterns.

### 2.2 Model Selection
- Adapted the **LLaMA** model to meet chatbot-specific requirements.
- Fine-tuned the **NousResearch/Llama-2-7b-chat-hf** model using quantization techniques on Google Colab. Utilized quantization to reduce the model's memory footprint.

### 2.4 Deployment Using Streamlit Framework
- Deployed the chatbot using **Streamlit**, providing a user-friendly interface with multi-mode interaction. The integration with **MLflow** allows tracking and managing interactions, helping refine the user experience.


