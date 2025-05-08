# vosk_usage
Simple vosk transcriber usage script:
```bash
ffmpeg -i ~/Work/vosk/input_file.m4a -c:a pcm_s16le -ar 16000 -ac 1 output_file.wav # Сконвертируйте ваш изначальный файл в mono, 16000 hz
./vosk-recognize.py *.wav --model model/vosk-model-small-ru-0.22/ # Скачайте модель и запустите транскрибацию сконвертированного wav-файла
```
