import whisper
from wer import wer

model = whisper.load_model("small")


def test_wer(path_audio: str, path_text: str = None, text:str = None) -> any:
    result = model.transcribe(path_audio)
    
    if (path_text == None and text == None): 
        raise RuntimeError()
    
    test_text = text if text != None else open(path_text, "r").read()
    return wer(test_text, result['text'])
