# GenAI-SummerCamp-ConversationalAssistant

## Table of Contents
1. [Introduction](#introduction)
2. [GenAI Summer Camp Details](#genai-summer-camp-details)
3. [Conversational Assistant Prompts](#conversational-assistant-prompts)
   - [Router Prompt](#router-prompt)
   - [Question Prompt](#question-prompt)
   - [Application Prompt](#application-prompt)
4. [Open Questions & Responses](#open-questions--responses)
   - [Optimization Process](#optimization-process)
   - [Prompt Performance Testing](#prompt-performance-testing)
   - [Considered Edge Cases](#considered-edge-cases)
5. [Documentation](#documentation)
   - [Approach](#approach)
   - [Running the Solution](#running-the-solution)
6. [Using ChatGPT for Documentation](#using-chatgpt-for-documentation)

## Introduction

The GenAI Summer Camp Assistant is a conversational AI designed to provide parents with information about the GenAI Summer Camp and facilitate the sign-up process for their kids.

## GenAI Summer Camp Details

The GenAI Summer Camp is a place where imagination meets innovation, offering a unique and immersive experience for young minds. The camp is designed to foster creativity and pique interest in cutting-edge technologies. With offerings like Robotics and AI, Virtual Reality, Augmented Reality, and Coding, campers are given the tools to explore, create, and innovate. The camp values imagination, collaboration, and lifelong learning.

## Conversational Assistant Prompts

### Router Prompt
The `router prompt` is the initial touchpoint for interactions with the GenAI Summer Camp Assistant. Using the `FewShotChatMessagePromptTemplate`, it sets the context for the conversation. By analyzing the intent behind the user's query, it efficiently directs them to either gather more information about the camp or initiate the sign-up process.

### Question Prompt
The `question` prompt is optimized for answering questions about the camp. It leverages the `FewShotChatMessagePromptTemplate` with a system message that offers a backdrop about the assistant's role and the camp's details.

### Application Prompt
The `application` prompt is designed for handling camp sign-ups. Similar to the question prompt, it uses a few-shot approach, guiding the assistant based on past examples to handle the application process smoothly.

## Open Questions & Responses

### Optimization Process
#### 1. **Knowledge Enhancement using RAG**:
Implement RAG with a vector database containing information on various summer camps to fetch relevant external data and minimize hallucinations.

#### 2. **Fine-Tuning the Model**:
Utilize OpenAI's API to fine-tune the `gpt-3.5-turbo` model for improved conversational experience.

#### 3. **Advanced Age Validation**:
Develop a dynamic age validation system that adjusts to camp policy changes.

#### 4. **Database Integration**:
Integrate with a real-time database for effective application management.

#### 5. **Feedback Mechanism**:
Instate a feedback loop to refine the assistant's responses.

#### 6. **Handling Edge Cases**:
Address intricate edge cases such as special characters, multiple queries, and uncommon inputs.

#### 7. **Memory Optimization**:
Optimize memory usage by refining prompts, managing conversation memory, simplifying chains, handling data dynamically, and monitoring and profiling regularly.

### Prompt Performance Testing

Evaluate the assistant's responses through manual evaluation, A/B testing with parents, and monitoring response times.

### Considered Edge Cases
Address potential edge cases like managing multiple applications, recognizing alternate communication preferences, handling specialized inquiries, sensitive information handling, and more.

## Documentation

### Approach

The GenAI Summer Camp Assistant is developed using a modular approach with the `langchain` library. The assistant uses various chains and memory management tools for a natural conversational flow, and a few-shot learning approach for diverse user queries.

### Running the Solution

To run the solution:

1. **Setup**:
   - Ensure you have Python 3.9.7 installed. If not, you can download and install it from the [official Python website](https://www.python.org/downloads/).
   - Open the project in Visual Studio Code (VSCode).

2. **File Overview**:
   - **`GenAI_Camp_Assistant_Builder.ipynb`**: The main notebook where the conversational assistant is built. Located in the root directory.
   - **`scripts/generate_camp_details.py`**: A script that aids in generating details about the GenAI Summer Camp. You need to run this script to get the camp's details.
   - **`data/generation_prompt.txt`**: The output from `generate_camp_details.py`, which contains the generated camp details.

3. **Library Installation**:
   - Open the integrated terminal in VSCode.
   - Navigate to the project directory.
     ```bash
     cd path/to/your/project/directory
     ```
   
4. **OpenAI Key Setup**:
   - The `GenAI_Camp_Assistant_Builder.ipynb` requires an OpenAI API key for execution. Ensure you add your OpenAI key in the notebook where indicated.

5. **Interacting with the Assistant**:
   - To get the best results, use the following example prompts when interacting with the assistant:
     - **General Information**: "Tell me about the GenAI Summer Camp."
     - **Offerings Inquiry**: "What activities and courses do you offer at the camp?"
     - **Pricing Details**: "How much does it cost to enroll my child in the camp?"
     - **Sign-up Process**: "I'd like to sign up my child for the camp. Can you guide me through the process?"
     - **Age Restrictions**: "What is the age range for camp attendees?"


## Using ChatGPT for Documentation

Throughout this README's development, ChatGPT was used for formatting, structuring, ensuring a comprehensive and user-friendly document.
