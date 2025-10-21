import os
import dashscope
from langchain_community.llms import Tongyi
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain.agents.factory import create_agent
from utils.get_shopping_items import get_shopping_items
from utils.append_shopping_item import append_shopping_item
from utils.open_browser import open_browser


class ConverterAgent():
    def __init__(self):
        """初始化"""

        # 获取DashScope的API密钥
        self.api_key = os.getenv("DASHSCOPE_API_KEY")
        if(self.api_key == None):
            raise ValueError("环境变量 DASHSCOPE_API_KEY 没有被正确初始化")

        # 加载大语言模型
        self.llm = ChatTongyi(
            model = "qwen-turbo",
            api_key = self.api_key,

            temperature = 0.0   # 低能量，让Agent更具有逻辑性s
        )

        # 加载工具集
        self.tools = [get_shopping_items, append_shopping_item, open_browser]

        # 提示词 (Agent的任务说明书)
        self.system_prompt = """
            你是一个专业的shopping list转换agent, 你的任务如下: 
            1. 首先调用get_shopping_items函数，传入文件路径"origin.docx"，获得完整的商品列表。
            2. 重要：你必须处理列表中的每一个商品，不能遗漏任何一个。
            3. 对于列表中的每一个[数量, 商品url]：
               - 首先调用open_browser函数，传入url参数，在浏览器中打开这个商品页面
               - 等待几秒让页面加载
               - 然后继续处理下一个商品
            4. 继续遍历，直到所有商品的URL都在浏览器中打开。
            5. 完成后输出"已在浏览器中打开X个商品页面"。

            注意：请逐个打开，不要同时打开太多页面以免浏览器卡死。
        """

            # "2. 拿到商品列表后, 你将会遍历这个列表, 并逐个访问url。"
            # "3. 访问url之后, 你将会提取这个商品的关键信息, 获取[所需商品数量, 商品名称, 设备型号], 并输出至terminal。"


        # 创建Agent
        self.agent = create_agent(
            model = self.llm,
            tools = self.tools,
            system_prompt = self.system_prompt,
            debug = True
        )
        