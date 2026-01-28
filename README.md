# 💎 InsightHub Pro - Enterprise AI Agent System

InsightHub Pro is a high-performance content intelligence platform that orchestrates specialized AI agents using **Google Gemini 2.0** with **Real-time Search Grounding**.

## 🏗️ Clean Architecture
This project follows a **Layered Architecture** (Presentation, Service, Infrastructure) inspired by enterprise Java standards to ensure scalability and decoupling.

- **Presentation (`app/`)**: Streamlit-based UI for real-time interaction.
- **Service Layer (`core/`)**: Business logic orchestration and Pydantic-based data validation.
- **Infrastructure (`providers/`)**: Abstracted API communication layer.

## 🚀 Technical Highlights
- **Multi-Agent Workflow**: Researcher -> Copywriter -> Translator.
- **Data Validation**: Strict DTO implementation using Pydantic.
- **Live Search**: Integrated Google Search Grounding for factual accuracy.

## 🛠️ Installation
```bash
pip install -r requirements.txt
streamlit run app/main.py