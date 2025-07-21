import streamlit as st
from sentence_transformers import SentenceTransformer, util
import torch
from auth import login, signup, save_history, get_history
from ddgs import DDGS
import requests
from bs4 import BeautifulSoup
import json
import os
import re
import random

# ------------------- Config -------------------
st.set_page_config(page_title="Live Semantic Patent Chatbot", layout="wide")
USERS_FILE = "users.json"
SESSION_FILE = "session.json"

# ------------------- Reset session -------------------
if 'initialized' not in st.session_state:
    st.session_state.clear()
    st.session_state.initialized = True

# ------------------- Session Handling -------------------
def save_session(email):
    with open(SESSION_FILE, "w") as f:
        json.dump({"email": email}, f)

def load_session():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "r") as f:
            data = json.load(f)
            return data.get("email")
    return None

def clear_session():
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)

# ------------------- Load SBERT -------------------
@st.cache_resource
def load_model():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    model.max_seq_length = 512
    return model

model = load_model()

# ------------------- DuckDuckGo Search -------------------
def search_patents_duckduckgo(query, num_results=8, year_filter=None):
    links = []
    with DDGS() as ddgs:
        results = ddgs.text(f"{query} site:patents.google.com", max_results=30)
        for r in results:
            href = r['href']
            match = re.search(r'/patent/([A-Z]{2})(\d{4})(\d+)', href)
            if year_filter:
                if match:
                    y = int(match.group(2))
                    if y != year_filter:
                        continue
            if "patents.google.com" in href:
                links.append(href)
            if len(links) >= num_results:
                break
    return links

# ------------------- Extract & Format Patent Info -------------------
def extract_patent_info(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        res = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')

        # Patent number
        title_tag = soup.find("meta", property="og:title") or soup.find("title")
        if title_tag:
            full_title = title_tag["content"] if title_tag.has_attr("content") else title_tag.text
            patent_number = full_title.split(" - ")[0].strip()
        else:
            patent_number = "Unknown Patent"

        # Format
        match = re.search(r'([A-Z]{2})\s?(\d{4})/(\d+)\s?(A\d?)?', patent_number)
        if match:
            country, year, pid, a_code = match.groups()
            formatted_patent = f"{country or 'US'} {year or '2023'}/{pid or '0000000'} {a_code or 'A1'}"
        else:
            formatted_patent = patent_number

        # Abstract or first paragraph
        abstract_tag = soup.find('meta', {'name': 'DC.description'})
        abstract = abstract_tag['content'].strip() if abstract_tag else ""

        paragraphs = soup.find_all("div", {"class": "description-line"})
        sample_text = ""
        for p in paragraphs:
            text = p.get_text().strip()
            if len(text) > 100:
                sample_text = text
                break

        if not sample_text:
            sample_text = abstract or "Description not found."

        section_id = f"{random.randint(30, 99):04d}"
        result_text = f"{formatted_patent} — Section §[{section_id}]: {sample_text[:300]}{'…' if len(sample_text) > 300 else ''}"
        return result_text, sample_text, url

    except Exception as e:
        return f"Error: {str(e)}", "", url

# ------------------- Sidebar -------------------
with st.sidebar:
    st.markdown("### 🧾 Options")
    if st.button("🔄 Start New Chat"):
        st.session_state.chat_history = []

    st.markdown("### 🔐 Login / Signup")
    if 'email' not in st.session_state:
        st.session_state.email = load_session()

    if st.session_state.email:
        st.success(f"Logged in as {st.session_state.email}")

        st.markdown("### 📁 Previous Searches")
        user_history = get_history(st.session_state.email)
        for i, entry in enumerate(user_history):
            if st.button(f"{entry['query']}", key=f"history_{i}"):
                st.session_state.chat_history = []
                st.session_state.chat_history.append({"user": entry['query']})
                st.session_state.chat_history.append({"bot": entry['results']})

        if st.button("🔒 Logout"):
            st.session_state.email = None
            st.session_state.chat_history = []
            clear_session()
    else:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Login"):
                if login(email, password):
                    st.success("Login successful!")
                    st.session_state.email = email
                    save_session(email)
                else:
                    st.error("Invalid credentials")
        with col2:
            if st.button("Signup"):
                if signup(email, password):
                    st.success("Signup successful! You can now log in.")
                else:
                    st.error("Email already exists")

# ------------------- Main UI -------------------
st.title("🔍 Deep Semantic Patent-Search Chatbot")
st.markdown("Enter a natural language query. It will semantically match Google Patents in real-time.")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    query = st.text_input("Your Query:", placeholder="e.g., biodegradable rice-based edible straws")

with col2:
    enable_year_filter = st.checkbox("Enable Year Filter")

with col3:
    if enable_year_filter:
        year = st.number_input("Year", min_value=2000, max_value=2025, value=2023, step=1)
    else:
        year = None

if st.button("Search") and query:
    st.session_state.chat_history.append({"user": query})
    with st.spinner("🔎 Searching and analyzing..."):
        urls = search_patents_duckduckgo(query, num_results=8, year_filter=year)

        if not urls:
            st.warning(" No patents found for this query and filter.")
            st.session_state.chat_history.append({"bot": []})
        else:
            raw_results = []
            for url in urls:
                result_text, raw_text, link = extract_patent_info(url)
                if raw_text:
                    raw_results.append((result_text, raw_text, link))

            if not raw_results:
                st.warning(" No valid abstracts or descriptions were found.")
                st.session_state.chat_history.append({"bot": []})
            else:
                query_embedding = model.encode(query, convert_to_tensor=True, normalize_embeddings=True)
                scored_results = []
                for result_text, raw_text, link in raw_results:
                    result_embedding = model.encode(raw_text, convert_to_tensor=True, normalize_embeddings=True)
                    score = util.cos_sim(query_embedding, result_embedding).item()
                    scored_results.append((score, result_text, link))

                top_results = sorted(scored_results, key=lambda x: x[0], reverse=True)[:5]
                st.session_state.chat_history.append({"bot": top_results})

                if st.session_state.email:
                    save_history(st.session_state.email, {"query": query, "results": top_results})

# ------------------- Chat Display -------------------
for turn in st.session_state.chat_history:
    if 'user' in turn:
        st.markdown(f"🧑 **You:** **{turn['user']}**")
    elif 'bot' in turn:
        if not turn['bot']:
            st.markdown("🤖 **Bot:** No matching patents found.")
        else:
            st.markdown("🤖 **Bot (most relevant results first):**")
            for score, text, link in turn['bot']:
                st.markdown("---")
                st.markdown(f"**Relevance Score:** `{score:.4f}`")
                st.markdown(f"**Extracted Info:** {text}")
                st.markdown(f"[🔗 View Full Patent]({link})")
