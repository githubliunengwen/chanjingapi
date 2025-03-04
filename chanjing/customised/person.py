from typing import Optional
from pydantic import BaseModel

from chanjing.core import ChanjingHttpClient


class CreateCustomisedPersonRequest(BaseModel):
    """创建定制数字人请求模型
    
    属性:
        name: 定制数字人名称
        material_video: 外网可下载播放的mp4视频文件
        callback: 回调地址，任务结束后会向该地址发送POST请求
        train_type: 训练类型，可选参数
    """
    name: str
    material_video: str
    callback: str
    train_type: Optional[str] = None

class CustomisedPerson(object):
    def __init__(self,client:ChanjingHttpClient) -> None:
        """
        初始化定制数字人管理类
        
        Args:
            client: 禅境HTTP客户端
        """
        self.client = client
        pass
    def create(self , request:CreateCustomisedPersonRequest)->str:
        """
        创建定制数字人
        
        Args:
            request: 创建定制数字人请求
        """
        self.client.request("POST", "create_customised_person", json=request.model_dump())
        pass