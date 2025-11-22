# LogicIA - NL ↔ CPC Translator  
**Natural Language ⇄ Classical Propositional Logic**  
Fully supports **any language** (English, Portuguese, Spanish, etc.)

[Overview](#overview) • [Features](#features) • [Project-Structure](#project-structure) • [Installation](#installation) • [Frontend-Setup](#frontend-setup-react) • [API](#post-translatenl_to_cpc) • [AI-Logic](#-ai-logic) • [License](#license)

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?style=flat-square&logo=fastapi)
![React](https://img.shields.io/badge/React-18+-blue.svg?style=flat-square&logo=react)
![Status](https://img.shields.io/badge/status-Active-success.svg?style=flat-square)

---

# Overview

LogicIA is an intelligent translator that converts **natural language (NL)** sentences into **Classical Propositional Calculus (CPC)** formulas - and converts CPC back into natural language.

It uses:

- **FastAPI (Python)** as backend  
- **Google Gemini 2.5 Flash** for AI-powered translation  
- **Regex fallback logic**  
- **React + Vite** as frontend  

Language support is universal because AI handles the translation layer.

---

# Features

### NL → CPC
- Extracts propositions automatically  
- Generates proposition letters (A–T)  
- Accepts user-provided propositions  
- Detects logical connectors:  

| Natural Language | Symbol |
|------------------|--------|
| and / e / também | ∧ |
| or / ou | v |
| not / não | ¬ |
| if…then / se...então | → |
| if and only if / se e somente se | ↔ |

---

### CPC → NL
- Converts logic symbols into natural-language expressions  
- Generates meaning for each proposition  
- If meanings are missing → **automatically invents cute-animal propositions**:  
  - Brownie (rabbit)  
  - Lya (cat)  
  - Catarina (cat)  
  - Sheldon (cat)

---

# Project Structure
```
LOGICIA/
│
├── App/                          # Frontend (React + Vite)
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   │   ├── css/
│   │   │   ├── box.jsx
│   │   │   └── header.jsx
│   │   ├── pages/
│   │   │   ├── css/style.css
│   │   │   ├── cpc.jsx
│   │   │   ├── home.jsx
│   │   │   ├── introduction.jsx
│   │   │   └── nl.jsx
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   └── vite.config.js
├── home.py                       # Backend routes
├── main.py                       # FastAPI entrypoint
├── schemas.py                    # Pydantic models
├── requirements.txt   
├── README.md                     # This documentation
└── .env
```

# Installation 

### 1️. Clone the repository
```
git clone https://github.com/cauerast/LogicIA.git
cd LogicIA
```

### 2. Create a virtual environment
```
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Configure Environment Variables (.env)
- create .env
```
GEMINI_API_KEY=YOUR_KEY_HERE
```

### 5. Start FastAPI
```
uvicorn main:app --reload
```
### Avaliable at FastAPI → http://localhost:8000/docs


# Frontend Setup (React)

```
cd App
npm install
npm run dev
```
### Your interface will be available at: http://localhost:5173

# POST /translate/nl_to_cpc
(photo)

# POST /translate/cpc_to_nl
(photo)
### If propositions are missing, the backend auto-generates cute-animal statements :)

# AI Logic
### NL → CPC Flow

- Extract propositions
- Clean text
- Assign letters A–T
- Replace operators
- Generate CPC formula
- Return strict JSON only

### CPC → NL Flow
- Interpret propositional letters
- Replace operators
- Auto-generate meanings if missing
- Return strict JSON only

# License

### MIT License -free for personal, academic, or commercial use.