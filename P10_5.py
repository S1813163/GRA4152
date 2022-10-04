
"""

Add a class MultiChoiceQuestion to the question hierarchy of Section 10.1 that allows
multiple correct choices. The respondent should provide all correct choices, separated
by spaces. Provide instructions in the question text.

"""

# Import ChoiceQuestion class from working repository (is also uploaded to GitHub)
from questions import ChoiceQuestion

##
#  This module defines a question with multiple choices
#

class MultiChoiceQuestion(ChoiceQuestion):
    ## Constructs a choice question with no choices
    def __init__(self):
        super().__init__()
        self._answer = []
    
    ## Override setAnswer
    #  Several answers are appended and added to a new instance variable which converts to a string format
    #  @param correctResponse the answer
    #
    def setAnswer(self, correctResponse):
        self._answer.append(correctResponse)
        self._answers = (' '.join(self._answer))

    ## Override checkAnswer
    #  Uses the new list with multiple answers from setAnswer
    #  @param response the response to check
    #  @return True if the response was correct, False otherwise
    def checkAnswer(self, response):
        return response == self._answers
  
    ## Override Question.display()
    #  Displays helper for providing alternatives
    #
    def display(self):
        # Display question text and explanations on how to answer
        super().display()
        print("Several alternatives might be correct. Provide your answers separated by spaces (e.g. 1 3 4)")


## Tester program for two different multi-choice questions
def main():
    first = MultiChoiceQuestion()
    first.setText("Which countries are part of Scandinavia?")
    first.addChoice("France", False)
    first.addChoice("Norway", True)
    first.addChoice("Denmark", True)
    first.addChoice("Belgium", False)
    first.addChoice("Sweden", True)
    
    second = MultiChoiceQuestion()
    second.setText("Which two Formula-1 drivers are in Mercedes in 2022?")
    second.addChoice("Lewis Hamilton", True)
    second.addChoice("George Russel", True)
    second.addChoice("Max Verstappen", False)
    second.addChoice("Sergio Perez", False)
    second.addChoice("Valtteri Bottas", False)
    
    presentQuestion(first)
    presentQuestion(second)
    
def presentQuestion(q):
    q.display()
    response = input("Your answer: ")
    print(q.checkAnswer(response))

main()