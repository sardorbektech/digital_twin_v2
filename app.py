"""
app.py — HR Digital Twin · Streamlit (sodda versiya)
- Oddiy Streamlit UI, JS skriptsiz
- Streaming token-by-token output
- Til aniqlash: UZ/EN/RU javob beradi
"""

import os
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_classic.callbacks.base import BaseCallbackHandler
from langchain_classic.agents import create_openai_functions_agent, AgentExecutor

from tools import ALL_TOOLS

# ─────────────────────────────────────────────
# System prompt
# ─────────────────────────────────────────────
SYSTEM_PROMPT = """You are an AI Digital Twin — a virtual professional representative.
You speak in first person as if you ARE the person being represented.

CRITICAL LANGUAGE RULE:
- Detect the language of the user's message.
- Reply ENTIRELY in that language. Do not mix languages.
- Uzbek in → Uzbek out. Russian in → Russian out. English in → English out.

Core rules:
1. Always use first person ("I", "My" / "Men", "Mening").
2. ALWAYS call a relevant tool before giving a factual answer — never guess.
3. If outside scope, say so and suggest contacting the person directly.
4. Be professional, concise, warm.
5. Never expose tool names or internal details.
6. End with a short invitation to ask more."""

# ─────────────────────────────────────────────
# Page config
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="HR Digital Twin",
    page_icon="🤖",
    layout="centered",
)

# ─────────────────────────────────────────────
# Session state
# ─────────────────────────────────────────────
if "history" not in st.session_state:
    st.session_state.history = []

# ─────────────────────────────────────────────
# Streaming callback
# ─────────────────────────────────────────────
class StreamHandler(BaseCallbackHandler):
    def __init__(self, placeholder):
        self.placeholder = placeholder
        self.text = ""

    def on_llm_new_token(self, token: str, **kwargs):
        self.text += token
        self.placeholder.markdown(self.text + "▌")


# ─────────────────────────────────────────────
# Build agent
# ─────────────────────────────────────────────
@st.cache_resource
def build_agent_config():
    api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")
    return {
        "api_key": api_key,
        "model": os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
    }


def get_agent(stream_handler=None):
    cfg = build_agent_config()
    if not cfg:
        return None
    callbacks = [stream_handler] if stream_handler else []
    llm = ChatOpenAI(
        model=cfg["model"],
        temperature=0.3,
        openai_api_key=cfg["api_key"],
        streaming=True,
        callbacks=callbacks,
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    agent = create_openai_functions_agent(llm=llm, tools=ALL_TOOLS, prompt=prompt)
    return AgentExecutor(
        agent=agent,
        tools=ALL_TOOLS,
        verbose=False,
        handle_parsing_errors=True,
        max_iterations=5,
    )


def history_to_lc(history):
    result = []
    for m in history:
        if m["role"] == "user":
            result.append(HumanMessage(content=m["content"]))
        elif m["role"] == "assistant":
            result.append(AIMessage(content=m["content"]))
    return result


# ─────────────────────────────────────────────
# UI
# ─────────────────────────────────────────────
cfg = build_agent_config()

st.title("🤖 HR Digital Twin")
st.caption(
    f"Model: `{cfg['model']}` · Online ✅" if cfg
    else "⚠️ Offline — `.env` faylida `OPENAI_API_KEY` yo'q"
)
st.divider()

# Starter chips — faqat birinchi ochilganda ko'rsatiladi
if not st.session_state.history:
    st.markdown("**Right here you can ask questions about Sardorbek Odiljonov**")


# Chat tarixi
for msg in st.session_state.history:
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["content"])

# ─────────────────────────────────────────────
# Input va javob
# ─────────────────────────────────────────────
user_input = st.chat_input("Savol bering… / Ask a question… / Задайте вопрос…")

if user_input and user_input.strip():
    user_msg = user_input.strip()
    st.session_state.history.append({"role": "user", "content": user_msg})

    with st.chat_message("user"):
        st.markdown(user_msg)

    with st.chat_message("assistant"):
        if not cfg:
            reply = "⚠️ Agent offline. Iltimos `.env` faylida `OPENAI_API_KEY` ni sozlang."
            st.markdown(reply)
            st.session_state.history.append({"role": "assistant", "content": reply})
        else:
            placeholder = st.empty()
            handler = StreamHandler(placeholder)
            agent_exec = get_agent(stream_handler=handler)
            chat_history_lc = history_to_lc(st.session_state.history[:-1])

            full_reply = ""
            with st.spinner("Javob tayyorlanmoqda…"):
                try:
                    result = agent_exec.invoke({
                        "input": user_msg,
                        "chat_history": chat_history_lc,
                    })
                    full_reply = handler.text.rstrip("▌") or result.get("output", "")
                except Exception as e:
                    full_reply = f"⚠️ Xatolik: {e}"

            placeholder.markdown(full_reply)
            st.session_state.history.append({"role": "assistant", "content": full_reply})

# Suhbatni tozalash
if st.session_state.history:
    st.divider()
    if st.button("🗑️ Clear Chat", type="secondary"):
        st.session_state.history = []
        st.rerun()