import unittest
import skype_send_message
import keyring


class SkypeSendTextMessageTest(unittest.TestCase):
    """skype_send_message tests"""

    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("setUpClass")
        print("==========")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("==========")
        print("tearDownClass")

    def setUp(self):
        """Set up for test"""
        print("Set up for [" + self.shortDescription() + "]")
        print("password is set ", keyring.set_password("Skype", "nexus12141", "xxxxxxxx"))
        
        
    def tearDown(self):
        """Tear down for test"""
        print("Tear down for [" + self.shortDescription() + "]")
        print("")
        print("password deleted: ", keyring.delete_password("Skype", "nexus12141"))

    def test_send_text_message(self):
        """SEND MESSAGE is SET, TEST"""
        print("id: " + self.id())
        self.assertEqual(skype_send_message.main("Skype", "nexus12141", "nexus12142", "test doc"), "test doc")


if __name__ == '__main__':
    unittest.main()

