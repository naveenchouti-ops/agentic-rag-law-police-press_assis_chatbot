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
    """Get full conversation memory for a chat"""
    return _MEMORY_STORE.get(chat_id, [])


def add_message(chat_id: str, role: str, content: str) -> None:
    """Add a message to chat memory"""
    if chat_id not in _MEMORY_STORE:
        _MEMORY_STORE[chat_id] = []

    _MEMORY_STORE[chat_id].append({
        "role": role,
        "content": content
    })


def clear_memory(chat_id: str) -> None:
    """Clear memory for a chat"""
    if chat_id in _MEMORY_STORE:
        del _MEMORY_STORE[chat_id]
