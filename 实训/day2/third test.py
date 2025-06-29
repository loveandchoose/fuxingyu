import os
import re


def windows_natural_sort_key(filename):
    """
    Windows自然排序键（带前导零的数字排在相同值的数字之前）
    示例排序结果：01.jpg, 1.jpg, 02.jpg, 2.jpg, 10.jpg
    """

    def split_parts(text):
        parts = re.split('([0-9]+)', text)
        for i in range(len(parts)):
            if parts[i].isdigit():
                # 带前导零的数字排序时标记为更小
                parts[i] = (int(parts[i]), -len(parts[i]))  # (数值, 前导零长度负值)
        return parts

    return [part for part in split_parts(filename)]


def rename_images_from_txt(image_folder, txt_file):
    # 读取新名称
    with open(txt_file, 'r', encoding='utf-8') as f:
        new_names = [line.strip() for line in f if line.strip()]

    # 获取并排序图片文件
    image_files = [f for f in os.listdir(image_folder)
                   if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    image_files.sort(key=windows_natural_sort_key)

    # 检查数量匹配
    if len(image_files) != len(new_names):
        print(f"错误: 图片数量({len(image_files)}) ≠ 名称数量({len(new_names)})")
        return

    # 执行重命名
    for old_name, new_name in zip(image_files, new_names):
        old_path = os.path.join(image_folder, old_name)
        ext = os.path.splitext(old_name)[1]
        new_path = os.path.join(image_folder, f"{new_name}{ext}")

        try:
            os.rename(old_path, new_path)
            print(f"成功: {old_name} → {new_name}{ext}")
        except Exception as e:
            print(f"失败: {old_name} | 错误: {e}")


# 使用示例
if __name__ == "__main__":
    rename_images_from_txt(
        image_folder=r"D:\Games\pythonProject3\实训\day2\pictures",
        txt_file=r"names.txt"
    )