# Parallel-chat-system
This program mimics a client/server model to produce a parallel chat system.
No external module was installed for the development of the system. All library used are python standard libraries.

## Getting started   
### Installation

- Clone repository

    ```bash
     git@github.com:priye-1/Parallel-chat-system.git
    ```

- Setup virtualenvironment with virtualenvwrapper

    ```bash
    mkvirtualenv parallel_chat_system
    ```

- Install requirements

    ```terminal
    # use dev or production requirments depending on location
    pip install -r > requirements.txt
    ```

## Running Scripts
- Start program

    ```terminal
    python app.py
    ```
- Ensure terminal is split into to represent two or more active users for parrallel messaging.    
   
### The system provides the following features:
• User signup and login: The system allows a single user to sign up and then login, without which no further operation can be implemented. Multiple clients can be logged into the system but a client logs in a single user
•	User and Password authentication: After signup, the system stores the data and checks for correlation of username and password during login. 
•	Mini database created and stored as json: The database adopted is used to store user and message details. It is represented as a json file. 
•	Messaging between logged in clients:A client/user logged in has the ability to send messages to other signed up users/clients. The message sent is also displayed to the sender and can be retrieved/view by the recipient.
•	Notification alarm: The system makes use of python’s winsound library to create a beep when a new message or reply is created.
•	Logged messages: The system keeps record of all messages sent or received from a user. This is done with the use of the database represented by json files.
•	User list display: A logged in user has the ability to view all other users that have created an account.
•	Online user list display: A logged in user also has the ability to view all users online
•	Message list display: A logged in user can view all messages sent and received.

## Contributing
Pull requests are welcome. For major changes, 
please open an issue first to discuss what you would like to change.
Make sure you assign the appropriate changelogs.



