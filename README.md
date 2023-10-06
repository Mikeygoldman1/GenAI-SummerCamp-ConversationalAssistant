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
The `router` prompt is the initial touchpoint for interactions with the GenAI Summer Camp Assistant. It sets the context for the conversation. By analyzing the intent behind the user's query, it efficiently directs them to either gather more information about the camp or initiate the sign-up process.

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

#### 1. Manual Evaluation

**Step-by-Step Process**:

- **Document Creation**:
  - Draft a range of diverse user prompts.
  
- **User Testing**:
  - Have users test the assistant using the listed prompts.
  - Encourage additional relevant prompts from users.
  
- **Evaluation Criteria**:
  - For each response from the assistant, evaluators should consider if the assistant:
    1. Hallucinates.
    2. Repeats itself.
    3. Responds impersonally.
    4. Gives inappropriate answers.

#### 2. A/B Testing with Parents

- **Setup**:
  - Design two or more variations of the assistant, differing in prompts or response structures.

- **Distribution**:
  - Randomly segment parent testers, ensuring each subgroup interacts with a unique version of the assistant.

- **Objective**:
  - Monitor metrics like satisfaction rate, completion rate for sign-ups, and response clarity.

- **Feedback Collection**:
  - Gather feedback on user experience, preferences, and any suggestions.

- **Analysis**:
  - Evaluate each version's performance based on data and feedback. The version with superior metrics becomes the preferred choice.

- **Iteration**:
  - Use insights from the A/B test to refine the assistant, iterating as needed.

#### 3. Response Time Monitoring

- Regularly monitor response times to ensure swift and efficient operations, especially during peak demand periods.

### Considered Edge Cases

#### 1. **Multiple Children Applications**:
- Ensure the assistant can manage applications for multiple children from a single parent simultaneously, without confusion.

#### 2. **Alternate Communication Preferences**:
- Beyond just phone and email, recognize and process other modes of communication that parents might prefer, such as messaging apps or postal addresses.

#### 3. **Specialized Inquiries**:
- Handle inquiries related to:
  - **Dietary Restrictions**: Cater to specific dietary needs or allergies.
  - **Accessibility Provisions**: Address questions about facilities for differently-abled children.
  - **Unique Camp Accommodations**: Respond to queries about special camp provisions or services.

#### 4. **Sensitive Information Handling**:
- Ensure that the assistant does not inadvertently store or misuse sensitive information, including phone numbers and email addresses.

#### 5. **Repeated Queries**:
- Recognize and address situations where parents might phrase the same question differently. The assistant should provide consistent information without redundancy.

#### 6. **Multilingual Support**:
- Depending on the demographic, parents might interact in various languages. It would be beneficial for the assistant to support major languages, ensuring inclusivity.

#### 7. **Emergency Situations**:
- If a parent indicates an emergency or a grave concern, the assistant should be primed to escalate the situation or offer immediate contact details for resolution.

#### 8. **Age Outliers**:
- While age validation is crucial, the assistant should also cater to exceptions. For instance, if a child slightly outside the stipulated age range displays exceptional circumstances or reasons for attendance, the assistant should be equipped to address such nuanced scenarios.


## Documentation

### Approach

The GenAI Summer Camp Assistant is developed using a modular approach with the `langchain` library. The assistant uses various chains and memory management tools for a natural conversational flow, and a few-shot learning approach for diverse user queries.

### Running the Solution

To run the solution:

1. **Setup**:
   - Ensure you have Python 3.9.7 installed. If not, you can download and install it from the [official Python website](https://www.python.org/downloads/).
   - Open the project in Visual Studio Code (VSCode).

2. **File Overview**:
   - **`scripts/GenAI_Camp_Assistant_Builder.ipynb`**: The main notebook where the conversational assistant is built.
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
