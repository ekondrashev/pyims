```
Testing started at 21:34 ...
/home/idumenskyi/work/pycharm/test_pyims_with_main/venv/bin/python /home/idumenskyi/apps/pycharm-2018.1.3/helpers/pycharm/_jb_unittest_runner.py --path /home/idumenskyi/work/pycharm/test_pyims_with_main/test_skype_send_message.py
Launching unittests with arguments python -m unittest /home/idumenskyi/work/pycharm/test_pyims_with_main/test_skype_send_message.py in /home/idumenskyi/work/pycharm/test_pyims_with_main
setUpClass
==========Set up for [PASSWORD is SET, TEST]
id: test_skype_send_message.skype_send_message_test.test_main_with_setting_password
Welcome to 'Skype send message'. 
Type your username of Skype: nexus12141
Type your password of Skype: xxxxxxx
password stored successfully
Type user name of Skype for 1-to-1 conversation: nexus12142
Sending: 
Type your message for user of Skype with you want to 1-to-1 conversation: test 10
messages:  [SkypeTextMsg(id='1537464193651', type='Text', time=datetime.datetime(2018, 9, 20, 17, 23, 13, 647000), clientId='1537464193611', userId='nexus12141', chatId='8:nexus12142', content='test2'), SkypeTextMsg(id='1537464053760', type='Text', time=datetime.datetime(2018, 9, 20, 17, 20, 53, 755000), clientId='1537464053720', userId='nexus12141', chatId='8:nexus12142', content='test 1'), SkypeTextMsg(id='1537463773104', type='Text', time=datetime.datetime(2018, 9, 20, 17, 16, 13, 97000), clientId='1537463773058', userId='nexus12141', chatId='8:nexus12142', content='test f'), SkypeTextMsg(id='1537463650385', type='Text', time=datetime.datetime(2018, 9, 20, 17, 14, 10, 377000), clientId='1537463650336', userId='nexus12141', chatId='8:nexus12142', content='test d'), SkypeTextMsg(id='1537463469791', type='Text', time=datetime.datetime(2018, 9, 20, 17, 11, 9, 766000), clientId='1537463469723', userId='nexus12141', chatId='8:nexus12142', content='tesr b'), SkypeTextMsg(id='1537463323072', type='Text', time=datetime.datetime(2018, 9, 20, 17, 8, 43, 78000), clientId='1537463323037', userId='nexus12141', chatId='8:nexus12142', content='test a'), SkypeTextMsg(id='1537463194836', type='Text', time=datetime.datetime(2018, 9, 20, 17, 6, 34, 824000), clientId='1537463194798', userId='nexus12141', chatId='8:nexus12142', content='testdf'), SkypeTextMsg(id='1537463018695', type='Text', time=datetime.datetime(2018, 9, 20, 17, 3, 38, 151000), clientId='1537463018118', userId='nexus12141', chatId='8:nexus12142', content='testd'), SkypeTextMsg(id='1537431348079', type='Text', time=datetime.datetime(2018, 9, 20, 8, 15, 48, 66000), clientId='1537431348036', userId='nexus12141', chatId='8:nexus12142', content='test'), SkypeTextMsg(id='1537430274389', type='Text', time=datetime.datetime(2018, 9, 20, 7, 57, 54, 357000), clientId='1537430274314', userId='nexus12141', chatId='8:nexus12142', content='fffffffffffffffffffffff')]
Your message is send
Skype nexus12141 xxxxxxx
password deleted:  None
Tear down for [PASSWORD is SET, TEST]



password != None

Expected :None
Actual   :password
 <Click to see difference>

Traceback (most recent call last):
  File "/home/idumenskyi/apps/pycharm-2018.1.3/helpers/pycharm/teamcity/diff_tools.py", line 32, in _patched_equals
    old(self, first, second, msg)
  File "/usr/lib/python3.6/unittest/case.py", line 829, in assertEqual
    assertion_func(first, second, msg=msg)
  File "/usr/lib/python3.6/unittest/case.py", line 822, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: None != 'password'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3.6/unittest/case.py", line 59, in testPartExecutor
    yield
  File "/usr/lib/python3.6/unittest/case.py", line 605, in run
    testMethod()
  File "/home/idumenskyi/work/pycharm/test_pyims_with_main/test_skype_send_message.py", line 34, in test_main_with_setting_password
    self.assertEqual(skype_send_message.main('Skype', 'nexus12141'), 'password')

==========
tearDownClass

Ran 1 test in 44.827s

FAILED (failures=1)

Process finished with exit code 1

```
