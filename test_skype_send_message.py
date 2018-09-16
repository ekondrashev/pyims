import unittest
import set_skype_send_message
from skype_send_message import set_send_message

class SetSkypeSendMessageTestCase(unittest.TestCase):
    """ TESTS FOR 'SKYPE_SEND_MESSAGE'. """
    def test_retr_mess(self):
        """ TEST MESSAGE """
        send_message = set_send_message('nexus12141', 'Your password', 'nexus12142', 'Hello nexus12142!')
        self.assertEqual(send_message, 'nexus12141, 'Your password', nexus12142, Hello nexus12142!')

unittest.main()
