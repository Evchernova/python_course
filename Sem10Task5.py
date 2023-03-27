"""Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
 преобразовать результаты из байтовового в строковый тип на кириллице."""

import subprocess
import chardet

args = ['ping', '-c', '2', 'yandex.ru']

yandex_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in yandex_ping.stdout:
    result = chardet.detect(line)
    line = line.decode(result["encoding"]).encode("utf-8")
    print(line.decode("utf-8"))

args = ['ping', '-c', '1', 'youtube.com']

youtube_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in youtube_ping.stdout:
    result = chardet.detect(line)
    line = line.decode(result["encoding"]).encode("utf-8")
    print(line.decode("utf-8"))
