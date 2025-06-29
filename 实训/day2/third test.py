import os


def rename_images_from_txt(image_folder, txt_file):
    """
    批量将图片文件名更改为txt文件中指定的名称（严格保持Windows资源管理器显示顺序）

    参数:
        image_folder: 存放图片的文件夹路径
        txt_file: 包含新文件名的文本文件路径
    """
    # 读取txt文件中的新文件名
    with open(txt_file, 'r', encoding='utf-8') as f:
        new_names = [line.strip() for line in f if line.strip()]

    # 获取图片文件列表（按Windows资源管理器顺序）
    image_files = []
    for f in os.listdir(image_folder):
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            image_files.append(f)

    # 使用Windows自然排序（如1,2,10而不是1,10,2）
    def windows_sort_key(filename):
        import re
        return [int(text) if text.isdigit() else text.lower()
                for text in re.split('([0-9]+)', filename)]

    image_files.sort(key=windows_sort_key)

    # 检查数量是否匹配
    if len(image_files) != len(new_names):
        print(f"错误: 图片数量({len(image_files)})与名称数量({len(new_names)})不匹配！")
        print("请确保：")
        print("1. 图片和名称数量相同")
        print("2. 文本文件中没有多余空行")
        return

    # 批量重命名
    for i, (old_name, new_name) in enumerate(zip(image_files, new_names)):
        old_path = os.path.join(image_folder, old_name)
        ext = os.path.splitext(old_name)[1]  # 保留原扩展名

        # 处理重复文件名
        counter = 1
        new_base = new_name
        while True:
            new_path = os.path.join(image_folder, f"{new_base}{ext}")
            if not os.path.exists(new_path):
                break
            new_base = f"{new_name}_{counter}"
            counter += 1

        try:
            os.rename(old_path, new_path)
            print(f"成功: {old_name} -> {os.path.basename(new_path)}")
        except Exception as e:
            print(f"失败: {old_name} | 错误: {str(e)}")


# 使用示例
if __name__ == "__main__":
    # 替换为你的实际路径（建议使用原始字符串r''防止转义问题）
    image_folder = r"D:\Games\pythonProject3\实训\day2\pictures"
    txt_file = r"names.txt"

    rename_images_from_txt(image_folder, txt_file)