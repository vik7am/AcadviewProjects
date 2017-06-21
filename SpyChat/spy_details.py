from datetime import datetime
class Spy_Details:

    def __init__(self, name, salutation, age, rating, status):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.online = True
        self.chats = []
        self.status_message = status
        self.STATUS_MESSAGES = ["I'm Bond. James Bond.", "[]--007--[]","The World Is Not Enough"]

class Chat_Message:

    def __init__(self,message,sent_by_me):

        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me