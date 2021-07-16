# coding: UTF-8
import pyttsx3
engine = pyttsx3.init()
engine.save_to_file("出力音声をここに入力する","test.mp3")
engine.runAndWait()