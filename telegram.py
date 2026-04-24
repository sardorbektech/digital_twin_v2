"""
telegram.py — HR Digital Twin Telegram Bot
Uses: iogram (aiogram v3) — modern async Telegram framework

Install: pip install aiogram python-dotenv langchain-openai langchain

Run: python telegram.py

.env keys needed:
  TELEGRAM_BOT_TOKEN=...
  OPENAI_API_KEY=...
  OPENAI_MODEL=gpt-4o-mini
"""

import asyncio
import logging
import os

from dotenv import load_dotenv

load_dotenv()

from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.markdown import hbold, hcode

from langchain_openai import ChatOpenAI
from langchain_classic.agents import AgentExecutor, create_openai_functions_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

from tools import ALL_TOOLS

# ─────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)

# ─────────────────────────────────────────────
# System prompt — language-aware
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
5. Never expose tool names or implementation details.
6. Keep Telegram responses concise — use bullet points where helpful.
7. End with a short invitation to ask more."""


# ─────────────────────────────────────────────
# Per-user conversation memory
# ─────────────────────────────────────────────
USER_HISTORY: dict[int, list[dict]] = {}
MAX_HISTORY = 20


def get_history(uid: int) -> list[dict]:
    return USER_HISTORY.get(uid, [])


def push_history(uid: int, role: str, content: str):
    if uid not in USER_HISTORY:
        USER_HISTORY[uid] = []
    USER_HISTORY[uid].append({"role": role, "content": content})
    if len(USER_HISTORY[uid]) > MAX_HISTORY:
        USER_HISTORY[uid] = USER_HISTORY[uid][-MAX_HISTORY:]


def clear_history(uid: int):
    USER_HISTORY.pop(uid, None)


def to_lc_messages(history: list[dict]):
    out = []
    for m in history:
        if m["role"] == "user":
            out.append(HumanMessage(content=m["content"]))
        elif m["role"] == "assistant":
            out.append(AIMessage(content=m["content"]))
    return out


# ─────────────────────────────────────────────
# LangChain agent (one per application run)
# ─────────────────────────────────────────────
def build_agent() -> AgentExecutor | None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logger.error("OPENAI_API_KEY not set. Agent disabled.")
        return None

    llm = ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        temperature=0.3,
        openai_api_key=api_key,
        streaming=False,
        max_tokens=1000,
    )
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    agent = create_openai_functions_agent(llm=llm, tools=ALL_TOOLS, prompt=prompt)
    return AgentExecutor(
        agent=agent, tools=ALL_TOOLS,
        verbose=False, handle_parsing_errors=True, max_iterations=5,
    )


AGENT: AgentExecutor | None = build_agent()


# ─────────────────────────────────────────────
# Keyboards
# ─────────────────────────────────────────────
def main_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="👤 About me"),      KeyboardButton(text="💼 Experience")],
            [KeyboardButton(text="🛠️ Skills"),         KeyboardButton(text="📜 Certifications")],
            [KeyboardButton(text="💰 Salary"),         KeyboardButton(text="🚀 Projects")],
            [KeyboardButton(text="📅 Availability"),   KeyboardButton(text="🗑 Reset chat")],
        ],
        resize_keyboard=True,
        one_time_keyboard=False,
    )


# Map button labels → natural-language queries
QUICK_MAP = {
    "👤 About me":         "Tell me about yourself",
    "💼 Experience":       "Describe your work experience",
    "🛠️ Skills":           "What are your main technical skills?",
    "📜 Certifications":   "What certifications do you have?",
    "💰 Salary":           "What are your salary expectations?",
    "🚀 Projects":         "Tell me about your notable projects",
    "📅 Availability":     "Are you available for work and do you prefer remote?",
}


# ─────────────────────────────────────────────
# Router + handlers
# ─────────────────────────────────────────────
router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    clear_history(message.from_user.id)
    await message.answer(
        f"👋 Salom! Men — {hbold('HR Digital Twin')}.\n\n"
        "Menga professional fon haqida savol bering:\n"
        "• Ish tajribasi va loyihalar\n"
        "• Texnik ko'nikmalar\n"
        "• Maosh va bandlik afzalliklari\n"
        "• Sertifikatlar\n\n"
        "Ingliz, o'zbek yoki rus tilida yozing — javob o'sha tilda keladi. 🌐\n\n"
        "Quyidagi tugmalardan foydalaning yoki o'z savolingizni yozing:",
        parse_mode="HTML",
        reply_markup=main_keyboard(),
    )


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "<b>Buyruqlar:</b>\n"
        "/start — Suhbatni qayta boshlash\n"
        "/reset — Tarixni tozalash\n"
        "/about — Bot haqida\n"
        "/help  — Ushbu yordam\n\n"
        "Yoki shunchaki savol yozing!",
        parse_mode="HTML",
    )


@router.message(Command("reset"))
async def cmd_reset(message: Message):
    clear_history(message.from_user.id)
    await message.answer("✅ Suhbat tarixi tozalandi. Yangidan boshlang!")


@router.message(Command("about"))
async def cmd_about(message: Message):
    await message.answer(
        f"🤖 {hbold('HR Digital Twin')}\n\n"
        "LangChain + OpenAI asosida qurilgan.\n"
        "AI o'zi qaysi ma'lumotni chaqirishni hal qiladi.\n\n"
        "Siz ushbu botga HR suhbatlari, intervyular va rekrutment "
        "uchun professional vakil sifatida murojaat qilishingiz mumkin.",
        parse_mode="HTML",
    )


@router.message(F.text == "🗑 Reset chat")
async def btn_reset(message: Message):
    await cmd_reset(message)


@router.message()
async def handle_text(message: Message):
    uid = message.from_user.id
    text = message.text.strip()

    if not text:
        return

    # Map quick-button labels to real queries
    query = QUICK_MAP.get(text, text)

    if not AGENT:
        await message.answer(
            "⚠️ Agent ishlamayapti.\n"
            "OPENAI_API_KEY sozlanmagan. .env faylini tekshiring."
        )
        return

    # Typing indicator
    await message.bot.send_chat_action(message.chat.id, "typing")

    push_history(uid, "user", query)
    history = get_history(uid)

    try:
        result = AGENT.invoke({
            "input": query,
            "chat_history": to_lc_messages(history[:-1]),
        })
        reply = result.get("output", "Javob yaratib bo'lmadi. Qayta urinib ko'ring.")
    except Exception as e:
        logger.exception("Agent error")
        reply = f"⚠️ Xatolik yuz berdi: {e}"

    push_history(uid, "assistant", reply)

    # Telegram 4096-char limit
    if len(reply) <= 4096:
        await message.answer(reply, reply_markup=main_keyboard())
    else:
        for i in range(0, len(reply), 4096):
            await message.answer(reply[i:i + 4096])
        await message.answer("⬆️ Javob yuqorida.", reply_markup=main_keyboard())


# ─────────────────────────────────────────────
# Main entry
# ─────────────────────────────────────────────
async def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN not set in .env")
        return

    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(router)

    logger.info("Digital Twin bot ishga tushdi...")
    await dp.start_polling(bot, drop_pending_updates=True)


if __name__ == "__main__":
    asyncio.run(main())