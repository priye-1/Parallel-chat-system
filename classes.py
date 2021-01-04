""" User and message classes to control messaging and user operations """
from os import path
from datetime import datetime
import json
import winsound

class User():
    """
    Class to handle all user operations.

    class attributes:
        - username
        - password

    class Methods:
        - save_user()
        - login_user()  
        - confirm_user()
        - view_users()
        - view_online_users() 
        - user_logout()

    """
    def __init__(self, username, password):
        self.username = username
        self.password = password
        

    def save_user(self):
        """
        Class method to save user details in a json file

        """
        username = self.username
        password = self.password
        status = "online"

        #pass user details to a dictionary
        user_dictionary = {'user':username, 'password':password, 'status':status}

        # create file to store value
        value_file =  open("value.txt", "w")

        if path.isfile("users.json") == True :                                      # check if file; users.json exists
            with open("users.json", "r+") as storage_file:
                data = json.load(storage_file)

                #create empty list to append all users
                user_list = []
                for new_data in data['data']:
                    user = new_data['user']
                    user_list.append(user)

                #check for duplicates of username within user_list  
                if self.username in user_list:
                    print("\nUsername already taken, Please Reenter details")

                    #pass value to the main script
                    value_file.write("failed")
                else:
                    value_file.write("successful")

                    #append the  new user to the general user database(data)
                    data['data'].append(user_dictionary)
                    storage_file.seek(0)
                    json.dump(data, storage_file)

                value_file.close()

        else: 
            #pass value to main script
            value_file.write("successful")

            # create and append to a json file when a message is sent. works like a database    
            with open("users.json", "w") as storage_file:
                storage_file.write('{ "data":')
                user_list = [user_dictionary]
                json.dump(user_list, storage_file)
                storage_file.write("}")


    def login_user(self):
        """
        Class method to log in a user

        """
        username = self.username
        password = self.password

        #open file to pass data to main script
        value_file =  open("value.txt", "w")

        if path.isfile("users.json") == True :
            with open("users.json", "r+") as user_file:
                data = json.load(user_file)
                user_file.close()
        
                user_list = []
                password_list = []
                response = []                                                     

                #loop through message to get user and password details
                for new_data in data['data']:
                    user = new_data['user']
                    password1 = new_data['password']
                    user_list.append(user)
                    password_list.append(password)
        
                    # append the value, 1 to the response list if username and password matches an instance in the database
                    if username == user and password == password1:
                        response.append(1)
                        new_data['status'] = "online"                               # change status of user to "online"
                        with open("users.json", "w") as user_file:
                            json.dump(data, user_file)   
                        
                    else:
                        response.append(0)     

                if username in user_list and password in password_list:              # check if username and password entered are in database
                    if 1 in response:                                                # check if username and password entered matches
                        value_file.write("successful")
                    else:
                        value_file.write("failed")    
                else:
                    value_file.write("failed")                                        # file to pass value to the main script           
        else:
            # when user tries to login without signing up
            print("\nNo user is signed up yet")
            value_file.write("failed")  


    def confirm_user(self, receiver):
        """
        Class method for user authentication

        """
        username = self.username
        password = self.password

        #pass value to main script
        value_file =  open("value.txt", "w")

        if path.isfile("users.json") == True :                                              #check if database(users.json) file exists
            with open("users.json", "r+") as user_file:
                data = json.load(user_file)
                user_file.close()
                user_list = []                                                    

                #loop through message to extract all users and append to a list
                for new_data in data['data']:
                    user = new_data['user']
                    user_list.append(user)
        
                if receiver in user_list:                                                   # check if username and password entered are in database
                    value_file.write("successful")  
                else:
                    value_file.write("failed")                
        else:
            print("\nNo user is signed up yet")
            value_file.write("failed")

    def view_users(self):
        """
        Class method to view all users that have created accounts
        
        """
        if path.isfile("users.json") == True :                              
            with open("users.json", "r+") as storage_file:
                data = json.load(storage_file)

                print("\n******All Users:")    
                #loop through message to print usernames
                for new_data in data['data']:
                    user = new_data['user']
                    print(f"---{user}")                
        else:
            print("No users are signed up yet")


    def view_online_users(self):
        """
        Class method to view all users online

        """
        username = self.username

        if path.isfile("users.json") == True :
            with open("users.json", "r+") as storage_file:
                data = json.load(storage_file)

                print("\n******Users currently online:") 
                if len(data['data']) == 1 :                                                 #check if only one user is signed up
                    print("No other user is online")
                else:    
                    #loop through message to print content
                    for new_data in data['data']:
                        if new_data['status'] == "online":                                  # check for users with "online" status
                            if new_data['user'] != username:
                                print(f"---{new_data['user']}")                
        else:
            print("No user is signed up yet")

    def user_logout(self):
        """
        Class method to log out a user by ending the program and changing status to "offline
        
        """
        username = self.username
        with open("users.json", "r+") as user_file:
            data = json.load(user_file)

            #loop through users to get current user
            for new_data in data["data"]:
                user = new_data["user"]
                if username == user:
                    new_data["status"] = "offline"                                      # change online status to offline             
                    user_file.seek(0)
                    json.dump(data, user_file)

    

               


class Message(User):                                                                    # Inheriting from the user class
    """
    Class to handle all user operations.

    class attributes:
        - receiver
        - sender
        - content

    class Methods:
        - save_message()
        - display_sent_message()  
        - view_received_message()
        - view_users_of_sent_message()
        - reply_message()

    """
    def __init__(self, username, receiver, sender, password, content):
        super().__init__(username, password)                                             #calling the parent class (User) attributes
        self.content = content
        self.receiver = receiver
        self.sender = sender
        self.username = username
        self.password = password

    def save_message(self):
        """
        Class method to save messages

        """
        username = self.username
        receiver = self.receiver
        time_ = datetime.now().strftime("%H:%M:%S")                                      # get current time
        content_ = self.content
        sender = self.sender

        # create a dictionary holding the message details
        message_dictionary = {'user':username, 'receiver':receiver, 'sender': sender, 'content':content_, 'time':time_ }

        new_file = f"{username}_{receiver}.json"                                         # create name of the file to mimic a database storing a message
        
        if path.isfile(new_file) == True :                                               # check if the user has sent a message previously
            with open(new_file, "r+") as storage_file:
                data = json.load(storage_file)
                data['data'].append(message_dictionary)                                  # append new message to list
                storage_file.seek(0)
                json.dump(data, storage_file)
                
        else: 
            # create and append to a json file when a message is sent. works like a database    
            with open(new_file, "w") as storage_file:
                storage_file.write('{ "data":')                                           # structure the json file 
                message_list = [message_dictionary]
                json.dump(message_list, storage_file)
                storage_file.write("}")
                frequency = 2500
                duration = 2000
                winsound.Beep(frequency, duration)                                         # create a beep, for 2 seconds
                print("\n*******Message sent")

        
    def display_sent_message(self):
        """
        Class method to display message as soon as they were created
        
        """

        print("\n\n*******************Active Chats**********************")
        print("************************************************************")

        username = self.username
        receiver = self.receiver
        sent_file = f"{username}_{receiver}.json"                                           # create the sent file

        if path.isfile(sent_file) == True:
            with open(sent_file, "r+") as storage_file:
                data = json.load(storage_file)

                #loop through message to print content
                for new_data in data['data']:
                    if new_data['user'] == self.username:
                        message = new_data['content']                                        # get message sent 
                        time_sent = new_data['time']                                         # get time message was sent
                        print(f"\nSent at {time_sent} to {new_data['receiver']}")
                        print(f"Message: {message}")
        else:
            print(f"Invalid response, {receiver} has not sent you any messages")


    def view_received_messages(self):
        """
        Class method to view received messages
        
        """
        username = self.username
        sender = self.sender
        receiver = self.receiver
        
        with open("users.json", "r+") as user_file:
            data = json.load(user_file)

            response = []

            #loop through users to get user names
            for new_data in data["data"]:
                user = new_data["user"]
                filename = f"{user}_{receiver}.json"

                if path.isfile(filename) == True:
                    with open(filename, "r") as chat_file:
                        chats = json.load(chat_file)
                        response.append(1)

                        for chat in chats['data']:                                               #get chat contents
                            message = chat['content']
                            time_sent = chat['time']
                            sender = chat['user']
                            print(f"\nSent at {time_sent} from {sender}")
                            print(f"Message: {message}")
                else:
                    pass  

            if (1 in response):
                pass
            else:
                print("\n*********You have not received any message yet")      
        

    def view_users_of_sent_message(self):
        """
        Class method to view Users to reply
        
        """
        username = self.username
        
        with open("users.json", "r+") as user_file:
            data = json.load(user_file)

        user_list= []
        response = []

         #loop through users to get user names
        for new_data in data["data"]:
            user = new_data["user"]

            #get file name of the stored chat
            filename = f"{user}_{username}.json"

            # check if file name  is already created
            if path.isfile(filename)  == True:
                user_list.append(user)
                response.append(1)
            else:
                response.append(0)

        value_file = open("value.txt", "w")

        if (1 in response):
            # pass value to main script
            value_file.write("successful")
            print("\n**********List of Users to reply:")

            for user in user_list:
                print(f"---{user}")
        else:
            value_file.write("failed")
            print("No messages has been sent to you yet")          


    def reply_message(self):
        """
        Class method to reply messages

        """
        sender = self.sender
        username = self. username
        content = self.content  
        receiver = self.receiver 

        with open("users.json", "r+") as user_file:
            data = json.load(user_file)
        user_list= []

        # get all users
        for new_data in data["data"]:
            user = new_data["user"]
            user_list.append(user)

        #get file name of the stroed chat
        filename = f"{receiver}_{username}.json"

        if sender  in user_list:
            if path.isfile(filename) == True:
                time_ = datetime.now().strftime("%H:%M:%S")                                 # get current time
                
                #saving message
                # create a dictionary holding the message, the user and the time it was sent
                message_dictionary = {'user':username, 'receiver':receiver, 'sender': username, 'content':content, 'time':time_ }

                new_file = f"{username}_{receiver}.json"
                
                if path.isfile(new_file) == True :                                              # check if the user has sent a message previously
                    with open(new_file, "r+") as storage_file:
                        data = json.load(storage_file)
                        data['data'].append(message_dictionary)                                 # append new message to list
                        storage_file.seek(0)
                        json.dump(data, storage_file)
                        
                else: 
                    # create and append to a json file when a message is sent. works like a database    
                    with open(new_file, "w") as storage_file:
                        storage_file.write('{ "data":')
                        message_list = [message_dictionary]
                        json.dump(message_list, storage_file)
                        storage_file.write("}")
                        frequency = 2500
                        duration = 2000
                        winsound.Beep(frequency, duration)                                          # sound notification alarm of 2 seconds          
                        print("\n*******Message sent")


            else:
                print(f"\n{sender} has not sent you any messages")
        else:
            print(f"\nUser is not Signed up!")     
