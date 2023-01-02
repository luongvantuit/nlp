import pandas as pd
import os
from test import test_wer

def tests_vn() -> None:
    df = pd.read_table(os.path.join(os.getcwd(), 'data/vn/tests.tsv'))
    for path, sentence in zip(df['path'],df['sentence']):
        result = test_wer(path_audio=os.path.join(os.getcwd(), f'data/vn/%s'%path), text=sentence)
        print(result)