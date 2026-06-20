import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from chatbot import get_response

st.title("CollegeMate 🎓")

# User input
user_input = st.text_input("Ask your question")

if user_input:
    response, confidence = get_response(user_input)

    st.write("### 🤖 Answer:")
    st.write(response)

    st.write("### 📊 Confidence Score:")
    st.write(round(confidence, 2))

    # Confidence bar chart
    st.bar_chart([confidence])

# -------- DATA ANALYSIS SECTION --------

st.header("📊 Data Insights")

data = pd.read_csv("college_faq.csv")

# Question length
data["question_length"] = data["question"].apply(len)

st.subheader("Question Length Distribution")
fig1 = plt.figure()
plt.hist(data["question_length"])
plt.xlabel("Length")
plt.ylabel("Frequency")
st.pyplot(fig1)

# Word count
data["word_count"] = data["question"].apply(lambda x: len(x.split()))

st.subheader("Word Count Distribution")
fig2 = plt.figure()
plt.hist(data["word_count"])
plt.xlabel("Words")
plt.ylabel("Frequency")
st.pyplot(fig2)
    