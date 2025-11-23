# LogicIA - NL ↔ CPC Translator  
**Natural Language ⇄ Classical Propositional Logic**  

[Overview](#overview) • [Features](#features) • [Project-Structure](#project-structure) • [Installation](#installation) • [Frontend-Setup](#frontend-setup-react) • [API](#post-translatenl_to_cpc) • [AI-Logic-And-Convertions](#ai-logic-and-convertions) • [License](#license)

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?style=flat-square&logo=fastapi)
![React](https://img.shields.io/badge/React-18+-blue.svg?style=flat-square&logo=react)
![Status](https://img.shields.io/badge/status-Active-success.svg?style=flat-square)

---

# Overview

LogicIA is an intelligent translator that converts **natural language (NL)** sentences into **Classical Propositional Calculus (CPC)** formulas - and converts CPC back into natural language.

Try the proect! -> 

-------------------------------------------------- https://logic-ia.vercel.app/ -------------------------------------------------

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
- If meanings are missing → **automatically invents cute-animal propositions and retrun respective nl :)**

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
---
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

---
# Frontend Setup (React)

```
cd App
npm install
npm run dev
```
### Your interface will be available at: http://localhost:5173
---
# POST /translate/nl_to_cpc
(photo)
---
# POST /translate/cpc_to_nl
 - If propositions are missing, the backend auto-generates cute-animal statements :)
(photo)
---
# AI Logic and Convertions

### 1. NL → CPC (Natural Language to Classical Propositional Calculus)

- The user provides a sentence in natural language (any language)
- The backend constructs a structured prompt with explicit mapping rules for the AI model.
- The LLM (Gemini) identifies propositions, assigns letters from **A to T**, and applies logical operators based on the mapping rules:
  - `"and" / "e" / "também" / "tambem"` → `∧`
  - `"or" / "ou"` → `v`
  - `"not" / "não" / "nao"` → `¬`
  - `"if ... then"` → `→`
  - `"if and only if" / "se e somente se" / "somente se"` → `↔`
- After interpreting and structuring the logical formula, the model returns a strict JSON object containing:
  - The generated formula  
  - All mapped propositions  
- This JSON is consumed by the frontend and displayed to the user.

---

### 2. CPC → NL (Classical Propositional Calculus to Natural Language)

- The user provides a logical formula using CPC notation. Proposition meanings may be included but are optional.
- The backend sends a prompt instructing the LLM to convert symbols back into natural-language expressions:
  - `∧` → `"and"`
  - `v` → `"or"`
  - `¬` → `"not"`
  - `→` → `"then"`
  - `↔` → `"if and only if"`
- If the user does not provide proposition meanings, the system automatically generates friendly descriptions using “cute animal” themes (e.g., Brownie the rabbit, Lya the cat, Catarina the cat, Sheldon the cat).
- The model returns a JSON object containing:
  - The natural-language translation  
  - The full set of generated or provided propositions  
- The frontend formats and displays the result to the user.

---
# License

### MIT License -free for personal, academic, or commercial use.
