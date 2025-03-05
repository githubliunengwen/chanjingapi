"""
蝉镜 - 合成视频实例

本示例展示如何使用create方法创建合成视频
"""
from chanjing.core import ChanjingHttpClient
import chanjing.synthesis  
import asyncio
import os

"""
   APP_ID: API应用ID
   APP_SECRET: API应用密钥

"""
APP_ID = "cj_test_id"
APP_SECRET = "cj_test_secret_key"

# from dotenv import load_dotenv


# # 加载环境变量
# load_dotenv()

# # 从环境变量获取API密钥和基础URL
# ADMIN_API_KEY = os.getenv("DIFY_ADMIN_KEY")
# BASE_URL = os.getenv("DIFY_BASE_URL")


async def main():
    """演示如何使用create方法创建合成视频"""
    # 初始化客户端
    client = ChanjingHttpClient(APP_ID, APP_SECRET)

    # 合成视频
    request = chanjing.synthesis.CreateVideoRequest(
          person= chanjing.synthesis.PersonConfig(
                id="C-b6a9747074ab4b7b8006f61f22ff022c",
                x=0,
                y=480,
                width=1080,
                height=1440
                ),
            audio= chanjing.synthesis.AudioConfig(
                tts=chanjing.synthesis.TTSConfig(
                    text=[
                        "君不见黄河之水天上来，奔流到海不复回。"
                    ],
                    speed=1,
                    audio_man="C-b7c7fa71ed304e0586c69ad4d611df0e"
                ),
                wav_url="https://res.chanjing.cc/chanjing/res/person/2025-02-08/72d12148-56b8-4eec-80b6-390a83ea5ea2_480.webm",
                type="tts",
                volume=100,
                language="cn"
            ),
            bg_color="#EDEDED",
            screen_width=1080,
            screen_height=1920
        )
    
    print("创建合成视频示例")
    print("-" * 30)

    response = chanjing.synthesis.Video(client).create(request)
    
    print("创建合成视频返回结果:")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())