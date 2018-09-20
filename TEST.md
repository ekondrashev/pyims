```
Testing started at 11:04 ...
/home/idumenskyi/work/pycharm/test_pyims_with_main/venv/bin/python /home/idumenskyi/apps/pycharm-2018.1.3/helpers/pycharm/_jb_unittest_runner.py --path /home/idumenskyi/work/pycharm/test_pyims_with_main/test_skype_send_message.py
Launching unittests with arguments python -m unittest /home/idumenskyi/work/pycharm/test_pyims_with_main/test_skype_send_message.py in /home/idumenskyi/work/pycharm/test_pyims_with_main
setUpClass
==========Set up for [PASSWORD is SET, TEST]
id: test_skype_send_message.skype_send_message_test.test_main_with_setting_password
Tear down for [PASSWORD is SET, TEST]


Error
Traceback (most recent call last):
  File "/usr/lib/python3.6/unittest/case.py", line 59, in testPartExecutor
    yield
  File "/usr/lib/python3.6/unittest/case.py", line 605, in run
    testMethod()
  File "/home/idumenskyi/work/pycharm/test_pyims_with_main/test_skype_send_message.py", line 34, in test_main_with_setting_password
    self.assertEqual(skype_send_message.main('username', 'password'), 'password')
TypeError: main() takes 1 positional argument but 2 were given

==========
tearDownClass

Ran 1 test in 0.003s

FAILED (errors=1)

Process finished with exit code 1
```
