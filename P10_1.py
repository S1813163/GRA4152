"""

Add a class NumericQuestion to the question hierarchy of Section 10.1. If the response
and the expected answer differ by no more than 0.01, then accept the response as
correct.

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
    
    ## Sets the answer for this question
    #  @param correctResponse the answer
    def setAnswer(self, correctResponse):
        self._answer = correctResponse
        
    ## Check a given response for correctness.
    #  @param response the response to check
    #  @return True if the response was correct, False otherwise
    def checkAnswer(self, response):
        return response == self._answer
    
    ## Displays this question
    #
    def display(self):
        print(self._text)

##
#  This module defines the NumericQuestion subclass.
#
        
class NumericQuestion(Question):
    # The subclass has its own constructor with empty string question and float answer for numerical questions.
    #
    def __init__(self):
        self._text = ""
        self._answer = float()

    ## Check a given numerical response for correctness with a threshold of +/- 0.01.
    #  @param response the response to check
    #  @return True if the response +/- threshold was correct, False otherwise    
    def checkAnswer(self, response):
        if response >= self._answer-0.01 and response <= self._answer+0.01:
            return True
        else:
            return False

# Tester program
n = NumericQuestion()
n.setText("What is 2+2?")
n.setAnswer(4)    
n.display()
response = float(input("What is your answer? "))
print(n.checkAnswer(response))
