# 💎 InsightHub Pro

> **A Professional Multi-Agent AI System powered by Google Gemini 2.0 & Python.**

## 🎯 Project Overview
InsightHub Pro is a sophisticated content intelligence engine that orchestrates specialized AI agents to transform raw topics into verified, high-quality professional content. By utilizing **Real-time Search Grounding**, the system ensures factual accuracy before generating multilingual assets.

## 🏗️ Technical Architecture
The project is built using a **Layered Architecture (SoC)** to ensure that the business logic remains decoupled from the UI and external API providers.

- **Presentation Layer (`app/`)**: A reactive dashboard built with **Streamlit**, designed for real-time user interaction and data visualization.
- **Service Layer (`core/`)**: The "Brain" of the application. It handles agent orchestration, custom exception handling, and strict data validation using **Pydantic DTOs**.
- **Infrastructure Layer (`providers/`)**: A modular adapter for the **Google Gemini API**, allowing for seamless integration and future scalability.

## 🤖 AI Agent Workflow
The system employs a sequential multi-agent chain:
1.  **The Researcher**: Performs deep-dive analysis using Live Search Grounding to gather verified facts.
2.  **The Content Creator**: Transforms technical data into engaging, professional narratives in Romanian.
3.  **The Translator**: Adapts the content for a global audience with high linguistic precision.

## 🚀 Key Features
- **Strict Data Validation**: Every internal data transfer is validated via Pydantic models to ensure system stability.
- **Enterprise-Grade Logging**: Full traceability of agent thoughts and API interactions.
- **Secure Configuration**: Decoupled environment management using `.env` protocols.
- **Modern Python Standards**: Fully compliant with Python 3.12+ conventions and type hinting.

## 🛠️ Tech Stack
- **AI Core**: Google Gemini 2.0 Flash
- **Framework**: Streamlit
- **Validation**: Pydantic v2
- **Environment**: Python-Dotenv
- **Version Control**: Git (Feature-Branch Workflow)

## ⚙️ Installation & Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/MihaiiV/InsightHub_Pro.git](https://github.com/MihaiiV/InsightHub_Pro.git)