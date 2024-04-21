import dspy

class MultiHopQA(dspy.Module):
    def __init__(self):
        self.retrieve = dspy.Retrieve(k=3)
        self.gen_query = dspy.ChainOfThought("context, question -> query")
        self.gen_answer = dspy.ChainOfThought("context, question -> answer")
        self.gen_answer

    def forward(self, question):
        context = []
    
        for hop in range(2):
            query = self.gen_query(context=context, question=question).query
            context += self.retrieve(query).passages

        return self.gen_answer(context=context, question=question)
