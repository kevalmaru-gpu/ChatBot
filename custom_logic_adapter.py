from chatterbot.logic import LogicAdapter
import random

class MyLogicAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        return True

    def process(self, statement, additional_response_selection_parameters=None):
        confidence = 0.9

        selected_statement = statement
        selected_statement.confidence = confidence

        return selected_statement