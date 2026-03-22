import streamlit as st
from src.preprocess import clean_text, get_sentences
from src.summarizer import summarize
from newspaper import Article

st.set_page_config(page_title="SummarizeAI", layout="wide")

# ---------- HEADER ----------
st.markdown("""
<h1 style='text-align:center;'>SummarizeAI</h1>
<p style='text-align:center;color:gray;'>Smart AI News Summarizer</p>
""", unsafe_allow_html=True)

# ---------- INPUT MODE ----------
option = st.radio("Choose Input Type", ["Paste Text", "Paste URL"])

text_input = ""

if option == "Paste Text":
    text_input = st.text_area("Paste your article here", height=300)

else:
    url = st.text_input("Enter article URL")

    if url:
        try:
            article = Article(url)
            article.download()
            article.parse()
            text_input = article.text
            st.success("Article fetched successfully!")
        except:
            st.error("Failed to fetch article")

# ---------- SUMMARY LENGTH ----------
length = st.select_slider(
    "Summary Length",
    options=["Short", "Medium", "Long"]
)

length_map = {
    "Short": 2,
    "Medium": 3,
    "Long": 5
}

# ---------- GENERATE ----------
if st.button("Generate Summary"):

    if text_input.strip() == "":
        st.warning("Please enter article or URL")
    
    else:
        with st.spinner("Analyzing content..."):

            text = clean_text(text_input)
            sentences = get_sentences(text)

            summary = summarize(
                text,
                sentences,
                num_sentences=length_map[length]
            )

        st.subheader("Summary")

        full_summary = ""

        for line in summary:
            st.write("•", line)
            full_summary += line + "\n"

        # ---------- COPY FEATURE ----------
        st.text_area("Copy Summary", value=full_summary, height=150)

        st.success("Summary generated successfully!")