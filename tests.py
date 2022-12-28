import whisper
import os
from wer import wers, wer_debug

path: str = os.path.join(os.getcwd(), "of1_01.mp3")


model = whisper.load_model("small")


result = model.transcribe(path)

f = open(os.path.join(os.getcwd(), "of1_ts01.txt"), "r")


print(
    wer_debug(f.read(),result["text"])
)


