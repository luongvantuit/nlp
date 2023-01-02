import os
from test import tests_wer


def test_en():
    tests_wer(os.path.join(os.getcwd(), "data/en/en.csv"),
              root_folder_data=os.path.join(os.getcwd(), "data/en"))
