from transformers import AutoTokenizer, T5ForConditionalGeneration
import torch

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5-base")
model = T5ForConditionalGeneration.from_pretrained("Salesforce/codet5-base")

def correct_code(code_snippet):
    """
    Accepts a string of buggy code and returns the corrected version
    using CodeT5.
    """
    # Prepare input with the prefix to guide the model
    input_text = f"fix: {code_snippet}"
    
    # Tokenize and encode
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    # Generate output
    outputs = model.generate(inputs, max_length=512, num_beams=5, early_stopping=True)

    # Decode and return the result
    corrected_code = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return corrected_code
