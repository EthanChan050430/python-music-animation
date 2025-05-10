# 音乐生成与动画展示项目

这是一个结合了音乐生成和海龟图形的Python项目。该项目可以生成音乐并同时展示动画文字，用于庆祝澳门回归24周年。

## 功能特点

- 使用MIDI生成柠檬（Lemon）歌曲音乐
- 通过Python的turtle模块创建文字动画
- 实现音乐与动画的同步展示

## 项目结构

- `Lemon.py` - 定义了柠檬（Lemon）歌曲的MIDI音符和节奏
- `MIDIMusicScales.py` - 提供MIDI音乐创建的基础功能和音阶定义
- `play.py` - 主程序，负责播放音乐和展示动画

## 技术栈

- Python
- Pygame (音乐播放)
- Turtle (图形动画)
- MIDIUtil (MIDI音乐生成)

## 如何使用

1. 确保您已安装所需的库: `pygame`, `midiutil`
   ```
   pip install pygame midiutil
   ```

2. 运行主程序:
   ```
   python play.py
   ```

3. 欣赏音乐和动画展示

## 作者

EthanChan

## 许可证

MIT