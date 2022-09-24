import pytest
from messages import MESSAGES
from version_handler import send_notification

class TestMessages:

    def test_message_fail_install(self):
        exit_code = send_notification(MESSAGES['fails']['install'])
        assert exit_code == 0


    def test_message_fail_download(self):
        exit_code = send_notification(MESSAGES['fails']['download'])
        assert exit_code == 0


    def test_message_fail_save_infos(self):
        exit_code = send_notification(MESSAGES['fails']['save_infos'])
        assert exit_code == 0


    def test_message_fail_save_file(self):
        exit_code = send_notification(MESSAGES['fails']['save_file'])
        assert exit_code == 0


    def test_message_fail_mkdir(self):
        exit_code = send_notification(MESSAGES['fails']['mkdir'])
        assert exit_code == 0