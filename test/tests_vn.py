import os
from test import tests_wer


def tests_vn() -> None:
    tests_wer(os.path.join(os.getcwd(), "data/vn/vn.csv"),
              root_folder_data=os.path.join(os.getcwd(), "data/vn"))
