import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("college_faq.csv")

# Show first few rows
print("Dataset Preview:\n", data.head())

# Total questions
print("\nTotal Questions:", len(data))

# 🔹 1. Question Length Analysis
data["question_length"] = data["question"].apply(len)

print("\nAverage Question Length:", data["question_length"].mean())

# Plot histogram
plt.figure()
plt.hist(data["question_length"])
plt.title("Question Length Distribution")
plt.xlabel("Length of Question")
plt.ylabel("Frequency")
plt.show()

# 🔹 2. Word Count Analysis
data["word_count"] = data["question"].apply(lambda x: len(x.split()))

print("\nAverage Word Count:", data["word_count"].mean())

plt.figure()
plt.hist(data["word_count"])
plt.title("Word Count Distribution")
plt.xlabel("Number of Words")
plt.ylabel("Frequency")
plt.show()

# 🔹 3. (Optional) Category Analysis
if "category" in data.columns:
    category_counts = data["category"].value_counts()

    print("\nCategory Distribution:\n", category_counts)

    plt.figure()
    category_counts.plot(kind='bar')
    plt.title("Category Distribution")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.show()