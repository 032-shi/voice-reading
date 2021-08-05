# coding: UTF-8
# 上の1行で日本語対応させる
import pyttsx3
engine = pyttsx3.init() #ライブラリの初期化
engine.save_to_file("出力音声をここに入力する","test.mp3")
engine.runAndWait() #実行処理