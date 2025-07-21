Below is a well-structured **README.md** file for the Semantic Patent Chatbot project based on the provided description. It includes all the key details, setup instructions, and features in a clear, professional format suitable for a GitHub repository or project documentation.

---

# Semantic Patent Chatbot

A powerful ChatGPT-style semantic patent chatbot built with **Streamlit**, **Sentence Transformers**, **FAISS**, and **Google Patent Web Scraping** via **DuckDuckGo**. This tool allows users to semantically search patents, explore top relevant paragraphs, and engage in multi-turn conversations with chat history — all without relying on commercial APIs.

## 🚀 Features
- **ChatGPT-like Conversational Interface**: Intuitive and user-friendly chat experience.
- **Semantic Understanding**: Powered by Sentence-BERT (`all-mpnet-base-v2`) for accurate query understanding.
- **Dual-Mode Search**:
  - **Local Search**: Fast, offline vector search using FAISS.
  - **Web Scraping**: Fetches real-time patent data from Google Patents via DuckDuckGo.
- **Natural Language Year Filters**: Supports queries like "blockchain patents after 2019".
- **Relevance Scoring**: Displays top matches with highlighted relevant sections.
- **Multi-Turn Conversations**: Maintains chat history for seamless interactions.
- **User-Friendly UI**: Search bar at the bottom for easy access.
- **Fallback Responses**: Graceful handling of "No patents found" scenarios.
- **Modular Design**: Includes login authentication for personalized user experience.
- **Open-Source & Offline-Friendly**: No reliance on paid APIs.

## 📁 Project Structure
```
├── app.py                # Main Streamlit application
├── auth.py               # Handles user signup/login
├── chatbot_model.py      # Loads model, FAISS index, and performs semantic scoring
├── history_manager.py    # Manages session/user chat history
├── data/
│   ├── users.json        # Stores user authentication data
│   └── history/
│       └── user1.json    # Per-user chat histories
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## ⚙️ Requirements
To run the project, install the required Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 📋 Dependencies
- `streamlit`
- `ddgs`
- `requests`
- `beautifulsoup4`
- `sentence-transformers`
- `torch`

## 💡 How It Works
1. **User Query**: Enter a query like "biodegradable packaging after 2019".
2. **Backend Pipeline**:
   - Parses query to extract date filters and categories.
   - Encodes query using Sentence-BERT (`all-mpnet-base-v2`).
   - Performs local search via FAISS or scrapes Google Patents via DuckDuckGo.
   - Extracts top semantic matches with highlighted snippets.
   - Displays responses in a chat format with conversation history.
3. **No Matches**: Returns friendly fallback messages like:
   ```
   ❌ No patents found after 2020 for this query. Try a different term.
   ```

## 🔐 Authentication System
- **Login/Signup**: Managed via `users.json`.
- **Chat History**: Saved per user in `data/history/<username>.json`.
- **Guest Mode**: Uses session state for non-logged-in users.

## 🕒 Year Filtering Example
The chatbot supports natural language year filtering. For example:
- Query: "blockchain in healthcare after 2020"
- Result: Filters patents published after 2020.

## 🛡️ Error Handling
- Gracefully handles cases where no patents are found.
- Provides user-friendly feedback for invalid or unmatchable queries.

## 🏃‍♂️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-repo>/semantic-patent-chatbot.git
   ```
2. Navigate to the project directory:
   ```bash
   cd semantic-patent-chatbot
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
5. Open your browser and visit:
   ```
   http://localhost:8501
   ```

## 🌱 Potential Future Improvements
- Deploy to **Streamlit Cloud** or **HuggingFace Spaces**.
- Add filters for country or patent domain.
- Support **PDF previews** of patents.
- Integrate a **full Elasticsearch pipeline** for hybrid search.
- Enable **voice-based query input**.

## 👨‍💻 Authors
Built for the **Silofortune Hackathon – Data Science Track**.  
**Contributors**: Yallappagouda Patil and team.

## 📜 License
This project is licensed under the **MIT License**. Feel free to use, modify, and contribute!

---

This README is concise yet comprehensive, covering all the key points from your description. Let me know if you need any modifications or additional sections!
