import requests
import os
from lxml import etree


def download_images():
    # 目标网站URL
    url = "http://pic.netbian.com/"

    # 设置保存目录 - 在当前目录下的images文件夹
    save_dir = os.path.join(os.getcwd(), "images")
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        print(f"已创建目录: {save_dir}")

    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }

    try:
        # 获取网页内容
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response.encoding = "gbk"
        html_content = response.text

        # 解析HTML
        tree = etree.HTML(html_content)
        img_src_list = tree.xpath("//ul[@class='clearfix']/li/a/span/img/@src")
        print(f"找到 {len(img_src_list)} 张图片")

        # 下载图片
        for i, img_src in enumerate(img_src_list):
            # 构建完整的图片URL
            img_url = f"http://pic.netbian.com{img_src}"
            print(f"正在下载第 {i + 1}/{len(img_src_list)} 张图片: {img_url}")

            try:
                # 获取图片
                img_response = requests.get(img_url, headers=headers)
                img_response.raise_for_status()

                # 从URL中提取文件名
                img_name = os.path.basename(img_src)

                # 构建保存路径 - 在images目录下
                save_path = os.path.join(save_dir, img_name)

                # 保存图片
                with open(save_path, "wb") as f:
                    f.write(img_response.content)

                print(f"已保存到: {save_path}")

            except Exception as img_error:
                print(f"下载图片失败: {img_error}")

        print("所有图片下载完成!")

    except Exception as e:
        print(f"获取网页失败: {e}")


if __name__ == "__main__":
    download_images()