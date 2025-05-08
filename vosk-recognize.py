#!/usr/bin/env python3
import argparse
import json
import wave
from vosk import Model, KaldiRecognizer

def recognize_file(filename, model):
    try:
        with wave.open(filename, "rb") as wf:
            # Проверка формата файла
            if wf.getnchannels() != 1:
                raise ValueError("Требуется моно-аудио (1 канал)")
            if wf.getsampwidth() != 2:
                raise ValueError("Требуется 16-битный PCM-формат")
            if wf.getframerate() != 16000:
                raise ValueError("Требуется частота дискретизации 16 кГц")

            recognizer = KaldiRecognizer(model, wf.getframerate())
            
            results = []
            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if recognizer.AcceptWaveform(data):
                    results.append(json.loads(recognizer.Result()))
            
            final = json.loads(recognizer.FinalResult())
            results.append(final)
            
            # Собираем полный текст
            full_text = " ".join([res["text"] for res in results if "text" in res])
            return full_text

    except Exception as e:
        return f"Ошибка: {str(e)}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Распознавание WAV-файлов через Vosk")
    parser.add_argument("files", nargs="+", help="WAV-файлы для обработки")
    parser.add_argument("--model", default="model", 
                      help="Путь к модели Vosk (по умолчанию: 'model')")
    
    args = parser.parse_args()

    # Загрузка модели
    try:
        model = Model(args.model)
    except Exception as e:
        print(f"Ошибка загрузки модели: {str(e)}")
        exit(1)

    # Обработка файлов
    for file_path in args.files:
        print(f"\nОбработка файла: {file_path}")
        result = recognize_file(file_path, model)
        
        if result.startswith("Ошибка"):
            print(f" {result}")
        else:
            print(" Распознанный текст:")
            print("-" * 50)
            print(result)
            print("-" * 50)
