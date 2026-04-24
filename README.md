# Digital Twin - AI Representative Platform

A professional AI digital twin system that represents a person in conversations, interviews, and networking scenarios. Features both CLI (main.py) and Streamlit web interface (app.py) implementations.

## Overview

This project creates an intelligent AI avatar that mimics a real person's professional profile, skills, and experience. It uses LangChain and OpenAI's GPT models to provide accurate, context-aware responses about:

- Technical skills and expertise
- Professional certifications
- Work experience and background
- Salary expectations
- Personal information and profile details

## Project Structure

```
Digital Twin/
├── main.py          # CLI-based digital twin (LangChain + OpenAI agent)
├── app.py           # Streamlit web interface
├── tools.py         # Shared tool functions for knowledge retrieval
├── venv/            # Python virtual environment
├── .gitignore       # Git ignore rules
└── README.md        # This file
```

## Features

### Main Features
- **Multi-turn conversation** with context awareness
- **Tool-based responses** for deterministic queries (skills, certifications, etc.)
- **OpenAI GPT fallback** for complex questions
- **Professional tone** maintained throughout interactions
- **Conversation history** preservation
- **Easy reset** functionality

### Supported Query Types
- Skills and technical knowledge
- Desired salary and compensation
- Professional certifications
- Work experience and background
- Personal information and profile

## Installation

### Prerequisites
- Python 3.8 or higher
- pip or conda package manager
- OpenAI API key (for AI-powered responses)

### Setup Steps

1. **Clone or navigate to the project directory:**
   ```powershell
   cd "e:\Projects\Digital Twin"
   ```

2. **Create a virtual environment:**
   ```powershell
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   ```powershell
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1

   # Windows CMD
   venv\Scripts\activate.bat
   ```

4. **Install required dependencies:**
   ```powershell
   pip install langchain langchain-openai langchain-core streamlit openai
   ```

5. **Set up OpenAI API key:**
   ```powershell
   # Option 1: Temporary (current session only)
   $Env:OPENAI_API_KEY = "sk-..."

   # Option 2: Permanent (Windows environment variable)
   setx OPENAI_API_KEY "sk-..."
   ```

## Usage

### CLI Mode (main.py)

Run the command-line interface:

```powershell
python main.py
```

**Commands:**
- Type any question to chat with the AI twin
- Type `quit` to exit
- Type `reset` to clear conversation history

**Example interactions:**
```
You: What are your main skills?
AI Twin: The user has strong expertise in Python, including machine learning frameworks...

You: What's your desired salary?
AI Twin: Desired annual salary: $100,000 – $130,000 USD...

You: Tell me about your experience
AI Twin: Work experience (5 years total)...
```

### Streamlit Mode (app.py)

Launch the web interface:

```powershell
streamlit run app.py
```

The application will:
- Open in your default browser (typically http://localhost:8501)
- Display a user-friendly chat interface
- Show full conversation history
- Provide a "Reset Conversation" button

**Features:**
- Text input field for queries
- Real-time responses
- Conversation history display
- Session state management

## Configuration

### Customizing Digital Twin Profile

Edit `tools.py` to update the digital twin's information:

```python
def get_personal_info(query: str) -> str:
    return (
        "Name: Your Name\n"
        "Location: Your City, Country\n"
        # ... modify other fields
    )
```

Similarly, update other functions for:
- `get_skills_and_knowledge()`
- `get_desired_salary()`
- `get_certifications()`
- `get_experience()`

### Modifying System Prompt

The AI twin's behavior is controlled by the `SYSTEM_PROMPT` in `app.py` (and `main.py`). Customize it to change:
- Personality traits
- Response format
- Professional tone level
- Boundary conditions

## Architecture

### Components

1. **tools.py** - Knowledge base and retrieval functions
   - Keyword-based routing for deterministic responses
   - Fallback mechanism for complex queries

2. **main.py** - LangChain-based CLI agent
   - OpenAI Functions Agent
   - Multi-turn conversation management
   - Command-line interface

3. **app.py** - Streamlit web application
   - Session state management
   - User-friendly chat interface
   - Graceful OpenAI fallback

### Data Flow

```
User Input
    ↓
Tool Router (respond_via_tools)
    ├─→ Match Found: Return Tool Response
    └─→ No Match: Fallback to OpenAI
            ↓
        Build Messages with History
            ↓
        OpenAI GPT Response
            ↓
Display Response + Update History
```

## Requirements

### Python Packages

```
langchain>=0.1.0
langchain-openai>=0.0.1
langchain-core>=0.1.0
streamlit>=1.28.0
openai>=1.0.0
```

Install all at once:
```powershell
pip install -r requirements.txt
```

Or install manually:
```powershell
pip install langchain langchain-openai langchain-core streamlit openai
```

## Troubleshooting

### Issue: "OPENAI_API_KEY not found"
**Solution:** Set your OpenAI API key as an environment variable:
```powershell
$Env:OPENAI_API_KEY = "your-api-key-here"
```

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Solution:** Install the missing package:
```powershell
pip install streamlit
```

### Issue: Virtual environment not activating
**Solution:** Enable PowerShell script execution:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate:
```powershell
.\venv\Scripts\Activate.ps1
```

### Issue: Port 8501 already in use (Streamlit)
**Solution:** Run on a different port:
```powershell
streamlit run app.py --server.port 8502
```

## Development

### Adding New Tool Functions

1. Add a new function to `tools.py`:
   ```python
   def get_new_info(query: str) -> str:
       """Returns new information."""
       return "Your response here"
   ```

2. Update `respond_via_tools()` routing:
   ```python
   if "keyword" in q:
       return get_new_info(query)
   ```

### Testing

Test the CLI mode:
```powershell
python main.py
```

Test the Streamlit app:
```powershell
streamlit run app.py
```

## API Considerations

- **Rate Limits:** OpenAI API has rate limits. Monitor usage on your dashboard.
- **Costs:** API calls incur charges. Track spending at https://platform.openai.com/account/usage
- **Model:** Currently uses `gpt-5.4-nano`. Update model name in code as needed.

## Security

- **Never commit API keys** to version control (use .gitignore)
- **Use environment variables** for sensitive data
- **Validate user inputs** for production use
- **Implement rate limiting** for production deployments

## Performance

- Tool-based responses are instant (no API calls)
- OpenAI responses typically take 1-3 seconds
- Conversation history grows linearly with chat length
- Consider implementing history pruning for long sessions

## Future Enhancements

- [ ] Add voice input/output support
- [ ] Implement conversation export (PDF, JSON)
- [ ] Add database persistence
- [ ] Support multiple languages
- [ ] Implement follow-up question suggestions
- [ ] Add sentiment analysis
- [ ] Create admin dashboard for profile management

## License

This project is provided as-is for educational and professional use.

## Contact & Support

For questions or issues:
1. Check troubleshooting section
2. Review tool configurations
3. Verify OpenAI API key setup
4. Check Python version compatibility (3.8+)

---

**Last Updated:** April 24, 2026
**Version:** 1.0.0
