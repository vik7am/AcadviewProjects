from spy_details import Spy_Details

class Spy_Manager:
    def __init__(self, spy_detail):
        self.spy_detail=spy_detail
        self.friends=[Spy_Details("Akash", "Mr.", 25, 4.8,""),Spy_Details("Jatin", "Mr.", 24, 4.7, ""),Spy_Details("Neha", "Ms.", 22, 4.6, "")]

    def add_status(self):
        print "Your Older status : "+self.spy_detail.status_message
        status_choice = int(raw_input("1.Existing Status \n2.New Status \n"))
        if status_choice == 1:
            position = 1
            for status in self.spy_detail.STATUS_MESSAGES:
                print "%d. %s" % (position, status)
                position = position + 1
            message_choice = int(raw_input(""))
            if message_choice>len(self.spy_detail.STATUS_MESSAGES) :
                print "Invalid Option"
            else:
                self.spy_detail.status_message = self.spy_detail.STATUS_MESSAGES[message_choice - 1]
        elif status_choice == 2:
            custom_status = raw_input("Your new Status: ")
            if len(custom_status) < 0:
                print "Invalid status"
            else:
                self.spy_detail.STATUS_MESSAGES.append(custom_status)
                self.spy_detail.status_message = custom_status
        else:
            print "Invalid Option"
        print "Your Current status : " + self.spy_detail.status_message

    def add_friend(self):
        friend = Spy_Details('', '', 0, 0.0, "")
        friend.name = raw_input("Friend's name: ")
        friend.salutation = raw_input("Mr. or Ms.: ")
        friend.age = int(raw_input("Age: "))
        friend.rating = float(raw_input("Spy rating: "))
        if len(friend.name) > 0 and friend.age > 12 and friend.rating>=self.spy_detail.rating:
            self.friends.append(friend)
            print "Friend Added"
        else:
            print 'Invalid data. Unable to add spy'
        return len(self.friends)

    def select_a_friend(self):
        friend_id = 0
        for friend in self.friends:
            print "%d. %s %s aged %d with rating %.2f is online" % (
                friend_id + 1, friend.salutation, friend.name, friend.age, friend.rating)
            friend_id = friend_id + 1
        choice = raw_input("")
        position = int(choice) - 1
        return position