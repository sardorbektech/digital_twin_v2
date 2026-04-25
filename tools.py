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
        "duration": "Avg 2025 - Jun 2026 (6 months)",
        "highlights": [
            "Prepared and structured datasets for Retrieval-Augmented Generation (RAG) workflows, ensuring clean inputs for embedding and retrieval.",
            "Implemented project-specific LLM evaluation pipelines, leveraging models as judges to assess accuracy, relevance, and latency.",
            "Designed automation workflows in N8N, including Gmail classification and a Resume Analyzer tool for HR use cases.",
            "Developed and deployed LLM-powered applications, integrating both local models (via Ollama) and cloud-based solutions depending on project needs.",
        ],
    }
]

SKILLS = {
    "languages": ["Python", "SQL"],
    "ml_frameworks": ["TensorFlow", "PyTorch", "scikit-learn", "XGBoost", "LightGBM"],
    "llm_ops": [
        "LangChain",
        "DeepEval",
        "Ragas",
        "Hugging Face Evaluate",
        "Ollama",
        "MCP",
    ],
    "gen_ai_techniques": [
        "Naive RAG",
        "Advanced RAG",
        "Graph RAG",
        "Hybrid RAG",
        "Fine-tuning (LoRA/QLoRA)",
        "AI Agents",
    ],
    "cloud": ["AWS (Bedrock, SageMaker, S3)", "GCP", "Azure", "Vercel"],
    "devops_mlops": [
        "Docker",
        "GitHub Actions",
        "MLflow",
        "Model Observability",
        "Scalable Deployment",
    ],
    "data_viz": ["Streamlit", "Plotly", "Matplotlib", "Seaborn"],
    "finance_data": ["yfinance", "Pandas TA", "NumPy", "Pandas"],
    "apis": ["FastAPI", "Streamlit", "Telegram Bot API", "AI APIs (OpenAI, Ollama)"],
}

CERTIFICATIONS = [
    "AI Engineer Core Track: LLM Engineering, RAG, QLoRA, Agents",
    "AI Engineer Production Track: Deploy LLMs & Agents at Scale",
    "Path to AI QA Engineer: Testing LLMs (DeepEval, Ragas, Ollama) - 2026",
    "AI and Data Science",
]

SALARY = {
    "notes": "Depending on role seniority, remote flexibility, equity, and benefits.",
}

PROJECTS = [
    {
        "name": "Real-Time Stock AI Agent",
        "description": "Intelligent stock analysis assistant combining real-time yfinance data with technical indicators (RSI, Bollinger Bands) for investment insights.",
        "stack": "Streamlit, OpenAI API, yfinance, Plotly, Pandas",
        "outcome": "Automated the generation of actionable trading recommendations through professional interactive visualizations.",
        "info": """An intelligent AI agent that delivers real-time stock analysis by combining live market data with advanced technical indicators. Built with Streamlit and LangChain, the platform provides actionable trading insights through an interactive dashboard.
        Key Features:

        Live Market Data: Fetches current and historical stock prices using yfinance.

        Technical Analysis: Computes RSI, Moving Averages (20-day, 50-day), Bollinger Bands, and volume trends.

        AI-Powered Recommendations: Uses OpenAI models to interpret signals and generate BUY/SELL/HOLD insights.

        Interactive Dashboard: Dark-themed Streamlit interface with professional Plotly visualizations.

        Multi-Symbol Support: Analyze multiple stocks simultaneously for portfolio-level insights.

        Impact:
        This project demonstrates how multi-tool AI agents can automate financial analysis, offering traders and analysts a professional, user-friendly platform for data-driven investment decisions."""
    },
    {
        "name": "Multi-Strategy RAG Engine",
        "description": "FastAPI backend exposing a Q&A (for books) service with four RAG strategies: Naive, Advanced, Graph, and All-in-One.",
        "stack": "FastAPI, LangChain, Graph RAG, Vector DB",
        "outcome": "Enabled real-time, token-by-token streaming for high-concurrency Q&A applications.",
        "info": """A scalable knowledge-base Q&A platform built with FastAPI, designed to experiment with multiple Retrieval-Augmented Generation (RAG) strategies. The system streams answers token-by-token as newline-delimited JSON (NDJSON), enabling real-time, high-concurrency applications.

        Key Features:

        Multi-RAG Engine: Supports four retrieval strategies — Naive RAG, Advanced RAG, Graph RAG, and Hybrid RAG.

        Backend Architecture: FastAPI service deployed on AWS, with a Next.js frontend for user interaction.

        Streaming Responses: Token-by-token streaming via NDJSON for efficient, low-latency Q&A.

        Flexible Knowledge Base: Designed for book Q&A and adaptable to other domains.

        Cloud-Ready Deployment: Optimized for scalability and integration with modern cloud infrastructure.

        Impact:
        This project demonstrates advanced retrieval engineering and showcases how different RAG strategies can be orchestrated in one system. It highlights practical skills in LLMOps, backend development, and cloud deployment while delivering a professional-grade Q&A service."""
    },
    {
        "name": "Digital Twin",
        "description": "LangChain-powered AI agent that represents a professional in interviews/chats.",
        "stack": "LangChain, OpenAI, Streamlit, python-telegram-bot",
        "outcome": "Automates recruiter pre-screening and handles professional inquiries 24/7.",
        "info": """A professional AI system that acts as a digital twin, representing a person in conversations, interviews, and networking scenarios. The platform provides both a CLI interface (main.py) and a Streamlit web application (app.py) for flexible use.

        Key Features:

        Context-aware representation: Mimics a professional's profile, skills, certifications, and career background.

        Conversational intelligence: Uses LangChain and OpenAI GPT models to deliver accurate, tailored responses.

        Profile integration: Handles queries about technical expertise, work history, salary expectations, and personal details.

        Multi-interface design: Offers both command-line and web-based interaction for different user needs.

        Impact:
        This project demonstrates how AI agents can serve as autonomous professional representatives, capable of handling recruiter pre-screening, networking conversations, and interview simulations. It highlights practical applications of LLM orchestration, agent design, and user-facing deployment."""
    },
    {
        "name": "DB Control AI",
        "description": "Intelligent database query interface that converts natural language prompts into SQL queries and executes them with real-time results.",
        "stack": "Next.js, TypeScript, Tailwind CSS, FastAPI, PostgreSQL",
        "outcome": "Simplified database interaction by enabling non-technical users to query and visualize data through a modern web interface.",
        "info": """An intelligent platform that enables users to query databases using natural language, automatically converting prompts into SQL and executing them with real-time results. The system combines a modern Next.js + TypeScript frontend with a robust FastAPI backend for seamless interaction.

        Key Features:

        Natural Language to SQL: Converts user queries into optimized SQL statements.

        Database Execution: Runs queries against PostgreSQL and other supported databases.

        Interactive Results: Displays outputs in user-friendly tables with query history tracking.

        Error Handling: Provides clear alerts and feedback for invalid queries.

        Multi-Interface Design: Includes both a Next.js web app and a FastAPI backend for flexibility.

        Architecture Highlights:

        Frontend: Next.js, TypeScript, Tailwind CSS, ESLint for type-safe, responsive UI.

        Backend: FastAPI with modular components for query generation, database operations, and API routing.

        Reusable Components: QueryForm, DataTable, SQLViewer, ResultsPanel, Sidebar, and Toast Notifications.

        Impact:
        This project demonstrates how LLM-powered interfaces can simplify database interaction, making complex SQL queries accessible to non-technical users. It highlights skills in full-stack development, database integration, and AI-assisted query generation."""
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
    lines = [
        f"Total experience: {sum(int(e['duration'].split()[0]) for e in EXPERIENCE)} years\n"
    ]
    for e in EXPERIENCE:
        lines.append(f"• {e['title']} @ {e['company']} ({e['duration']})")
        for h in e["highlights"]:
            lines.append(f"   - {h}")
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
    Returns desired salary compensation preferences.
    Use when asked about salary, compensation, pay expectations, or financial requirements.
    """
    s = SALARY
    return f"Desired annual salary:" f"Notes: {s['notes']}"


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
