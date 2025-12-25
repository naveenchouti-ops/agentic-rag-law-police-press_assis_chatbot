## Purpose

This repository contains a small Streamlit-based prototype chatbot that uses the OpenAI Python client. These Copilot instructions capture the project-specific patterns, workflows, and examples that help an AI coding agent be productive quickly.

## Quick overview (big picture)

- **UI**: `prototype/app.py` implements the entire web UI as a Streamlit app (single-file prototype).
- **AI integration**: Uses `OpenAI(api_key=...)` to call `client.chat.completions.create(...)` with `messages` stored in Streamlit `st.session_state`.
- **State model**: `st.session_state` stores `messages` (chat history) and `user_profile`. The first message in `messages` is always the `system` prompt and is replaced on profile changes.

## Important files

- [prototype/app.py](prototype/app.py) — main app; follow its patterns for session state, system prompt replacement, and streaming UI components.

## How to run locally

- Ensure a Python environment with `streamlit` and the OpenAI client installed. Typical packages: `streamlit`, `openai` (or the OpenAI SDK you already use in the repo).
- Provide the OpenAI API key via Streamlit secrets: add `OPENAI_API_KEY` to `~/.streamlit/secrets.toml` or use `st.secrets` in deployment.

Example run command:

```
cd prototype
streamlit run app.py
```

## Project-specific conventions & patterns

- Session-state system message: the app keeps the system prompt at index 0 of `st.session_state['messages']`. Any agent edits to conversation initialization must preserve that index and update only the content, not the message order.
- When modifying how user profile data is used, update both `st.session_state['user_profile']` and the `system_prompt` construction in `prototype/app.py` so the UI and system message remain synchronized.
- UI elements are defined inline (text inputs, radio/selectbox, columns). Follow the existing arrangement when adding or rearranging inputs.
- Model selection: default stored at `st.session_state['openai_model']`. Use that key when adding model toggles.

## Typical change patterns and examples

- Add a new user field: add Streamlit input (e.g., `st.text_input`) and include the value in `st.session_state['user_profile']` and the `system_prompt` string.

Example (pseudo-edit):

```py
# add UI input
location = st.text_input("Location")
# store
st.session_state['user_profile']['location'] = location
# include in system_prompt string
```

- Preserve `messages[0]` as the system message. If you need to alter how messages are constructed, update the logic that sets or replaces `st.session_state['messages'][0]` in `prototype/app.py`.

## External dependencies & integration points

- OpenAI API: calls happen through `client.chat.completions.create(...)` in `prototype/app.py`. Respect the shape of the returned object (`response.choices[0].message.content`) when reading replies.
- Streamlit secrets: `st.secrets['OPENAI_API_KEY']` is the only secret used in the app. CI/deployment must supply this secret.

## Debugging tips

- If the UI shows no responses, confirm `OPENAI_API_KEY` is present and the HTTP client package matches the import (`from openai import OpenAI`).
- To inspect messages, print or log `st.session_state['messages']` temporarily in the UI; changes are lost on rerun unless stored back into session state.

## Tests and CI

- No tests or CI configuration were found. For changes that affect `prototype/app.py`, manually run the Streamlit app locally and exercise key flows: profile update, sending messages, and switching models.

## Safety & rate limits

- Avoid sending extremely long profiles as the `system` prompt; prefer a short summary if token usage becomes a concern. Keep the `system` prompt succinct.

## When to ask the maintainer

- Missing environment details: if you need to change dependency versions or add a requirements file, ask which package manager/version to pin.
- Deployment targets: if you plan to deploy (Streamlit Cloud, Docker, or other), ask how secrets and deployment are handled.

## If you modify this file

- Keep guidance concise and include exact file path examples (like `prototype/app.py`) for any pattern you document.

---
If anything important is missing (dependencies, CI, or secret management approach), tell me which parts are unclear and I will update this file.
