# J.A.R.V.I.S. (Just A Rather Very Intelligent System)

J.A.R.V.I.S. is a Django-based voice-activated AI assistant inspired by Iron Man's legendary virtual assistant. It leverages the Groq API (powered by `llama-3.1-8b-instant`) to provide intelligent text and voice responses in both English and Hindi.

---

## 🚀 Key Features

- **Groq LLM Integration:** Powered by `llama-3.1-8b-instant` to deliver fast, contextual, and helpful answers.
- **Bilingual Support:** Automatically responds in English or Hindi depending on the language of your query.
- **Voice Capabilities:**
  - **Speech-to-Text:** Use your microphone to query Jarvis directly using the HTML5 Web Speech Recognition API.
  - **Text-to-Speech:** Jarvis replies speak back to you using the browser's speech synthesis engine.
- **Chat History Logging:** Keeps track of every interaction in a local SQLite database (`ChatHistory` model).
- **Sleek Cyberpunk UI:** Custom dark-themed user interface with signature green glowing aesthetics.

---

## 📁 Project Structure

The project has a nested repository structure. The primary application is located inside the inner `Jarvis` directory:

```text
Jarvis/
│
├── Jarvis/                         # <-- Main Django Application Directory
│   ├── jarvis/                     # Django App containing logic, models, and views
│   │   ├── migrations/
│   │   ├── models.py               # ChatHistory database model
│   │   ├── urls.py
│   │   └── views.py                # Main request logic & Groq API client integration
│   │
│   ├── jarvis_project/             # Django Project Configuration
│   │   ├── settings.py
│   │   └── urls.py
│   │
│   ├── templates/
│   │   └── index.html              # Frontend UI with Speech API integration
│   │
│   ├── .env                        # Local environment credentials (API Key)
│   ├── db.sqlite3                  # Local database
│   └── manage.py                   # Django CLI utility
│
├── venv/                           # Virtual Environment
└── manage.py                       # Outer CLI wrapper
```

---

## 🛠️ Prerequisites & Setup

Follow these steps to set up and run J.A.R.V.I.S. on your local machine:

### 1. Set Up the Virtual Environment
First, ensure you have Python 3.x installed. Navigate to the project root and activate the pre-configured virtual environment:

**On Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**On Windows (CMD):**
```cmd
.\venv\Scripts\activate.bat
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### 2. Install Dependencies
Install the required packages in your active environment:
```bash
pip install django groq python-dotenv
```

### 3. Configure the Environment Variables
Create a `.env` file in the inner `Jarvis/` directory (or modify the existing one) to specify your Groq API Key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## ⚡ Running the Application

Once your virtual environment is active and dependencies are installed, navigate to the directory containing `manage.py` and start the server:

### Run migrations to set up the database:
```bash
python manage.py migrate
```

### Start the development server:
```bash
python manage.py runserver
```

Open your web browser and navigate to `http://127.0.0.1:8000/` to start interacting with Jarvis!

---

## 🗣️ How to Use

1. **Text Inputs:** Type your command in the input bar and press **Enter** or click **Send**.
2. **Voice Command:** Click the **🎤 Mic** button, give permissions to use the microphone, and speak. Jarvis will automatically capture your speech and submit the message.
3. **Voice Response:** Jarvis will read out its response aloud automatically.
