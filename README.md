# GEN-AI  🚀  
 *AI Experiments | Google Gemini | Hugging Face | OpenAI | Internship-Ready Portfolio* 🌸  

---

## ✨ About This Project
Hi, I’m Harshali 👩‍💻 — a Master’s student passionate about **AI/ML development**.  

This repository is my **AI playground** where I experiment with:  
🌐 Google Gemini API, 🤗 Hugging Face Transformers, and OpenAI GPT models.  

💡 It’s built as part of my journey to land an **AI-focused internship** where I can contribute to creating impactful, intelligent systems.  

---

## 🌟 Features
✅ **Google Gemini API Integration** (`gemini-1.5-pro`, `gemini-1.5-flash`)  
✅ **Hugging Face Transformers** for offline inference (e.g., `distilgpt2`)  
✅ **OpenAI GPT APIs** for chat & embeddings  
✅ **Advanced RAG (Retrieval-Augmented Generation)** with multi-vector support  
✅ **Vector Database Integration** (Qdrant) for semantic search  
✅ **Graph Database** (Neo4j) for knowledge graph operations  
✅ **Memory Management** with persistent storage and history  
✅ **Response Caching** to avoid unnecessary API hits & save free-tier quota  
✅ **Docker Compose** for containerized services (Qdrant, Neo4j)  
✅ Environment variables for secure API key management  
✅ Clean, modular codebase ready for production deployment  

---

## 🚀 Tech Stack
- 🐍 Python 3.13
- 🌐 Google Generative AI SDK
- 🤗 Hugging Face Transformers
- 🧠 OpenAI Python SDK
- 🔑 Dotenv for API key security
- 💻 VS Code + GitHub

---

## 📂 Project Structure
GEN-AI COHORT/
├── chat_gemini.py            # Chat with Google Gemini
├── chat.py                   # Chat with OpenAI GPT models
├── embedding.py              # Embedding generation (OpenAI/HF)
├── advanced_rag.py           # Advanced RAG with multi-vector retrieval
├── rag_1.py                  # RAG pipeline implementation
├── mem.py                    # Memory management with persistent storage
├── tokenization.py           # Tokenizer utility scripts
├── weather_agent.py          # Weather API agent (demo)
├── runcommand_agent.py       # Command execution agent
├── ollama_api.py             # Ollama integration for local LLMs
├── docker-compose.yml        # Docker config for Qdrant services
├── docker-compose.graph.yml  # Docker config for Neo4j graph DB
├── requirements.txt          # Python dependencies
├── .env                      # API keys (not tracked in Git)
├── response_cache.json       # Cached API responses
└── README.md                 # Project documentation


---

## � Recent Additions

### 🤖 Advanced RAG System (`advanced_rag.py`)
- Multi-vector retrieval for enhanced context understanding
- Integrates with **Qdrant vector database** for semantic search
- Hybrid retrieval combining sparse and dense vectors
- Production-ready implementation for Q&A systems

### 💾 Memory Management (`mem.py`)
- Persistent memory storage with history tracking
- Session-based memory for context retention
- Integration with mem0 framework for intelligent memory
- Reset and cleanup utilities for session management

### 📊 Graph Database Support (`docker-compose.graph.yml`)
- Neo4j integration for knowledge graph operations
- APOC plugins enabled for advanced graph operations
- Secure authentication and file-based import/export
- Ideal for complex relationship modeling

---

## �🏃‍♀️ Getting Started
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/gen-ai-cohort.git
cd gen-ai-cohort
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Set Up Environment Variables
Create a .env file and add your API keys:

OPENAI_API_KEY=sk-xxxxxx
GEMINI_API_KEY=AIzaSyxxxxxx
4️⃣ Run Example
python chat_gemini.py
🎯 Why This Project?

This isn’t just a test repo — it’s my real-world preparation for AI/ML internships.
Here, I’m learning:

🧠 Large Language Models (LLMs)
🌐 API-driven app development
⚡ Optimization strategies (like caching & token management)
📦 Building production-ready workflows
🏆 Achievements

🌟 Successfully integrated Gemini, Hugging Face, and OpenAI in one cohesive codebase
🌟 Designed with scalability and developer friendliness
🌟 Ready to extend into a full-stack GenAI application

📬 Let’s Connect!

🌐 LinkedIn - https://www.linkedin.com/in/harshali-kadam/
📧 Email: harshalikadam58@gmail.com




