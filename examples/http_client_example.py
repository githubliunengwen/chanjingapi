"""
禅境API客户端基本用法示例
"""

import logging
import os
from chanjing.core import ChanjingHttpClient
import chanjing.customised.audio
import chanjing.customised.person
import chanjing.synthesis
import chanjing.schemas

# 设置日志级别
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
"""
   APP_ID: API应用ID
   APP_SECRET: API应用密钥
  
   """
APP_ID = "cj_test_id"
APP_SECRET = "cj_test_secret_key"

def main():
    """演示禅境API客户端基本用法"""
    print("禅境API客户端演示")
    print("-" * 30)
    
    # # 从环境变量获取API密钥（推荐做法）
    # api_key = "cj_test_id"
    # api_secret  = "cj_test_secret_key"
    # if not api_key:
    #     print("警告: 未设置CHANJING_API_KEY环境变量，使用示例API密钥")
    #     print("在实际使用中，请设置您的API密钥:")
    #     print("  Windows (PowerShell): $env:CHANJING_API_KEY='your_api_key'")
    #     print("  Linux/Mac: export CHANJING_API_KEY='your_api_key'")
    #     api_key = "example_api_key"  # 这只是一个示例，实际使用时需要替换
    
    # # 初始化客户端
    # client = ChanjingHttpClient(app_id=api_key,app_secret=api_secret)
    
    try:
        # # 示例1: 发送GET请求
        # print("\n示例1: 发送GET请求")
        # print("-" * 20)
        # 注意: 这是一个示例端点，实际使用时需要替换为真实的API端点
        # response = client.request("GET", "font_list")
        # print_response(response)
        
        # 示例2: 发送带参数的GET请求
        # print("\n示例2: 发送带参数的GET请求")
        # print("-" * 20)
        # params = {
        #    "id": "f7736a11-6a5d-41e1-9248-7920077dd1a9"
        # }
        # response = client.request("GET", "video", params=params)
        # print_response(response)
        
        # 示例3: 发送POST请求
        # print("\n示例3: 发送POST请求")
        # print("-" * 20)

        # 定制数字人
        # request = chanjing.customised.person.CreateCustomisedPersonRequest(
        #     name="2测试2",
        #     material_video="https://www.w3school.com.cn/example/html5/mov_bbb.mp4",
        #     callback="https://xx.com",
        #     train_type=""
        # )

        # request = chanjing.customised.person.ListCustomisedPersonRequest(
        #     page=1,
        #     page_size=10
        # )

        # request = chanjing.customised.person.DeleteCustomisedPersonRequest(
        #     id="C-9c70756460a246b59e377e45e9cc7990"
        # )

        # 定制声音
        # request = chanjing.customised.audio.ListCustomisedAudioRequest(
        #     page=1,
        #     page_size=10
        # )

        # request = chanjing.customised.audio.CreateCustomisedAudioRequest(
        #     name="2测试2",
        #     url="https://www.cambridgeenglish.org/images/153149-movers-sample-listening-test-vol2.mp3",
        #     callback="https://xx.com",
        # )

        # 合成视频
        request = chanjing.synthesis.ListVideoRequest(
            page=1,
            page_size=10
        )

        # request = chanjing.synthesis.CreateVideoRequest(
        #     person= chanjing.synthesis.PersonConfig(
        #         id="C-b6a9747074ab4b7b8006f61f22ff022c",
        #         x=0,
        #         y=480,
        #         width=1080,
        #         height=1440
        #         ),
        #     audio= chanjing.synthesis.AudioConfig(
        #         tts=chanjing.synthesis.TTSConfig(
        #             text=[
        #                 "君不见黄河之水天上来，奔流到海不复回。"
        #             ],
        #             speed=1,
        #             audio_man="C-b7c7fa71ed304e0586c69ad4d611df0e"
        #         ),
        #         wav_url="https://res.chanjing.cc/chanjing/res/person/2025-02-08/72d12148-56b8-4eec-80b6-390a83ea5ea2_480.webm",
        #         type="tts",
        #         volume=100,
        #         language="cn"
        #     ),
        #     bg_color="#EDEDED",
        #     screen_width=1080,
        #     screen_height=1920
        # )

        # 初始化客户端
        client = chanjing.core.ChanjingHttpClient(APP_ID, APP_SECRET)

        # person = chanjing.customised.person.CustomisedPerson(client)
        # response = person.create(request)
        # response = person.list(request)
        # response = person.detail("C-9c70756460a246b59e377e45e9cc7990")
        # response = person.delete(request)
        # audio = chanjing.customised.audio.CustomisedAudio(client)
        # response = audio.create(request)
        # response = audio.list(request)
        # response = audio.detail("C-Audio-039372c2c3854155808c3097b6e7897f")
        #
        video = chanjing.synthesis.Video(client)
        # response = video.create(request)
        # response = video.list(request)
        # response = video.detail("b89be741-68d6-49ed-92b4-b6abb9f19780")
        response = video.font_list()
      
        print(response)
        # 示例3: 发送POST请求
        # print("\n示例3: 发送POST请求")
        # print("-" * 20)
        # data ={
        # "page": 1,
        # "page_size": 20
        # } 
        # response = client.request("POST", "list_customised_person", json=data)


        # print_response(response)
        
    except ValueError as e:
        print(f"参数错误: {e}")
    except ConnectionError as e:
        print(f"连接错误: {e}")
    except TimeoutError as e:
        print(f"请求超时: {e}")
    except Exception as e:
        print(f"请求失败: {e}")


def print_response(response):
    """打印响应信息"""

    print("\n响应信息")
    print("-" * 20)
    # print(f"响应代码: {response.code}")
    # print(f"响应消息: {response.msg}")
    # print(f"追踪ID: {response.trace_id}")

    print(f"data: {response.data}")

    if response.data and hasattr(response.data, "list") and response.data.list:
        print(f"返回数据条数: {len(response.data.list)}")
        print(f"第一条数据: {response.data.list[0].name if response.data.list else '无'}")
    
    if response.data and hasattr(response.data, "page_info"):
        page_info = response.data.page_info
        print(f"分页信息: 第{page_info.page}页，每页{page_info.size}条，共{page_info.total_count}条")


if __name__ == "__main__":
    main()
