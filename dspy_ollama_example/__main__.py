import dspy

ollama_llama3 = dspy.OllamaLocal(model='llama3:latest')

result = ollama_llama3("tell me about interstellar's plot")