# 🌐 Engli Tutor Chatbot
DEPI Microsoft Machine Learning Track final project.

## 1. Overview

This project develops a conversational chatbot, initially based on the **LLaMA model**. Due to deployment constraints on Azure, we transitioned to an alternative solution using the **Google Generative AI API**, showcased in a **Streamlit** application. The chatbot integrates **MLflow** to track interactions, enabling evaluation and analysis of AI responses and overall performance.


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


