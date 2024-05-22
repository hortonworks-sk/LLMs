import torch
from transformers import pipeline, BitsAndBytesConfig



class MistralQuestionGenerator

    model_kwargs = { "load_in_4bit" : True, 
                    do_sample=True, 
                    temperature=0.99, 
                    top_k=100}


    '''
    bnb_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_compute_dtype=torch.bfloat16 )
    '''
    
    prompt_prelude = '''[INST]You are an expert user extracting information to quiz people on documentation. You will be passed a page extracted from the documentation.  Write an unnumbered list of 10 questions that can be answered based *solely* on the given text, and include the answer under each question.  Prefix the question with the word question followed by a colon, and 
            prefix the answer with the word answer followed by a colon[/INST]'''



    def __init__(self):

        #self.doc_pickle_path = doc_pickle_path

        self.pipe = pipeline("text-generation", 
                    model="mistralai/Mistral-7B-Instruct-v0.2",
                    max_new_tokens=1000, 
                    model_kwargs)

    def generate_questions(doc_pickle_path, qa_dataset_path):
        
        self.qa_dataset_path = qa_dataset_path

        with open(doc_pickle_path, 'rb') as docpickle:
            docs = pickle.load(docpickle)

            for doc in docs: 

                text = doc.text 
                prompt = prompt_prelude + text
                print("prompt: " + prompt)
                outputs = pipe(prompt, max_new_tokens=1000)

    
    def pickle_to
    
    
    def generate_qa_pairs(chunk): 
        
        prompt = prompt_prelude + text
        print("Prompt: "+ prompt)
        output = pipe(prompt, max_new_tokens=1000)
        
        return output
    
    
    