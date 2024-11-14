import requests
import pygame
import sounddevice as sd
import numpy as np
import wave
import keyboard
from examples.asr.flashexample import asr
from examples.tts.ttsexample import tts

def chat_with_qingyunke(msg):
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

user_input='今天日期是什么'

def chat():
    while(1):
        # 与青云客进行对话
        print("你可以随时输入消息，输入 '退出' 可以结束对话。")

        # while True:
        print('请说话：')
        # 设置文件名
        output_filename = "recorded_audio.wav"
        # 调用录音函数

        record_and_save(output_filename)

        global user_input
        user_input = asr(output_filename)
        print(user_input)

        # 检查用户是否输入 '退出'，如果是则结束对话

            # 调用聊天函数并输出结果
        response = chat_with_qingyunke(user_input)
        print("chatbot：", response)
        tts(response)
        play_audio('response.pcm.wav')

def get_input():
    return user_input
