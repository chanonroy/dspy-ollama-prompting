import dspy

class GenerateAnswer(dspy.Signature):
    """ Answer questions with short factoid answers"""

    context = dspy.InputField(desc="may contain relevant facts")
    question = dspy.InputField()
    answer = dspy.OutputField(desc="often between 1 and 5 words")