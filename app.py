from classes import User, Message
from os import path

#start program
print("\n\n*************Welcome to A mini Parallel Chat System******************")
print("****************************************************************************")

# receive user input to select operation
choice = input("Login to continue: (yes/no) \nNo account? type (s) to signup\n")                 

while True:
    if choice == "s":

        #get user details
        username = input("\nEnter username to Signup: ")
        password1 = input("Enter password to signup: ")
        password2 = input("Enter password again: ")
        
        # check password
        while password1 != password2:
            print("\nNo Password Match! please try aggain")
            password1 = input("Enter password: ")
            password2 = input("Enter password again: ")

        else:
            # save user to a json file
            new_user = User(username, password1)
            new_user.save_user()

            # pick value from file saved in the class method
            with open("value.txt", "r") as value_file:
                value = value_file.readline()

            if value == "failed":
                continue
            else: 
                print("\n******Signup Successful*********")

        choice = "yes" 

    elif choice == "yes": 

        # proceed to login
        username = input("\nEnter username to login: ")
        password1 = input("Enter password to login: ") 

        # create an object of user class and call the login_user function
        user_login = User(username, password1)
        user_login.login_user()

        # pick value from file saved in the class method
        with open("value.txt", "r") as value_file:
            value = value_file.readline()
            if value == "successful":

                print("\n******Login Successful*********")

                # collect user input for next action    
                choice1 = str(input("\nChoose next action: \n1 >> View all Users\n2 >> View Users Online\n3 >> Send a message \n4 >> View my messages \n5 >> Reply a message \n0 >> Log Out\n"))
                
                while choice != "N":
                    if choice1 == "1":

                        # create an instance of the User class and call the view_users method to display all users
                        new_user = User(username, password1)
                        new_user.view_users()

                        # collect user input for next action
                        choice1 = str(input("\nChoose next action: \n1 >> View all Users\n2 >> View Users Online\n3 >> Send a message \n4 >> View my messages \n5 >> Reply a message\n0 >> Logout\n"))

                    elif choice1 == "2":

                        # create an instance of the User class and call the view_online_users method to display all users online
                        new_user = User(username, password1)
                        new_user.view_online_users()
                        choice1 = str(input("\nChoose next action: \n1 >> View all Users\n2 >> View Users Online\n3 >> Send a message \n4 >> View my messages \n5 >> Reply a message\n0 >> Logout\n"))

                    elif choice1 == "3":
                        receiver = input("Recipient: \n")

                        # confirm entered user is signed up
                        check_recipient = User(username, password1)
                        check_recipient.confirm_user(receiver)

                        # pick value from file saved in the class method
                        confirm_user_file = open("value.txt", "r")
                        confirmed_user = confirm_user_file.readline()

                        # check if recipient is in database
                        if confirmed_user == "successful":
                            content = input("\nEnter message: \n")                                  #get message from user
                            new_message = Message(username, receiver, username, password1, content)
                            new_message.save_message()                                              #save the message
                            new_message.display_sent_message()                                      #display the saved message
                    
                            choice1 = str(input("\nChoose next action: \n1 >> View all Users\n2 >> View Users Online\n3 >> Send a message\n4 >> View my messages \n5 >> Reply a message\n0 >> Logout\n"))

                        else:
                            print("\nUser is not signed up")
                            choice1 = str(input("\nChoose next action: \n1 >> View all Users\n2 >> View Users Online\n3 >> Send a message\n4 >> View my messages \n5 >> Reply a message\n0 >> Logout\n"))

                    elif choice1 == "4":
                        receiver = username

                        # create an instance of the User class and call the view_received_message method to view messages sent to user
                        view_message = Message(username, receiver, username, password1, "sample_content")
                        view_message.view_received_messages()

                        # collect user input for next action
                        choice1 = str(input("\nChoose next action: \n1 >> View all Users\n2 >> View Users Online\n3 >> Send a message\n4 >> View my messages \n5 >> Reply a message\n0 >> Log Out\n"))

                    elif choice1 == "5":
                        sender = username 
                        receiver = "sample"

                        # create an instance of the User class and call the view_received_message method to view messages sent to user
                        reply_messages = Message(username, receiver, username, password1, "sample_content")
                        reply_messages.view_users_of_sent_message()

                        # pick value from file saved in the class method
                        confirm_user_file = open("value.txt", "r")
                        confirmed_user = confirm_user_file.readline()

                        if confirmed_user == "successful":                                          # proceed to reply message
                            receiver = input("\nWho's message are you replying? \n")
                            content = input("Write message: \n")
                            new_message = Message(username, receiver, sender, password1, content)
                            new_message.reply_message()                                             #calling the reply message function
                            new_message.display_sent_message()
                            choice1 = str(input("\nChoose next action: \n1 >> View all Users\n2 >> View Users Online\n3 >> Send a message\n4 >> View my messages \n5 >> Reply a message\n0 >> Log Out\n"))
                        else:

                            # if a user has not been sent a message
                            print("\nNo message to reply")
                            choice1 = str(input("\nChoose next action: \n1 >> View all Users\n2 >> View Users Online\n3 >> Send a message\n4 >> View my messages \n5 >> Reply a message\n0 >> Logout\n"))
                    
                    elif choice1 == "0":
                        new_user = User(username, password1)
                        new_user.user_logout()                                                      #log out user
                        exit() 

                    else:
                        print("\nPlease enter valid response!")
                        choice1 = input("\nChoose next action: \n1 >> View all Users\n2 >> View Users Online\n3 >> Send a message \n4 >> View my messages \n5 >> Reply a message\n0 >> End Program\n\n")
            
            # redirect user to signup if not signed up
            elif value == "failed": 
                print("\n*********You have not signed up or you entered the wrong details? ")
                choice = input("Try to Login again ?: (yes/no) or type (s) to signup\n")
                   
    elif choice == "no":
        # end program
        break

    else:
        # If response entered is not part of the options
        print("\nPlease Enter a valid response.......")
        choice = input("Login to continue: (yes/no) \nNo account? type (s) to signup\n")                 
