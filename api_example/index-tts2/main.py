from gradio_client import Client, handle_file
from enum import StrEnum


class EmoControl(StrEnum):
    SameAsSample = "Same as the voice reference"
    EmoAudio = "Use emotion reference audio"
    EmoVector = "Use emotion vectors"
    ExpTextEmoDes = "Use text description to control emotion"


text = """
各位观众晚上好，欢迎收看本次新闻快报。

今天我们来聊聊编程语言Rust。最近，一位开发者分享了他使用Rust语言开发一款多人在线游戏引擎的经历。他强调，如果没有Rust，这款引擎的许多核心功能可能无法实现。

开发者提到，他之所以选择Rust，是因为它能在多个方面满足游戏引擎的严苛要求：


"""

# !!! 注意替换为自己的实例 URL
client = Client("https://c82c4a170304865bd2.gradio.live")
result = client.predict(
    emo_control_method=EmoControl.EmoVector,
    # 注意替换为自己的 参考音频
    prompt=handle_file("audio_sample/man.mp3"),
    text=text,
    emo_ref_path=None,
    emo_weight=0.65,
    vec1=0,
    vec2=0,
    vec3=0,
    vec4=0,
    vec5=0,
    vec6=0,
    vec7=0,
    vec8=0,
    emo_text="沉着的新闻播报语气",
    emo_random=False,
    max_text_tokens_per_segment=120,
    param_16=True,
    param_17=0.8,
    param_18=30,
    param_19=0.8,
    param_20=0,
    param_21=3,
    param_22=10,
    param_23=1500,
    api_name="/gen_single",
)
print(result)
