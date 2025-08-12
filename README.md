# 🐱 KittenTTS Interactive Demo

An interactive demonstration script for the impressive KittenTTS text-to-speech model. This is a test script/preview built upon the same technology used in DJZ-Speech (10MB retro TTS), while we wait for the full KittenTTS release.

## About

This demo showcases the [KittenML/kitten-tts-nano-0.1](https://huggingface.co/KittenML/kitten-tts-nano-0.1) model - an ultra-lightweight, high-quality text-to-speech system built on eSpeak technologies. It's very impressive! 😻

**Created by:** [KittenML Team](https://huggingface.co/KittenML/kitten-tts-nano-0.1)  
**Built on:** eSpeak technologies  
**Interactive demo by:** This repository  
**Community:** [Join the Discord](https://discord.gg/upcyF5s6)

## ✨ Features

- **Ultra-lightweight**: Model size less than 25MB (15M parameters)
- **CPU-optimized**: Runs without GPU on any device  
- **Interactive CLI**: User-friendly interface with guided prompts
- **8 voice options**: Male and female expressive voices
- **Speed control**: Adjustable speech rate (0.5x to 2.0x)
- **Smart file naming**: Automatic timestamped output files
- **Multi-session**: Generate multiple audio files in one session

## 🚀 Installation

### Install KittenTTS

```bash
pip install https://github.com/KittenML/KittenTTS/releases/download/0.1/kittentts-0.1.0-py3-none-any.whl
```

### Get This Demo

Download or clone this repository to get the interactive demo script.

## 💻 Usage

Run the interactive demo:

```bash
python kitten_tts_demo-v0/kitten_tts_demo.py
```

The demo will guide you through:
1. **Text input** - Enter the text you want to convert to speech
2. **Voice selection** - Choose from 8 expressive voices
3. **Speed setting** - Adjust playback speed (0.5-2.0x)
4. **File naming** - Custom or automatic timestamped filenames

### Available Voices

- `expr-voice-2-m/f` - Male/Female Voice #2 - Expressive
- `expr-voice-3-m/f` - Male/Female Voice #3 - Expressive  
- `expr-voice-4-m/f` - Male/Female Voice #4 - Expressive
- `expr-voice-5-m/f` - Male/Female Voice #5 - Expressive

## 📁 What You Get

This repository contains:
- `kitten_tts_demo-v0/kitten_tts_demo.py` - Interactive demo script
- `README.md` - This documentation
- `generated_audio/` - Output folder (created automatically)

## 🔧 System Requirements

Works literally everywhere - any system with Python 3.6+

## 📋 Status

This is a **preview/test script** while we wait for the full KittenTTS model release. The underlying technology is production-ready and impressive!

## 🙏 Credits

- **KittenML Team** - Original model creators
- **eSpeak** - Underlying speech synthesis technology  
- **Community** - [Discord community](https://discord.gg/upcyF5s6)

---

*Built upon the same lightweight TTS technology that powers DJZ-Speech (10MB retro TTS)*
