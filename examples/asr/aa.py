import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
import time
import requests
import keyboard
import sounddevice as sd
import numpy as np
import wave
import pygame
from examples.asr.flashexample import asr
from examples.tts.ttsexample import tts

class ChatGUI:
    def __init__(self, master):
        self.master = master
        master.title("人机交互页面")

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.text_area.pack(expand=True, fill='both')
        self.text_area.insert(tk.END, "欢迎来到人机交互页面！点击 '开始语音对话' 开始与机器人聊天。\n")

        self.record_button = tk.Button(master, text="开始语音对话", command=self.start_chat_thread)
        self.record_button.pack()

        self.stop_button = tk.Button(master, text="停止语音对话", command=self.stop_chat_thread, state=tk.DISABLED)
        self.stop_button.pack()

        self.user_input = ""

    def start_chat_thread(self):
        self.record_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, "你：")
        self.user_input = ""

        def chat_thread():
            while True:
                output_filename = "recorded_audio.wav"
                record_and_save(output_filename)

                self.user_input = asr(output_filename)
                self.text_area.insert(tk.END, f"{self.user_input}\n")
                response = chat_with_qingyunke(self.user_input)
                self.text_area.insert(tk.END, f"chatbot：{response}\n")
                tts(response)
                play_audio('response.pcm.wav')
                time.sleep(1)  # 为了避免过快刷新

        self.chat_thread = Thread(target=chat_thread)
        self.chat_thread.start()

    def stop_chat_thread(self):
        self.record_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.text_area.insert(tk.END, "对话结束\n")
        self.chat_thread.join()

def chat_with_qingyunke(msg):
    # 与青云客进行对话的函数，与你提供的代码一致
    # ...
    base_url = "http://api.qingyunke.com/api.php"
    key = "free"
    appid = 0

    # 对消息进行 urlencode 处理
    encoded_msg = requests.utils.quote(msg)

    # 构建请求参数
    params = {
        "key": key,
        "appid": appid,
        "msg": encoded_msg
    }

    # 发送 GET 请求
    response = requests.get(base_url, params=params)

    # 解析返回的 JSON 数据
    result = response.json()

    # 返回聊天结果
    return result["content"]
def record_and_save(filename, sample_rate=44100):
    # 录音和保存的函数，与你提供的代码一致
    # ...
    print("Recording... (Press 'q' to stop)")

    # 开始录音
    audio_data = []
    with sd.InputStream(channels=2, samplerate=sample_rate, dtype=np.int16) as stream:
        stream.start()
        while True:
            # 读取音频数据
            block, overflowed = stream.read(1024)  # 修改此行
            audio_data.append(block.copy())

            # 检查是否按下 'q' 键，如果是则停止录音
            if keyboard.is_pressed('q'):
                break

    # 合并音频数据
    audio_data = np.concatenate(audio_data, axis=0)

    print("Recording complete.")

    # 保存为.wav文件
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())

    print(f"Audio saved as {filename}")

def play_audio(file_path):
    # 播放音频的函数，与你提供的代码一致
    # ...
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # 等待音频播放完毕
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        pygame.mixer.quit()
        
if __name__ == "__main__":
    root = tk.Tk()
    gui = ChatGUI(root)
    root.mainloop()
