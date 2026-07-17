# LearnWise-AI

An AI-powered learning assistant built with Streamlit and the Groq API.

## Features

- 🤖 AI Chatbot
- 📊 Student Dashboard
- 📝 Resume Parser
- 🎯 Course Recommendations
- 🧠 Quiz Generator
- 🗺️ Learning Roadmap
- 👤 User Profile
- 💾 Student Database

## Technologies Used

- Python
- Streamlit
- Groq API
- SQLite
- Pandas
- Matplotlib

## Project Structure

```
LearnWise-AI/
│── app.py
│── requirements.txt
│── students.db
│── .gitignore
│── README.md
└── pages/
    ├── Chatbot.py
    ├── Dashboard.py
    ├── Database.py
    ├── Login.py
    ├── Profile.py
    ├── Quiz.py
    ├── Recommendation.py
    ├── Resume_parser.py
    └── Roadmap.py
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ishikasaxena55/LearnWise-AI.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your Groq API key:

```
GROQ_API_KEY=your_api_key
```

4. Run the application:

```bash
streamlit run app.py
```

## Author

**Ishika Saxena**

GitHub: https://github.com/ishikasaxena55
