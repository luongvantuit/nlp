import os
from test import tests_wer


def tests_en() -> None:
    tests_wer(path_csv=os.path.join(os.getcwd(), "data/en/en.csv"),
              root_folder_data=os.path.join(os.getcwd(), "data/en"))
