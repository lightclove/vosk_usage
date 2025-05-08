from vosk import Model, KaldiRecognizer
import pyaudio

# Укажите путь к модели (например, папка 'model' в проекте)
model = Model("model/vosk-model-small-ru-0.22")  # Измените путь!
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    input=True,
    frames_per_buffer=8192
)
stream.start_stream()

print("Говорите...")

while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
        result = recognizer.Result()
        print(result)  # Вывод распознанного текста
