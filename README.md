# NeuroNotes • AI Flashcard Companion 🧠

NeuroNotes is a lightweight AI-powered flashcard app designed to streamline learning using spaced repetition and natural language processing. Built with Python and leveraging the Mistral LLM, it helps you generate, review, and retain knowledge more effectively.

DEMO: 

![Screenshot 2025-06-17 204608](https://github.com/user-attachments/assets/880cd12b-c191-4c58-aec6-580c696953a3)

![Screenshot 2025-06-17 204745](https://github.com/user-attachments/assets/10c68282-3367-4539-addf-2b7ed743373b)

## 🔍 Features

- **Flashcard generation**: Convert study notes into question-answer flashcards using AI.
- **Spaced repetition review**: Track what you've learned and prioritize cards intelligently.
- **Customizable options**: Configure study frequency, card formats, and data storage.

## ⚙️ Tech Stack

- **Python 3.8+**
- **Mistral LLM** via `mistral_llm.py`
- **Key modules**:
  - `app.py` – main CLI and orchestration
  - `utils.py` – helper functions for flashcard creation, storage, and evaluation
- **Dependencies** listed in `requirements.txt`

## 🚀 Getting Started

### 1. Clone the project

```bash
git clone https://github.com/Pradyumna026/NeuroNotes-AI-Flashcard-Companion.git
cd NeuroNotes-AI-Flashcard-Companion

2. Install dependencies
    pip install -r requirements.txt

3. Configure your LLM
Ensure API credentials (e.g., for Mistral) are configured in your environment or a .env file. Refer to mistral_llm.py for expected variables (e.g., MISTRAL_API_KEY).

4. Launch the app
   streamlit run app.py

🗂️ File Structure

 NeuroNotes-AI-Flashcard-Companion/
├── app.py             # CLI entry point
├── mistral_llm.py     # LLM interaction logic
├── utils.py           # Data processing and flashcard logic
├── requirements.txt   # Python dependencies
└── README.md          # This documentation

7.🧑‍💻 Author

Pradyumna
📧 [pradyumnasingh781@gmail.com]


