from transformers import pipeline

class Analyzer:
    def __init__(self):
        
        self.ai = pipeline("text-classification", model="./ai")
        self.history = []

    def push(self, text):
        res = self.ai(text)[0]
        self.history.append(
            {
                '_': res['label'],
                'score': res['score'],
                'message': text
            }
        )

    def pull(self):
        return self.history[-1]['_']