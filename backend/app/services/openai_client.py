import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def ask_openai(system_prompt, user_message, memory=None):
    """
    Send a chat completion request to OpenAI API with conversation context.
    
    LOGIC EXPLANATION (Step-by-step):
    1. Validate inputs to ensure system_prompt and user_message are not empty
    2. Build message array starting with conversation history (memory) if available
    3. Add system prompt to set the AI's behavior and context
    4. Add the current user message as the latest input
    5. Send all messages to OpenAI API with temperature=0.4 for balanced creativity
    6. Extract and return the AI's response text
    7. Handle any errors gracefully and return a user-friendly error message
    
    Args:
        system_prompt (str): Instructions that define the AI's role and behavior
        user_message (str): The current user's question or input
        memory (list, optional): Previous conversation messages for context
    
    Returns:
        str: AI's response text or error message
        
    Edge cases handled:
    - Empty or None system_prompt: Returns error message
    - Empty or None user_message: Returns error message
    - None memory: Treated as empty conversation history
    - OpenAI API failures: Caught and returns user-friendly error
    - Invalid response format: Returns error message
    """
    try:
        # Edge case: Validate required inputs
        if not system_prompt or not isinstance(system_prompt, str) or not system_prompt.strip():
            return "⚠️ System configuration error. Please contact support."
        
        if not user_message or not isinstance(user_message, str) or not user_message.strip():
            return "⚠️ Please provide a valid message."
        
        # Step 1: Initialize messages array
        messages = []

        # Step 2: Add conversation history if available
        if memory and isinstance(memory, list):
            messages.extend(memory)

        # Step 3: Add system prompt to define AI behavior
        messages.append({"role": "system", "content": system_prompt.strip()})
        
        # Step 4: Add current user message
        messages.append({"role": "user", "content": user_message.strip()})

        # Step 5: Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.4
        )

        # Step 6: Extract and validate response
        if not response or not response.choices:
            return "⚠️ AI response failed. Please try again."
            
        return response.choices[0].message.content

    except Exception as e:
        # Step 7: Handle errors gracefully
        print("🔥 OpenAI ERROR:", e)
        return "⚠️ AI response failed. Please try again."


































































# def ask_openai(system_prompt: str, user_message: str, memory=None) -> str:
#     messages = []

#     # 🧠 past conversation (memory)
#     if memory:
#         messages.extend(memory)

#     # 🧾 system + user message
#     messages.append({"role": "system", "content": system_prompt})
#     messages.append({"role": "user", "content": user_message})

#     # 🤖 OpenAI call
#     response = client.chat.completions.create(
#         model="gpt-4o-mini",   # or gpt-4.1-mini
#         messages=messages,
#         temperature=0.4
#     )

#     return response.choices[0].message.content
