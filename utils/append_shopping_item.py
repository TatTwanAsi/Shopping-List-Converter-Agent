import os
from langchain.tools import tool

@tool  # 定义工具的修饰符
def append_shopping_item(file_path, new_line):
    """ 将新的 [所需商品数量, 商品url] 追加到指定文件中 """
    with open(file_path, "a", encoding = "utf-8") as f:
        f.write(new_line + "\n")
    print(f"\n\n --- \"{new_line}\" 已追加至 : {file_path} --- \n\n")