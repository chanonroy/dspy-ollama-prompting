import dspy

class Terms(dspy.Signature):
    """
    List of extracted entities
    """
    prompt = dspy.InputField()
    terms = dspy.OutputField(format=list)


class FindTerms(dspy.Module):
    """
    Extract movie titles from a question
    """
    def __init__(self):
        super().__init__()
        self.entity_extractor = dspy.Predict(Terms)

    def forward(self, question):
        max_num_terms = max(1, len(question.split())//4)
        instruction = f"Identify up to {max_num_terms} terms in the following question that are famous movie names."
        prediction = self.entity_extractor(
            prompt=f"{instruction}\n{question}"
        )
        return prediction.terms  