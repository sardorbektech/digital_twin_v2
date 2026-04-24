"""
tools.py — LangChain-compatible tools for the HR Digital Twin.
Each tool is decorated with @tool so the LangChain agent can decide which to call.
"""

from langchain_classic.tools import tool


# ──────────────────────────────────────────────
# Shaxsiy ma'lumotlar — o'zgartiring
# ──────────────────────────────────────────────
PROFILE = {
    "name": "Sardorbek Odiljonov",
    "location": "Tashkent, Uzbekistan",
    "languages": "English (conversational), Uzbek (native)",
    "education": "B.Sc. Artificial Intelligence Applications and Solutions, third year student, PDP University, 2027",
    "linkedin": "linkedin.com/in/sardorbek-odiljonov-199b08228",
    "github": "github.com/sardorbektech",
    "open_to": "Full-time, Part-time, and Remote-friendly companies.",
    "email": "sardorbektech@gmail.com",
}

EXPERIENCE = [
    {
        "title": "LLM Engineer Intern",
        "company": "Ministry of Economy and Finance of the Republic of Uzbekistan",
        "duration": "6 months",
        "highlights": [
            "Architected and optimized RAG pipelines including data cleaning, embedding generation, and vector DB management.",
            "Implemented rigorous LLM evaluation frameworks using DeepEval and Ragas to measure accuracy, relevance, and latency.",
            "Built autonomous AI agents and automated workflows (Gmail automation, Resume Analyzer) using N8N and LangChain.",
            "Developed and deployed scalable LLM applications utilizing local models via Ollama and cloud-based solutions."
        ],
    }
]

SKILLS = {
    "languages": ["Python", "SQL"],
    "ml_frameworks": ["TensorFlow", "PyTorch", "scikit-learn", "XGBoost", "LightGBM"],
    "llm_ops": ["LangChain", "DeepEval", "Ragas", "Hugging Face Evaluate", "Ollama", "MCP"],
    "gen_ai_techniques": ["Naive RAG", "Advanced RAG", "Graph RAG", "Hybrid RAG", "Fine-tuning (LoRA/QLoRA)", "AI Agents"],
    "cloud": ["AWS (Bedrock, SageMaker, S3)", "GCP", "Azure", "Vercel"],
    "devops_mlops": ["Docker", "GitHub Actions", "MLflow", "Model Observability", "Scalable Deployment"],
    "data_viz": ["Streamlit", "Plotly", "Matplotlib", "Seaborn"],
    "finance_data": ["yfinance", "Pandas TA", "NumPy", "Pandas"],
    "apis": ["FastAPI", "Streamlit", "Telegram Bot API", "AI APIs (OpenAI, Ollama)"],
}

CERTIFICATIONS = [
    "8-Week LLM Engineer Mastery: Generative AI, RAG, and LoRA",
    "Multi-Cloud AI Deployment (AWS, GCP, Azure, Vercel) & MLOps Specialist",
    "Path to AI QA Engineer: Testing LLMs (DeepEval, Ragas, Ollama) - 2026",
    "AI and Data Science"
]

SALARY = {
    "range": "$4,000 - $60,000 USD / year",
    "notes": "Depending on role seniority, remote flexibility, equity, and benefits.",
}

PROJECTS = [
    {
        "name": "Real-Time Stock AI Agent",
        "description": "Intelligent stock analysis assistant combining real-time yfinance data with technical indicators (RSI, Bollinger Bands) for investment insights.",
        "stack": "Streamlit, OpenAI API, yfinance, Plotly, Pandas",
        "outcome": "Automated the generation of actionable trading recommendations through professional interactive visualizations.",
    },
    {
        "name": "Multi-Strategy RAG Engine",
        "description": "FastAPI backend exposing a Q&A (for books) service with four RAG strategies: Naive, Advanced, Graph, and All-in-One.",
        "stack": "FastAPI, LangChain, Graph RAG, Vector DB",
        "outcome": "Enabled real-time, token-by-token streaming for high-concurrency Q&A applications.",
    },
    {
        "name": "HR Digital Twin",
        "description": "LangChain-powered AI agent that represents a professional in interviews/chats.",
        "stack": "LangChain, OpenAI, Streamlit, python-telegram-bot",
        "outcome": "Automates recruiter pre-screening and handles professional inquiries 24/7.",
    },
    {
        "name": "Custom LLM Evaluation",
        "description": "Automated testing suite for domain-specific LLMs using DeepEval.",
        "stack": "Ollama, DeepEval, Python, LLM-as-Judge",
        "outcome": "Established quality benchmarks for local LLM deployments, ensuring 90+ relevance scores.",
    },
]


# ──────────────────────────────────────────────
# LangChain Tools
# ──────────────────────────────────────────────

@tool
def get_personal_info(query: str) -> str:
    """
    Returns general personal and professional profile information:
    name, location, education, contact links, languages, availability.
    Use when someone asks 'who are you', 'tell me about yourself', 'contact info', etc.
    """
    p = PROFILE
    return (
        f"Name: {p['name']}\n"
        f"Location: {p['location']}\n"
        f"Languages: {p['languages']}\n"
        f"Education: {p['education']}\n"
        f"LinkedIn: {p['linkedin']}\n"
        f"GitHub: {p['github']}\n"
        f"Email: {p['email']}\n"
        f"Open to: {p['open_to']}"
    )


@tool
def get_experience(query: str) -> str:
    """
    Returns detailed work experience, employment history, and professional background.
    Use when asked about work history, past jobs, professional experience, or career path.
    """
    lines = [f"Total experience: {sum(int(e['duration'].split()[0]) for e in EXPERIENCE)} years\n"]
    for e in EXPERIENCE:
        lines.append(f"• {e['title']} @ {e['company']} ({e['duration']})")
        for h in e["highlights"]:
            lines.append(f"   – {h}")
    return "\n".join(lines)


@tool
def get_skills(query: str) -> str:
    """
    Returns technical skills, tools, frameworks, and domain expertise.
    Use for questions about programming languages, ML frameworks, cloud platforms,
    data engineering tools, or specific technologies.
    """
    result = []
    for category, items in SKILLS.items():
        label = category.replace("_", " ").title()
        result.append(f"{label}: {', '.join(items)}")
    return "\n".join(result)


@tool
def get_certifications(query: str) -> str:
    """
    Returns professional certifications, completed courses, and credentials.
    Use when asked about certificates, courses, qualifications, or training.
    """
    certs = "\n".join(f"• {c}" for c in CERTIFICATIONS)
    return f"Professional Certifications:\n{certs}"


@tool
def get_salary_expectations(query: str) -> str:
    """
    Returns desired salary range and compensation preferences.
    Use when asked about salary, compensation, pay expectations, or financial requirements.
    """
    s = SALARY
    return (
        f"Desired annual salary: {s['range']}\n"
        f"Notes: {s['notes']}"
    )


@tool
def get_projects(query: str) -> str:
    """
    Returns information about notable projects, portfolio work, and technical achievements.
    Use when asked about projects, portfolio, what was built, technical achievements, or case studies.
    """
    lines = ["Notable Projects:\n"]
    for p in PROJECTS:
        lines.append(f"▸ {p['name']}")
        lines.append(f"  {p['description']}")
        lines.append(f"  Stack: {p['stack']}")
        lines.append(f"  Outcome: {p['outcome']}\n")
    return "\n".join(lines)


@tool
def get_availability_and_preferences(query: str) -> str:
    """
    Returns job preferences, work style, availability, remote work stance, and ideal role.
    Use when asked about availability, start date, remote work, preferred work environment,
    or what kind of role is being sought.
    """
    return (
        "Availability: Ready to start within 2–4 weeks.\n"
        "Work preference: Remote-first or hybrid (max 2 days in-office).\n"
        "Ideal role: Senior ML Engineer or ML Tech Lead at a product-driven company.\n"
        "Industries of interest: FinTech, HealthTech, EdTech, SaaS.\n"
        "Team size preference: 5–50 person engineering teams.\n"
        "Not interested in: full-time on-site roles, pure consulting without ownership."
    )


# Expose all tools as a list for the agent
ALL_TOOLS = [
    get_personal_info,
    get_experience,
    get_skills,
    get_certifications,
    get_salary_expectations,
    get_projects,
    get_availability_and_preferences,
]