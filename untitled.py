import torch
from transformers import pipeline, BitsAndBytesConfig



model_kwargs = { "load_in_4bit" : True }

pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.2", max_new_tokens=1000, do_sample=True, temperature=0.99, top_k=100)