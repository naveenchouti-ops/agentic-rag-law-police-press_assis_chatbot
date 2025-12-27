⚖️ Law Agent  
– Explains IPC, CrPC, and Indian laws  
– Educational purpose only (no legal advice)

🚓 Police Agent  
– FIR process, investigation flow, arrest procedures  
– Procedural and awareness-based explanations

📰 Press Agent  
– News-style reporting  
– Neutral tone with journalistic ethics

🧠 Decide Agent (Decision / Routing Brain)  
– Analyzes user query intent  
– Automatically decides whether Law, Police, or Press agent should respond  
– Does NOT generate answers (decision-only agent)

🤖 Agent Router  
– Executes routing based on Decide Agent output  
– Supports single-agent mode or multi-agent execution

🧠 RAG (Retrieval Augmented Generation)  
– Uses vector databases (Chroma) for factual grounding  
– Domain-wise RAG: Law RAG, Police RAG, Press RAG

💬 Memory  
– Maintains conversation context across turns  
– Improves continuity and follow-up understanding

🧑‍⚖️ Judge Agent (Optional – Advanced)  
– Evaluates responses from Law, Police, and Press agents  
– Selects the safest and most accurate answer  
– Provides confidence score and reasoning

🧪 Voting / Judge Mode  
– Optional multi-agent judgement mode  
– Enterprise-ready Agentic AI pattern




Frontend (React / Chat UI)
        |
        v
FastAPI Backend (main.py)
        |
        v
Decide Agent (decide_agent.py)
        |
        v
Agent Router (agent_router.py)
        |
        +-------------------------------+
        |               |               |
        v               v               v
     Law Agent      Police Agent     Press Agent
        |               |               |
        v               v               v
     Law RAG DB    Police RAG DB    Press RAG DB
        |               |               |
        +---------------+---------------+
                        |
                        v
                Judge Agent (Optional)
                        |
                        v
                  LLM (OpenAI / Local)







AI_project/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   │   ├── agent_law.py
│   │   │   ├── agent_police.py
│   │   │   ├── agent_press.py
│   │   │   ├── agent_router.py
│   │   │   ├── decide_agent.py
│   │   │   └── judge_agent.py  
│   │   │
│   │   ├── services/
│   │   │   ├── rag_retriever.py
│   │   │   ├── openai_client.py
│   │   │   ├── memory_manager.py
│   │   │   └── reflection.py
│   │   │
│   │   └── main.py
│   │
│   ├── data/
│   ├── text/
│   ├── vectordb/
│   └── ingest_*.py
│
├── frontend/
└── README.md


