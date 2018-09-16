import argparse
from skpy import Skype
parser = argparse.ArgumentParser()
parent_parser = argparse.ArgumentParser(add_help=False)
parent_parser.add_argument('--username', action="store")
parent_parser.add_argument('--password', action="store")
def set_send_message(username, password, retr, mess):
    contact = Skype(username, password)
    contact.user  # you
    contact.contacts  # your contacts
    contact.chats  # your conversations
    message = contact.contacts[retr].chat  # 1-to-1 conversation
    message.sendMsg(mess)
    message.getMsgs()
    all_arg = username + ' ' + password + ' ' + retr + ' ' + mess
    return all_arg.title()
