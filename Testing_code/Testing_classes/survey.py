class AnonymousSurvey:
    def __init__(self, question):
        """Store a question, and prepare to store responses"""
        self.question = question
        self.reponses = []
    
    def show_question(self):
        print(self.question)
    
    def store_response(self, new_response):
        """Adds new response so answer list"""
        self.reponses.append(new_response)
    
    def show_results(self):
        """Shows all stored responses"""
        print("Survey results:")
        for response in self.reponses:
            print(f"- {response}")