# Semantic Patent Chatbot

A powerful **Streamlit-based chatbot** designed to perform **semantic patent searches** using sentence embeddings. This tool helps users find relevant patent abstracts based on natural language queries, with support for user login, personalized chat history, and year-based filtering.

---

## Features

✅ ChatGPT-like interface with semantic understanding  
✅ **Login & signup system** with persistent session handling  
✅ **Patent search powered by DuckDuckGo + Semantic Embeddings**  
✅ Optional **year-based filtering** (e.g., show patents after 2018)  
✅ **Relevance scores** displayed for each result  
✅ **History stored per user** (or in session if not logged in)  
✅ “No patents found” message for unmatched queries  
✅ “Start New Chat” functionality  
✅ Local and offline-friendly with zero commercial APIs

---

## Project Structure

chatbot_app/
│
├── app.py # Main Streamlit app
├── auth.py # Signup/login/session management
├── chatbot_model.py # Loads model and handles semantic scoring
├── history_manager.py # Stores and loads per-user history
├── data/
│ ├── users.json # JSON file of user credentials
│ └── history/
│ └── user1.json # Per-user chat history files
├── requirements.txt # Python dependencies
└── README.md

yaml
Copy code

---

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
🔧 requirements.txt Example
txt
Copy code
streamlit
sentence-transformers
duckduckgo-search
torch
numpy
scikit-learn


🧠 How It Works
User inputs query in natural language.

Chatbot:

Retrieves patent links using DuckDuckGo (via search_patents_duckduckgo).

Extracts key content from links.

Converts both query and content into embeddings using all-MiniLM-L6-v2.

Scores results using cosine similarity.

Top results with highest semantic relevance are returned.

🔐 Authentication
Users can sign up and log in.

If not logged in, searches are stored only for the session.

When logged in:

Chat history is saved to /data/history/<username>.json

Multiple past chats are stored with timestamps

📅 Filtering by Year
Toggle the "Apply Year Filter" option

Set the minimum year (e.g., 2015) to only get newer patents

❗ Error Handling
If no patents are found:

User sees a warning message:

❌ No patents found for your query. Try another search or adjust the filter.

🏁 Running the App
bash
Copy code
streamlit run app.py


✨ Future Improvements
Deploy to Streamlit Cloud or HuggingFace Spaces

Add support for filtering by country or domain

Integrate PDF patent preview

Use FAISS for scalable vector search (for large local patent datasets)

👩‍💻 Developed By
Built for the Silofortune Hackathon – Data Science Track
Contributors: Manasa A S and team

📄 License
This project is licensed under the MIT License.
