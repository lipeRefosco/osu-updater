# import os
from tempfile import tempdir
import tempfile

# Application 
from version_handler import create_desktop_file
from desktopfile import *

class TestVersionHandler:
    
    def test_shoud_return_true_when_try_save_desktop_file_on_temp_directory(self):
        expected = True
        file = tempfile.gettempdir() + '/osulazer.desktop'

        assert create_desktop_file(file, desktop_file) == expected

