import requests
from bs4 import BeautifulSoup

# 豆瓣Top250电影URL
url = "https://movie.douban.com/top250"

# 设置请求头模拟浏览器访问
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    # 发送HTTP请求
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 检查请求是否成功

    # 解析HTML内容
    soup = BeautifulSoup(response.text, "html.parser")

    # 查找所有电影条目
    movie_items = soup.find_all("div", class_="item")[:10]  # 只取前10个

    # 提取电影信息
    top_movies = []
    for item in movie_items:
        # 电影标题
        title = item.find("span", class_="title").get_text()

        # 电影评分
        rating = item.find("span", class_="rating_num").get_text()

        # 电影年份和地区
        info = item.find("div", class_="bd").find("p").get_text().strip().split("\n")
        year_region = info[1].strip().split("/")[0].strip()

        # 添加到结果列表
        top_movies.append({
            "title": title,
            "rating": rating,
            "year_region": year_region
        })

    # 打印结果
    print("豆瓣电影Top10：")
    for i, movie in enumerate(top_movies, 1):
        print(f"{i}. {movie['title']} | 评分：{movie['rating']} | {movie['year_region']}")

except requests.exceptions.RequestException as e:
    print(f"请求出错: {e}")
except Exception as e:
    print(f"发生错误: {e}")