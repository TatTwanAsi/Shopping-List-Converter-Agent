from agents.converter_agent import ConverterAgent
import json
from utils.get_shopping_items import get_shopping_items
import webbrowser



def main():
    # try:
    #     converter_agent = ConverterAgent()
    # except Exception as e:
    #     print(f"unexpected error occured while initializing agent: {e}")
    #     return

    # task_input = {
    #     "messages":[
    #         {
    #             "role": "user",
    #             "content":(
    #                 "请读取当前目录下的origin.docx文件, 这就是输入的购物清单。按照你的prompt去执行就好"
    #             )
    #         }
    #     ]
    # }

    # print("\n\n\n --- Agent 开始执行任务 --- \n\n\n")

    # result = converter_agent.agent.invoke(task_input)
    
    # print("\n\n\n --- 输出结果 --- \n\n\n")

    # print(result['messages'][-1].content)

    # shopping_list = get_shopping_items("./origin.docx")
    # print(f"\n\n\n --- 商品种数: {len(shopping_list)} --- \n\n\n")
    
    
    # try:
    #     with open("./shopping_items.json", 'w') as f:
    #         json.dump(shopping_list, f, indent = 2)
    # except Exception as e:
    #     print(e)
    
    # for item in shopping_list:
    #     print(item)

    try:
        with open("shopping_items.json", 'r') as f:
            shopping_items = json.load(f)
        # print(f"找到{len(shopping_items)}个商品")

        shopping_list = list(enumerate(shopping_items))
        for i in range(110,120):
            print(i)
            webbrowser.open(shopping_list[i][1]['url'])
        


    except FileNotFoundError:
        print(f"错误: 找不到文件 {json_file}")
    except json.JSONDecodeError:
        print(f"错误: {json_file} 不是有效的JSON文件")
    except Exception as e:
        print(f"发生错误: {e}")


    

if __name__ == "__main__":
    main()
