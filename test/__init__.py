import whisper
from wer import wer
import os
import pandas

model = whisper.load_model("medium")


def test_wer(path_audio: str, path_text: str = None, text: str = None) -> any:
    result = model.transcribe(path_audio, fp16=False)

    if (path_text == None and text == None):
        raise RuntimeError()

    test_text = text if text != None else open(path_text, "r").read()
    return wer(test_text, result['text'], debug=False)


def tests_wer(path_csv: str, root_folder_data: str = os.getcwd()):
    df = pandas.read_csv(path_csv, sep=';', encoding='utf-8')
    for audio, text in zip(df['audio'], df['text']):
        result = test_wer(path_audio=os.path.join(
            root_folder_data, audio), path_text=os.path.join(root_folder_data, text))
        print(f'%s: %.2f' % audio % result['WER'])
