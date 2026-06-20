import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Load model (this may take time first time)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load your dataset
data = pd.read_csv("college_faq.csv")

# Extract questions and answers
questions = data["question"].tolist()
answers = data["answer"].tolist()

# Convert all questions into embeddings (IMPORTANT STEP)
question_embeddings = model.encode(questions, convert_to_tensor=True)

def get_response(user_input):
    # Convert user input into embedding
    user_embedding = model.encode(user_input, convert_to_tensor=True)

    # Compute similarity between user input and all questions
    scores = util.cos_sim(user_embedding, question_embeddings)

    # Get best matching question index
    best_match = scores.argmax()

    # Get confidence score
    confidence = scores[0][best_match]

    print("Confidence:", float(confidence))  # for debugging

    # Decision logic
    if confidence > 0.3:
        return answers[best_match], float(confidence)
    else:
        return "Sorry, I don't have enough information.", float(confidence)