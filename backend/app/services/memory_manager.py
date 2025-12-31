# Simple in-memory conversation store
# Later we can replace with Redis / DB / Vector DB

from typing import List, Dict

# Structure:
# {
#   "chat_id_1": [
#       {"role": "user", "content": "..."},
#       {"role": "assistant", "content": "..."}
#   ]
# }

_MEMORY_STORE: Dict[str, List[Dict[str, str]]] = {}


def get_memory(chat_id: str) -> List[Dict[str, str]]:
    """
    Retrieve conversation history for a specific chat session.
    
    LOGIC EXPLANATION (Step-by-step):
    1. Validate that chat_id is a non-empty string
    2. Look up the chat_id in the in-memory conversation store
    3. Return the conversation history if found, or empty list if not found
    
    Args:
        chat_id (str): Unique identifier for the chat session
        
    Returns:
        List[Dict[str, str]]: List of message dictionaries with 'role' and 'content' keys
        
    Edge cases handled:
    - None or empty chat_id: Returns empty list
    - Non-existent chat_id: Returns empty list
    - Invalid type for chat_id: Returns empty list
    """
    # Edge case: Validate chat_id
    if not chat_id or not isinstance(chat_id, str):
        return []
    
    return _MEMORY_STORE.get(chat_id, [])


def add_message(chat_id: str, role: str, content: str) -> None:
    """
    Add a new message to the conversation history of a chat session.
    
    LOGIC EXPLANATION (Step-by-step):
    1. Validate all input parameters are non-empty strings
    2. Validate role is either 'user' or 'assistant' or 'system'
    3. Check if chat_id exists in memory store
    4. Create new conversation list if chat_id doesn't exist
    5. Append the new message with role and content to the conversation
    
    Args:
        chat_id (str): Unique identifier for the chat session
        role (str): Message role ('user', 'assistant', or 'system')
        content (str): The message content/text
        
    Returns:
        None
        
    Edge cases handled:
    - None or empty chat_id: Function returns without adding
    - Invalid role: Function returns without adding
    - None or empty content: Function returns without adding
    - First message in a new chat: Creates new conversation list
    """
    # Edge case: Validate all inputs
    if not chat_id or not isinstance(chat_id, str):
        return
    
    if not role or not isinstance(role, str) or role not in ['user', 'assistant', 'system']:
        return
    
    if content is None or not isinstance(content, str):
        return
    
    # Initialize conversation if this is a new chat_id
    if chat_id not in _MEMORY_STORE:
        _MEMORY_STORE[chat_id] = []

    # Add message to conversation history
    _MEMORY_STORE[chat_id].append({
        "role": role,
        "content": content
    })


def clear_memory(chat_id: str) -> None:
    """
    Remove all conversation history for a specific chat session.
    
    LOGIC EXPLANATION (Step-by-step):
    1. Validate that chat_id is a non-empty string
    2. Check if the chat_id exists in the memory store
    3. Delete the conversation history if it exists
    
    Args:
        chat_id (str): Unique identifier for the chat session to clear
        
    Returns:
        None
        
    Edge cases handled:
    - None or empty chat_id: Function returns without doing anything
    - Non-existent chat_id: Function returns without error
    """
    # Edge case: Validate chat_id
    if not chat_id or not isinstance(chat_id, str):
        return
    
    if chat_id in _MEMORY_STORE:
        del _MEMORY_STORE[chat_id]
