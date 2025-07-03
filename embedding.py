from transformers import AutoTokenizer, AutoModel
import torch

# Load a pre-trained Hugging Face model for embeddings
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

# Input text
text = "Eiffel Tower is in Paris and is a famous landmark, it is 324 meters tall"

# Tokenize and get embeddings
inputs = tokenizer(text, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).squeeze()

# Print vector embeddings
print("Vector Embeddings:", embeddings.numpy())
