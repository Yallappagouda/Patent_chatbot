🧠 Semantic Patent Chatbot
A powerful ChatGPT-style semantic patent chatbot built with Streamlit, Sentence Transformers, FAISS, and Google Patent Web Scraping via DuckDuckGo.

This tool enables users to semantically search patents, explore top relevant paragraphs, and handle multi-turn chats with history — all without relying on commercial APIs.

🚀 Features
✅ ChatGPT-like conversational interface

✅ Semantic understanding with Sentence-BERT embeddings

✅ Dual mode search:

Local search via FAISS (offline fast vector search)

Web scraping via DuckDuckGo and Google Patents

✅ Natural year filters, e.g., "blockchain patents after 2019"

✅ Relevance scores with highlighted sections

✅ Multi-turn conversation with history like ChatGPT

✅ User-friendly UI with search bar at the bottom

✅ "No patents found" fallback responses

✅ Modular design with login authentication

✅ No paid APIs required — completely open-source and offline-friendly

📁 Project Structure
bash
Copy
Edit
├── app.py                # Main Streamlit application
├── auth.py               # Handles user signup/login
├── chatbot_model.py      # Loads model, FAISS index, and performs semantic scoring
├── history_manager.py    # Handles session/user chat history
├── data/
│   ├── users.json        # User authentication data
│   └── history/
│       └── user1.json    # Per-user chat histories
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
⚙️ Requirements
Install required Python packages:

bash
Copy
Edit
pip install -r requirements.txt
✅ requirements.txt includes:
nginx
Copy
Edit
streamlit
ddgs
requests
beautifulsoup4
sentence-transformers
torch
💡 How It Works
User enters a query → e.g., "biodegradable packaging after 2019"

Backend Pipeline:

✅ Parse query → extract date filters, categories, etc.

✅ Encode query using SBERT (all-mpnet-base-v2).

✅ Search Locally via FAISS for fast response, or scrape Google Patents via DuckDuckGo.

✅ Extract top semantic matches with highlighted snippets.

✅ Display responses in chat format with chat history.

No matches? → returns friendly fallback messages.

🔐 Authentication System
Supports login/signup via users.json.

Chat history saved per user under data/history/<username>.json.

If not logged in, uses session state only.

🕒 Year Filtering Example
Supports natural language year filtering:

"blockchain in healthcare after 2020"

Automatically filters patents published after 2020.

🛡️ Error Handling
✅ Graceful fallback when no patents are found:

plaintext
Copy
Edit
❌ No patents found after 2020 for this query. Try a different term.
🏃‍♂️ How to Run
bash
Copy
Edit
streamlit run app.py
Visit http://localhost:8501 in your browser.

🌱 Potential Future Improvements
✅ Deploy to Streamlit Cloud / HuggingFace Spaces

✅ Add country/domain filters

✅ PDF previews of patents

✅ Full Elasticsearch pipeline for hybrid search

✅ Voice-based query input

👨‍💻 Authors
Built for Silofortune Hackathon – Data Science Track
Contributors: Yallappagouda Patil and team

📜 License
Licensed under the MIT License — feel free to use, modify, and contribute!
