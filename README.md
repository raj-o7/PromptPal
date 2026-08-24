# PromptPal

An AI chat application with user authentication — built with Flask, SQLAlchemy, and JWT, integrating a third-party AI API to deliver ChatGPT/Gemini-style conversational responses.

**[Live Demo](https://promptpal-wv2f.onrender.com/)** · Backend: Python (Flask) · Frontend: HTML/CSS/JS

---

## Features

- **User authentication** — secure registration and login with hashed passwords (`werkzeug`/`flask_jwt_extended`)
- **JWT-based session handling** — stateless auth via access tokens for protected routes
- **AI-powered chat** — integrates a third-party AI API to generate conversational responses
- **CORS-enabled API** — supports a decoupled frontend making cross-origin requests
- **Environment-based configuration** — secrets and config loaded via `.env` (`python-dotenv`)
- **Persistent storage** — SQLAlchemy ORM with auto-created tables on startup

## Tech Stack

- **Backend:** Python, Flask (application factory pattern), Flask-SQLAlchemy, Flask-JWT-Extended, Flask-CORS
- **Frontend:** HTML, CSS, JavaScript
- **Auth:** JWT (JSON Web Tokens), password hashing
- **Config:** python-dotenv for environment variables

## Project Structure

```
PromptPal/
├── config/          # App configuration
├── instance/        # Instance-specific files (e.g. local DB)
├── logger/          # Logging setup
├── main/            # App factory, models, core logic
│   └── models.py    # User model (registration/auth)
├── app.py           # Entry point — creates app, configures JWT/CORS, runs server
├── routes.py         # Auth routes — /register, /login
├── requirements.txt
└── .env              # (not committed) API keys, JWT secret
```

## API Endpoints

| Method | Endpoint         | Description                          |
|--------|------------------|---------------------------------------|
| POST   | `/register`      | Create a new user account             |
| POST   | `/login`         | Authenticate and receive a JWT token  |

*(Additional chat/AI endpoints — to be documented)*

## Running Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/raj-o7/PromptPal.git
   cd PromptPal
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with:
   ```
   JWT_SECRET_KEY=your_secret_key_here
   # Add your AI API key here
   ```

4. Run the app:
   ```bash
   python3 app.py
   ```
   The server will start at `http://127.0.0.1:5050/`

## Possible Improvements

- Add rate limiting on chat endpoint to prevent API quota abuse
- Move `logs/` out of version control (add to `.gitignore`)
- Add automated tests for auth flow
- Deploy live demo (Render/Railway for backend, Vercel/Netlify for frontend)

---

Built by Rajkumar Singh · [GitHub](https://github.com/raj-o7) · [LinkedIn](https://www.linkedin.com/in/rajkumar-singh-433215248/)
