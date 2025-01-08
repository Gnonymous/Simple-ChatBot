<p align="center">
  <img src="img/chatbot对话机器人.svg" alt="Simple-ChatBot" width="180"/>
</p>

<h1 align="center">Simple-ChatBot</h1>

<p align="center">
  <b>🤖 智能语音交互机器人 | Voice Interactive ChatBot</b>
</p>
<p align="center">
  <a href="#-项目介绍">简介</a> •
  <a href="#-快速开始">快速开始</a> •
  <a href="#-系统架构">架构</a> •
  <a href="#-主要功能模块">功能</a> •
  <a href="./Exp_Report.md">详细文档</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-white.svg" alt="License">
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/version-2.0.0-yellow.svg" alt="Version">
  <img src="https://img.shields.io/github/issues/Gnonymous/Simple-ChatBot.svg" alt="Issues">
  <img src="https://img.shields.io/github/last-commit/Gnonymous/Simple-ChatBot.svg" alt="Last Commit">
</p>
<p align="center">
  <a href="./Exp_Report.md">
    <img src="https://img.shields.io/badge/Document-Exp-red.svg" alt="License">
  </a>
  <img src="https://img.shields.io/github/stars/Gnonymous/Simple-ChatBot.svg" alt="Stars">
</p>

<div align="center">
  <sub>Owner with ❤︎ by
  <a href="https://github.com/Gnonymous">Gnonymous</a>
  </sub>
</div>

---

> 一个轻量级的智能语音交互机器人，基于Python实现的人机对话系统。

## 🌟 项目介绍

Simple-ChatBot 是一个基于 Python 的简易（但蠢笨）智能语音交互机器人项目。本项目最初源于中南大学人机交互(HCI)课程的实验项目。

~~本学期结束后我会对该项目进行更新，敬请期待~~

---

Simple-ChatBot is a simple (but clumsy) intelligent voice interaction robot project based on Python. This project originally came from an experimental project in the HCI course at CSU.

~~I will update this project after the end of this term, please stay tuned~~. 

---

### 🎯 核心特性

- 实时语音识别与转换
- 智能对话响应系统
- 简洁直观的图形界面
- 轻量级架构设计
- 高度可定制化

## 🔍 系统架构

### 技术栈

![System Architecture](img/image-20241106220644365.png)

> [!NOTE]
>
> 该项目并不复杂，并没有复杂的前后端，“后端“以``函数``的形式。

#### 后端架构
- **语音识别**: [腾讯云语音识别控制平台](https://cloud.tencent.com/product/asr)
- **对话系统**: [青云客智能聊天机器人](http://api.qingyunke.com/)(有条件可以使用[Ollama](https://ollama.com/)在本地部署LLM，效果⬆️)
- **核心处理**: Python 3.7+

#### 前端界面
- **GUI框架**: Tkinter
- **交互设计**: 简约直观的用户界面

## 📁 项目结构

```
Simple-ChatBot/
├─ Exp_Report.md     # 详细实验报告
├─ README.md         # 项目说明文档
├─ chatbot_withoutGUI.py  # 命令行版本
├─ chatbot_withGUI.py     # 图形界面版本
├─ asr/              # 语音识别模块
├─ common/           # 公共组件
├─ examples/         # 示例代码
│  ├─ asr/
│  └─ tts/
├─ img/             # 图片资源
└─ tts/             # 语音合成模块
```

## 🚀 快速开始

### 前置要求

1. Python 3.8 或更高版本
2. 腾讯云API密钥配置
3. 网络连接

### 使用指南

1. 克隆项目
```bash
git clone https://github.com/Gnonymous/Simple-ChatBot.git
cd Simple-ChatBot
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置API密钥
   - 配置[腾讯云语音识别平台API](https://cloud.tencent.com/product/asr)
   - 配置[青云客智能对话API](http://api.qingyunke.com/)

4. 运行程序
```bash
python chatbot_withGUI.py
```
## 📌 主要功能模块

> [!TIP]
>
> 1. 在使用之前，建议配合阅读[Exp_Report.md](https://github.com/Gnonymous/Simple-ChatBot/blob/main/Exp_Report.md)
> 2. 前期请配置好[腾讯云语音识别控制平台](https://cloud.tencent.com/product/asr)与[青云客智能聊天机器人](http://api.qingyunke.com/) API Key
> 3. 点击`开始语音对话`开始讲话，点击`停止语音对话`，静待输出响应应答

###  ➪ [chatbot_withoutGUI.py](https://github.com/Gnonymous/Simple-ChatBot/blob/main/chatbot_withoutGUI.py)「建议从此入手，开箱即用」

* [def chat_with_qingyunke(msg)](https://github.com/Gnonymous/Simple-ChatBot/blob/main/chatbot_withoutGUI.py#L10)「处理文本理解与应答」
* [def record_and_save(filename, sample_rate=44100)](https://github.com/Gnonymous/Simple-ChatBot/blob/main/chatbot_withoutGUI.py#L35)「处理语音与文本」
* [def chat()](https://github.com/Gnonymous/Simple-ChatBot/blob/main/chatbot_withoutGUI.py#L84)「对话主循环」

###  ➪  [chatbot_withGUI.py](https://github.com/Gnonymous/Simple-ChatBot/blob/main/chatbot_withGUI.py)「串联前端GUI，开箱即用」

* [Class ChatGUI](https://github.com/Gnonymous/Simple-ChatBot/blob/main/chatbot_withGUI.py#L14)「基于Tkinter的GUI界面」
* [if __name__ == "__main__":](https://github.com/Gnonymous/Simple-ChatBot/blob/main/chatbot_withGUI.py#L133)「处理主线程」

<img src="img/image-20241106220858199.png" alt="image-20241106220858199"  />

---

## Others

> [!CAUTION]
>
> ⚠️该项目仅作学习交流使用，鼓励在此基础上进行二次开发更新，切勿因抄袭导致课程不及格！
>
> ⚠️The project is only for learning and communication use, encourage secondary development and update on the basis of again, do not plagiarism lead to course failure!
