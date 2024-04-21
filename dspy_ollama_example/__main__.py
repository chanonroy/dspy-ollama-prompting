import dspy
from TextExtraction import FindTerms

llama3 = dspy.OllamaLocal(model='llama3:latest')

dspy.settings.configure(lm=llama3)

module = FindTerms()
response = module("Their jaws and wallets will drop to the floor. Watch out for the godfather.")
print(response)    
