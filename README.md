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
6. [Contribution & Collaboration](#contribution--collaboration)
7. [Contact Information](#contact-information)
8. [Acknowledgments](#acknowledgments)

## Introduction
[Your introduction content here]

## GenAI Summer Camp Details
[Details about the camp here]

## Conversational Assistant Prompts
### Router Prompt
[Description and code for the router prompt]

### Question Prompt
[Description and code for the question prompt]

### Application Prompt
[Description and code for the application prompt]

## Open Questions & Responses
### How would you optimize the process if you had more time?
1. If I had more time I would implement Retrieval-Augmented Generation (RAG) with information on different summer camps stored in a vector database. RAG would fetch relevant data from outside the foundation model and would enhance the input with this data. This would make the current assistant more knowledgeable about summer camps in general and would be more helpful to users. It would also reduce hallucinations from occurring.
2. I would fine-tune the gut-3.5-turbo model using Openai's API. I would synthetically generate training data that contains personalized assistant responses. This would improve the overall user experience and users will not feel like they are talking with a bot but with a human. (This can also be achieved in the system prompt but fine-tuning achieves better results).
3. Develop a more sophisticated age validation system to automatically adjust to any changes in camp policy.
4. Integrate with a real-time database to manage and track applications seamlessly.
5. Establish a feedback mechanism to continuously refine and enhance the assistant's responses.
6. Address nuanced edge cases such as handling special characters, multiple queries in a single prompt, or uncommon user inputs.

### How would you test the prompts' performance?

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
I would add handling of the following edge cases:

Sensitive Information Handling: Ensure that the assistant doesn't accidentally store or misuse sensitive information like phone numbers, email addresses, etc.

Repeated Queries: Parents might ask the same question in different ways. The assistant should be able to recognize this and not provide redundant or conflicting information.

Multilingual Support: Depending on the region, parents might ask questions in different languages. Adding support for major languages can be beneficial.

Emergency Situations: If a parent expresses a concern about an emergency or a serious issue, the assistant should be equipped to escalate the matter or provide immediate contact details.

Dietary requirements: The user 

Age Outliers: While we validate the age based on the camp's age range, there might be special cases where a child slightly outside the age range might still want to attend due to exceptional circumstances. The assistant should be able to handle such nuanced scenarios.


## Documentation
### Approach
[Explanation of your approach to the assignment]

### Running the Solution
[Instructions on how to run and test your solution]

## Contribution & Collaboration
[Information about collaboration, if any, and how others can contribute]

## Contact Information
[Your or the project's contact information]

## Acknowledgments
[Any credits, references, or thanks you'd like to include]
