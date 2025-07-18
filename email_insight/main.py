from fastapi.staticfiles import StaticFiles
import os

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

# Dynamically get the absolute path to the 'static' directory
current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(current_dir, "static")

# Mount the correct static folder using absolute path
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_home():
    with open(os.path.join(static_dir, "index.html"), encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.post("/analyze", response_class=HTMLResponse)
async def analyze_text(ai_action: str = Form(...), user_text: str = Form(...)):
    if ai_action == "spam":
        result = "🛑 This email appears to be spam."
    elif ai_action == "summary":
        result = "📌 This is a short summary of your input."
    elif ai_action == "ner":
        result = "📍 Named Entities detected: [Company, Date, Person]"
    else:
        result = "❌ Invalid action selected."

    with open(os.path.join(static_dir, "index.html"), encoding="utf-8") as f:
        html_content = f.read()

    # Inject result dynamically (if you're not using templates)
    html_content = html_content.replace("</body>", f"""
        <div class="result">
            <h3>✅ Analysis Result:</h3>
            <p>{result}</p>
        </div>
    </body>""")

    return HTMLResponse(content=html_content)
