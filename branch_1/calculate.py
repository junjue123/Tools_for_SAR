import math
import ast

def calculate_distance(coord1, coord2):
    """计算两个坐标之间的欧氏距离"""
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def match_targets_by_distance(ws1, ws2):
    """根据中心坐标将两个工作表中的目标进行匹配"""
    matched_pairs = []
    unmatched_targets1 = []  # 用于存储未匹配的目标
    unmatched_targets2 = []  # 初始时全为未匹配

    for i in range(2,ws2.max_row + 1):
        corners = ws2.cell(row=i,column = 3).value
        corners = ast.literal_eval(corners)
        x_coords = [point[0] for point in corners]
        y_coords = [point[1] for point in corners]

        cx = sum(x_coords) / len(x_coords)
        cy = sum(y_coords) / len(y_coords)

        unmatched_targets2.append((ws2.cell(row=i,column=1).value,ws2.cell(row=i,column=2).value,cx,cy,i))
    print(unmatched_targets2)

    # 获取工作表中的所有目标及其中心坐标
    targets1 = []
    for i in range(2, ws1.max_row + 1):
        corners = ws1.cell(row=i, column=3).value
        corners = ast.literal_eval(corners)
        x_coords = [point[0] for point in corners]
        y_coords = [point[1] for point in corners]

        cx = sum(x_coords) / len(x_coords)
        cy = sum(y_coords) / len(y_coords)

        targets1.append((ws1.cell(row=i, column=1).value,ws1.cell(row=i, column=2).value, cx, cy, i))
    print(targets1)

    # 匹配最近的目标
    for target1 in targets1:
        min_distance = float('inf')
        best_match = None
        for target2 in unmatched_targets2:
            distance = calculate_distance((target1[3],target1[4]), (target2[3],target2[4]))
            if distance < min_distance:
                min_distance = distance
                best_match = target2
        if best_match:
            matched_pairs.append((target1[4], best_match[4]))  # 保存匹配行的索引
            # print(matched_pairs)
            unmatched_targets2.remove(best_match)  # 将匹配过的目标移除，防止重复匹配
        else:
            unmatched_targets1.append(target1[4])  # 未匹配的目标

    # 将未匹配的目标排到最后
    for unmatched1 in unmatched_targets1:
        matched_pairs.append((unmatched1, None))  # 记录未匹配目标，None 表示无匹配

    for unmatched2 in unmatched_targets2:
        matched_pairs.append((None, unmatched2[4]))  # 记录未匹配目标，None 表示无匹配

    return matched_pairs


def calculate_dynamic_weights(confidence1, confidence2,class1,class2):
    # 如果其中一方置信度为0，直接将其权重设为0，另一方权重设为1
    if confidence1 == 0:
        return 0.0, 1.0
    elif confidence2 == 0:
        return 1.0, 0.0
    """根据置信度动态调整权重"""
    if class1 is not None and class2 is not None:
        if class1.lower() != class2.lower():
            if confidence1 > confidence2:
                return 1.0,0.0
            else:
                return 0.0,1.0

    # 确定哪个置信度更高
    if confidence1 > confidence2:
        low_confidence, high_confidence = confidence2, confidence1
    else:
        low_confidence, high_confidence = confidence1, confidence2

    # 计算低置信度除以高置信度
    low_weight = low_confidence / high_confidence

    # 将低置信度权重和1相加
    low_weight = low_weight + 1

    # 归一化权重
    low_weight_normalized = low_weight / (low_weight + 1)
    high_weight_normalized = 1 - low_weight_normalized

    return (low_weight_normalized, high_weight_normalized) if confidence1 > confidence2 else (high_weight_normalized, low_weight_normalized)
