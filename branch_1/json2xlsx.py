import json
import pandas as pd
import os
import math

def calculate_angle(corners):
    dx = corners[1][0] - corners[0][0]
    dy = corners[1][1] - corners[0][1]
    angle = math.atan2(dy, dx)
    return angle  

def json_to_excel(json_file_path):
    # 读取JSON文件
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # 如果数据是一个字典，将其包装在列表中以确保它可以被转换为DataFrame
    if isinstance(data, dict):
        data = [data]

    # 创建DataFrame
    df = pd.DataFrame(data)

    # 直接将 corner 列作为 box 列
    df['box'] = df['corner']

    # 计算角度并创建一个新的列
    df['angle'] = df['box'].apply(calculate_angle)

    # 选择所需的列
    final_df = df[['class', 'confidence', 'box', 'angle']]

    output_file_path = os.path.splitext(json_file_path)[0] + '.xlsx'

    # 将DataFrame保存为Excel文件
    final_df.to_excel(output_file_path, index=False)
    print(f"Excel文件已保存至: {output_file_path}")


if __name__ == '__main__':
    # 调用函数转换JSON文件为Excel文件
    json_to_excel('test/SAR.json')


