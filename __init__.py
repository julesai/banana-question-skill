from mycroft import MycroftSkill, intent_file_handler


class BananaQuestion(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('question.banana.intent')
    def handle_question_banana(self, message):
        self.speak_dialog('question.banana')


def create_skill():
    return BananaQuestion()

