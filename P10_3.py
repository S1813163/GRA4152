"""

Modify the checkAnswer method of the Question class so that it does not take into
account different spaces or upper/lowercase characters. For example, the response
"GUIDO van Rossum" should match an answer of "Guido van Rossum".

"""

##
#  This module defines the Question superclass.
# 

class Question:
    ## Constructs a question with empty question and answer string
    #
    def __init__(self):
        self._text = ""
        self._answer = ""
        
    ## Sets the question text
    #  @param questionText the text of this question
    def setText(self, questionText):
        self._text = questionText
    
    ## Sets the answer for this question. returns the response using lower letters and removes space sensitivity
    #  @param correctResponse the answer
    def setAnswer(self, correctResponse):
        self._answer = correctResponse.replace(" ", "").lower()
        
    ## Check a given response for correctness. returns the response using lower letters and removes space sensitivity
    #  @param the response to check
    #  @return True if the response was correct, False otherwise
    def checkAnswer(self, response):
        return response.replace(" ", "").lower() == self._answer
    
    ## Displays this question
    #
    def display(self):
        print(self._text)

# Does not take into account upper/lowercase characters and number of spaces
# as seen in the reponse variable
q = Question()
q.setText("Who is the inventor of Python?")
q.setAnswer("Guido van Rossum")
q.display()
response = "GUIDO van   RoSsum"
print(q.checkAnswer(response))



