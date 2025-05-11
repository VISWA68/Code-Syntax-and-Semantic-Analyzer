from transformers import T5ForConditionalGeneration, RobertaTokenizer
import sys

# Ensure UTF-8 encoding for output
sys.stdout.reconfigure(encoding='utf-8')

model_path = "D:/code_corrector/codet5_model" 
model = T5ForConditionalGeneration.from_pretrained(model_path)
tokenizer = RobertaTokenizer.from_pretrained("Salesforce/codet5-base")

buggy_code = "public static boolean isEmpty(String str) { return str.length() == 0; }"
input_text = "fix: " + buggy_code

inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True, padding="max_length")
outputs = model.generate(**inputs, max_length=512)
fixed_code = tokenizer.decode(outputs[0], skip_special_tokens=True)

fixes = fixed_code.split("public static boolean isEmpty") 
fixes = [f"public static boolean isEmpty{fix.strip()}" for fix in fixes if fix.strip()]  # Re-add signature and clean up

print("🔧 Fixed Code(s):")
for i, fix in enumerate(fixes, 1):
    print(f"Fix {i}:\n{fix}\n")