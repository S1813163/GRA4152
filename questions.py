
"""
Questions

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
#  This module defines a question with multiple choices
#

class ChoiceQuestion(Question):
    ## Constructs a choice question with no choices
    def __init__(self):
        super().__init__()
        self._choices = []
    
    ## Adds an answer choice to this question.
    #  @param choice the choice to add
    #  @param correct True if this is the correct choice, False otherwise
    def addChoice(self, choice, correct):
        self._choices.append(choice)
        if correct:
            # Convert len(choices) to string.
            choiceString = str(len(self._choices))
            self.setAnswer(choiceString)
    
    # Override Question.display()
    def display(self):
        # Display question text
        super().display()
        
        # Display the answer choices.
        for i in range(len(self._choices)):
            choiceNumber = i + 1
            print("%d: %s" % (choiceNumber, self._choices[i]))



class MultiChoiceQuestion(ChoiceQuestion):
    ## Constructs a choice question with no choices
    def __init__(self):
        super().__init__()
        self._answer = []
    
    ## Override setAnswer
    #  Several answers are appended and added to a new instance variable which converts to a string format
    #
    def setAnswer(self, correctResponse):
        self._answer.append(correctResponse)
        self._answers = (' '.join(self._answer))

    ## Override checkAnswer
    #  Uses the new list with multiple answers from setAnswer
    #
    def checkAnswer(self, response):
        return response == self._answers
  
    ## Override Question.display()
    #  Displays helper for providing alternatives
    #
    def display(self):
        # Display question text and explanations on how to answer
        super().display()
        print("Several alternatives might be correct. Provide your answers separated by spaces (e.g. 1 3 4)")
        





