from spy_manager import Spy_Manager
from chat_manager import Chat_Manager
from spy_details import Spy_Details

def login():
    resume = raw_input("1.Continue as Mr. James Bond \n2.New Spy \n3.Exit \n")
    if resume == "1":
        home()
    elif resume=="2":
        spy_detail.name = raw_input("Your Name: ")
        if len(spy_detail.name) > 0:
            spy_detail.salutation = raw_input("Mr. or Ms.: ")
            spy_detail.age = int(raw_input("Your Age: "))
            if spy_detail.age > 12 and spy_detail.age < 50:
                spy_detail.rating = float(raw_input("Spy rating: "))
                home()
            else:
                print "Sorry " + spy_detail.salutation + " " + spy_detail.name + " you are not of the correct age to be a spy"
        else:
            print "Invalid name"
            login()
    elif resume=="3":
        print "Bye"
    else:
        print "Invalid option"
        login()

def home():
    print "Welcome %s %s Age: %d and Rating %0.2f" % (spy_detail.salutation, spy_detail.name, spy_detail.age, spy_detail.rating)
    if spy_detail.rating<=2.5 :
        print "Welcome to Spy chat"
    elif spy.spy_detail.rating>2.5 and spy.spy_detail.rating<4.0:
        print "We are happy to have you back"
    else:
        print "Proud to have you onboard"
    ONLINE = True
    while ONLINE:
        menu = "1. Add a status update \n2. Add a friend \n3. Send a secret message \n4. Read a secret message \n5. Read Chats from a user \n6. Close Application \n"
        choice = raw_input(menu)
        if choice=="1" :
            spy.add_status()
        elif choice=="2":
            no_of_friends=spy.add_friend()
            print "No of Friends: "+str(no_of_friends)
        elif choice=="3":
            chat.send_message()
        elif choice=="4":
            chat.read_message()
        elif choice=="5":
            chat.read_chat_history()
        elif choice=="6" :
            ONLINE=False
        else:
            print "Invalid option"

print "Welcome to Spy Chat"
spy_detail=Spy_Details("James bond", "Mr.", 28, 4.1,"I'm Bond. James Bond.")
spy=Spy_Manager(spy_detail)
chat=Chat_Manager(spy)
login()