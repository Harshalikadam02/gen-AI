from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

# Input prompt
prompt = "What is greater? 9.8 or 9.11"

# Encode the prompt
inputs = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors="pt")

# Generate a response
outputs = model.generate(inputs, max_length=50, pad_token_id=tokenizer.eos_token_id)

# Decode and print the response
reply = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Chatbot Response:", reply)
