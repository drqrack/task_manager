class Chat:
    # def __init__(self, chatee, last_message, last_message_time):
    #     self.chatee = chatee
    #     self.last_message = last_message
    #     self.last_message_time = last_message_time

    def __init__(self):                                             #runs by itself anytime you try to create an object to the class
        self.chatee = input("Who are you chatting with? \n")
        self.last_message = input("What was your last message? \n")
        self.last_message_time = input("When was the last message sent? \n")

    def __str__(self):                                              #runs by itself anytime you try to print on the console
        return f"You are chatting with {self.chatee}"

    def open(self):
        return f"You just opened the chat with {self.chatee} with last message {self.last_message} that was sent at {self.last_message_time}"