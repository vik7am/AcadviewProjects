from spy_details import Chat_Message
from steganography.steganography import Steganography
from termcolor import colored

class Chat_Manager:

    def __init__(self, spy):
        self.spy=spy

    def send_message(self):
        friend_id = self.spy.select_a_friend()
        if friend_id>=len(self.spy.friends):
            print "Invalid option"
            return
        input_image = raw_input("Name of the image: ")
        message = raw_input("Your Message: ")
        Steganography.encode(input_image, "output.jpg", message)
        chat = Chat_Message(message, True)
        self.spy.friends[friend_id].chats.append(chat)
        print "Message Encoded Successfully"
        print "Image Name:output.jpg"

    def read_message(self):
        friend_id = self.spy.select_a_friend()
        if friend_id >= len(self.spy.friends):
            print "Invalid option"
            return
        output_image = raw_input("What is the name of the file?")
        try:
            message = Steganography.decode(output_image)
        except:
            print "Image does not contain any message"
            return
        if self.verify_message(message, friend_id):
            chat = Chat_Message(message, False)

            self.spy.friends[friend_id].chats.append(chat)
            print "Message Decoded Successfully"
        else:
            print "Message Decoding Failed"

    def read_chat_history(self):
        friend_id = self.spy.select_a_friend()
        if friend_id >= len(self.spy.friends):
            print "Invalid option"
            return
        for chat in self.spy.friends[friend_id].chats:
            if chat.sent_by_me:
                print "[%s] %s : %s" % (colored(chat.time.strftime("%d %B %Y"),"blue"), colored("You", "red"),  chat.message)
            else:
                print "[%s] %s : %s" % (colored(chat.time.strftime("%d %B %Y"),"blue"), colored(self.spy.friends[friend_id].name, "red"), chat.message)

    def verify_message(self, message, friend_id):
        if len(message)>100 :
            print "Your Friend %s %s is removed due to spamming" %(self.spy.friends[friend_id].salutation, self.spy.friends[friend_id].name)
            self.spy.friends.pop(friend_id)
            return False
        elif message=="SOS":
            print "Save Our Ship"
        elif message=="SAVE ME":
            print "Hey save me I'm in Danger"
        elif message=="HELP ME":
            print "I need Help as soon as possible"
        return True