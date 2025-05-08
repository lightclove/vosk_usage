# vosk_usage
Simple vosk transcriber usage script:

## Сконвертируйте ваш изначальный файл в mono, 16000 hz
```bash
ffmpeg -i ~/Work/vosk/input_file.m4a -c:a pcm_s16le -ar 16000 -ac 1 output_file.wav 
```
 ## Скачайте модель для вашего языка(показано не будет, смотрите документацию vosk) и запустите транскрибацию сконвертированного wav-файла
```bash
./vosk-recognize.py *.wav --model model/vosk-model-small-ru-0.22/
```
Модели Vosk:
https://alphacephei.com/vosk/models
