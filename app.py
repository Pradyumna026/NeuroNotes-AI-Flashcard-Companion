import streamlit as st
from mistral_llm import generate_flashcards
from utils import extract_text_from_pdf


st.set_page_config(
    page_title="🧠 NeuroNotes – AI Flashcard Companion",
    layout="wide",
    page_icon="🧠"
)

st.markdown("""
    <style>
        html, body {
            background-color: #0f172a;
            color: #f1f5f9;
            font-family: 'Segoe UI', sans-serif;
        }

        .block-container {
            padding: 2rem;
        }

        h1 {
            font-size: 3rem;
            font-weight: bold;
            color: #38bdf8;
            text-align: center;
        }

        h3, h4 {
            color: #facc15;
        }

        .stButton>button, .stDownloadButton>button {
            background-color: #14b8a6;
            color: white;
            font-weight: 600;
            padding: 0.65rem 1.3rem;
            border-radius: 12px;
            border: none;
            transition: background-color 0.3s ease;
        }

        .stButton>button:hover, .stDownloadButton>button:hover {
            background-color: #0f766e;
        }

        .flashcard {
            background-color: #1e293b;
            padding: 1rem;
            margin-bottom: 1rem;
            border-left: 5px solid #14b8a6;
            border-radius: 10px;
        }

        .sidebar .sidebar-content {
            background-color: #1e293b;
        }

        .stSelectbox>div>div {
            background-color: #334155;
            color: #f8fafc;
        }

        hr {
            border-top: 1px solid #334155;
        }

        .error-box {
            background-color: #450a0a;
            color: #fecaca;
            padding: 1rem;
            border-radius: 8px;
        }

        .tip-box {
            background-color: #1f2937;
            padding: 1rem;
            border-left: 4px solid #38bdf8;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown("<h1>🧠 NeuroNotes – AI Flashcard Companion</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Turn any academic PDF into smart, bite-sized flashcards using AI.</p>", unsafe_allow_html=True)
st.markdown("---")


with st.sidebar:
    st.header("⚙️ Generator Settings")
    subject = st.selectbox(
        "**Select Subject Domain**",
        ["General", "Life Sciences", "Physical Sciences", "Engineering", 
         "Humanities", "Business", "Medicine", "Law", "Information Technology"],
        index=0
    )
    st.markdown("---")
    st.info("📎 Upload your study PDF on the right panel to begin.")


st.markdown("### 📘 Upload Your Study Material")
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if st.button("🚀 Generate Smart Flashcards"):
    if uploaded_file:
        with st.spinner("🧠 Thinking... extracting text and generating flashcards..."):
            try:
                content = extract_text_from_pdf(uploaded_file)
                flashcards = generate_flashcards(content, subject)

                st.success("🎉 Flashcards successfully generated!")
                st.markdown("### 📑 Your Generated Flashcards")

                flashcard_list = [card for card in flashcards.split('\n') if card.strip()]
                for i, card in enumerate(flashcard_list, 1):
                    st.markdown(f"<div class='flashcard'><strong>Card #{i}:</strong> {card}</div>", unsafe_allow_html=True)


                st.markdown("---")
                st.markdown("### 💾 Download Options")
                col1, col2 = st.columns(2)
                with col1:
                    st.download_button(
                        "⬇️ Download TXT",
                        data=flashcards,
                        file_name=f"NeuroNotes_{subject}.txt",
                        mime="text/plain"
                    )
                with col2:
                    st.download_button(
                        "⬇️ Download CSV",
                        data="\n".join([f"\"{card}\"" for card in flashcard_list]),
                        file_name=f"NeuroNotes_{subject}.csv",
                        mime="text/csv"
                    )

            except Exception as e:
                st.error("⚠️ Flashcard generation failed.")
                st.markdown(f"<div class='error-box'><strong>Error:</strong> {str(e)}</div>", unsafe_allow_html=True)
                st.markdown("""
                    <div class='tip-box'>
                        <strong>📌 Tips to Resolve:</strong>
                        <ul>
                            <li>Ensure the PDF is not a scanned image (use text-based files).</li>
                            <li>Try uploading a smaller file or just one chapter.</li>
                            <li>Use high-quality academic content.</li>
                        </ul>
                    </div>
                """, unsafe_allow_html=True)
    else:
        st.warning("📤 Please upload a PDF to proceed.")
