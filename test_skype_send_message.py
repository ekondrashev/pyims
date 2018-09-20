import unittest
import skype_send_message



class skype_send_message_test(unittest.TestCase):
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


    def tearDown(self):
        """Tear down for test"""
        print("Tear down for [" + self.shortDescription() + "]")
        print("")

    def test_main_with_setting_password(self):
        """PASSWORD is SET, TEST"""
        print("id: " + self.id())
        self.assertEqual(skype_send_message.main('username', 'password'), 'password')
        #self.assertEqual(skype_send_message.main(username, password), password)  # unresolved reference
        #print("password deleted: ", keyring.delete_password(servicename, username))

    #def test_main(self):
        #"""PASSWORD is NOT SET, TEST"""
        #print("id: " + self.id())
        #self.assertNotEqual(skype_send_message.main("username", "password"), "password")



if __name__ == '__main__':
    unittest.main()
