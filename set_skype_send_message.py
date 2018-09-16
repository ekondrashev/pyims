from skype_send_message import set_send_message

username = input("Type your username of Skype: ")
password = input("Type your password of Skype: ")
retr = input("Type username of Skype for 1-to-1 conversation: ") # the username that receives the sent message
mess = input("Type your message for user of Skype with you want to 1-to-1 conversation: ")

send_message = set_send_message(username, password, retr, mess)
print("\tmessage: " + send_message + '.')
