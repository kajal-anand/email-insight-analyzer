# 📧 Email Insight Analyzer – Fullstack App (FastAPI + Gemini API)

> **AI-Powered Email Analysis & Intelligence Platform with Backend Processing**

A modern, responsive web application that provides comprehensive email analysis using artificial intelligence (Spam Detection, Summarization, NER), powered by FastAPI and Gemini API. The UI is served via a single `index.html` inside the `static/` folder. Analysis is done via a real backend using FastAPI routes.

---

## ✨ Features

### 🛡️ **Spam Detection**
- **Real AI-based classification** via Gemini API or logic
- **Detects spam intent** with custom response
- **Highlights threat level** and action guidance

### 📝 **Summarization**
- **Shortens long emails** using AI
- **Preserves key insights** while removing fluff

### 🔍 **Named Entity Recognition (NER)**
- **Extracts companies, people, dates**, etc.
- **Highlights entities** from the email text

---

## 🧠 How It Works

### **Frontend** (`index.html` inside `static/`)
- Clean UI built using **HTML, CSS, JavaScript**
- Sends form data to **FastAPI** via `/analyze/` POST route
- Displays backend-generated result on the same page

### **Backend** (FastAPI + AI Logic)
- Uses **FastAPI** to serve both static HTML and `/analyze/` route
- **Gemini API** (or mock AI logic) handles spam/summary/NER
- Response is rendered back using **Jinja2 templating**

---

## 🗂 Project Structure

```
email-insight-analyzer/
├── static/
│   └── index.html             # UI served directly
├── main.py                    # FastAPI backend logic
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

---

## 🔥 Run the App

### **Prerequisites**
- Python 3.8+
- pip package manager

### **Installation & Setup**

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/email-insight-analyzer.git
   cd email-insight-analyzer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the server**
   ```bash
   uvicorn main:app --reload
   ```

4. **Access the application**
   ```
   Visit: http://localhost:8000
   ```

---

## 💻 Usage

### **Step-by-Step**

1. **Open the app** in your browser
2. **Choose one of:**
   - 🛡️ **Spam Detection**
   - 📝 **Summarization**
   - 🔍 **Named Entity Recognition**
3. **Paste your email text**
4. **Click "Analyze Email"**
5. **Get the result** below the form!

### **Example Workflow**

| Step | Action | Result |
|------|--------|---------|
| 1 | Select "Spam Detection" | ✅ Option selected |
| 2 | Paste suspicious email | ✅ Text input filled |
| 3 | Click "Analyze Email" | ✅ Backend processing |
| 4 | View results | ✅ AI analysis displayed |

---

## 🌐 Backend API

### **POST `/analyze/`**
- **Accepts:** `email_text` and `ai_action` from frontend form
- **Returns:** Rendered HTML with the AI result

#### **Example Payload:**
```json
{
  "email_text": "Congratulations! You've won a prize. Click here...",
  "ai_action": "spam"
}
```

#### **Example Response:**
```html
✅ Analysis Result:
🛑 This email appears to be spam.
```

---

## 🎨 UI Behavior (inside `index.html`)

- **All AI processing** is backend-driven
- **No logic on client-side** JS
- **The result is injected** using `{{ result }}` on reload

### **✅ Result Injection**
In `index.html`, this logic dynamically shows AI output:

```html
{% if result %}
<div class="result">
    <h3>✅ Analysis Result:</h3>
    <p>{{ result }}</p>
</div>
{% endif %}
```

The `result` variable is passed by FastAPI during response rendering.

---

## 🛠️ Technical Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | FastAPI | API routes and server |
| **Frontend** | HTML/CSS/JS | User interface |
| **AI Engine** | Gemini API | Text analysis |
| **Templating** | Jinja2 | Dynamic HTML rendering |
| **Server** | Uvicorn | ASGI server |

---

## 🔧 Configuration

### **Environment Variables**
Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_api_key_here
DEBUG=True
HOST=localhost
PORT=8000
```

### **Requirements.txt**
```txt
fastapi
uvicorn
jinja2
python-multipart
google-generativeai
python-dotenv
```

---

## 🚀 Deployment

### **Local Development**
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```


## 🔮 Future Scope

### **Version 2.0 Roadmap**
- [ ] **Integrate actual Gemini API** calls
- [ ] **Expand AI logic** for:
  - Sentiment Analysis
  - Phishing Detection
  - Translation
- [ ] **Add export** as PDF or CSV
- [ ] **User authentication** and session management
- [ ] **Email history** and analytics dashboard

### **Version 3.0 Vision**
- [ ] **Real-time email monitoring**
- [ ] **Batch processing** for multiple emails
- [ ] **Custom AI model training**
- [ ] **Mobile app** companion
- [ ] **Team collaboration** features

---
