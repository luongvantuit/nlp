import whisper
import os



path: str = os.path.join(os.getcwd(), "audio.mp3")


model = whisper.load_model("small")


result = model.transcribe(path)


print(result["text"])


