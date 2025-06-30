import requests
from bs4 import BeautifulSoup
import re
import time
import random
from urllib.parse import quote

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Referer": "https://c61.oversea.cnki.net"
}

# 目标文章列表
titles = [
    "基于视觉信息的煤矸识别分割定位方法",
    "基于YOLO11的无人机航拍图像小目标检测算法",
    "AA-GM-YOLO：基于改进YOLO的机加工切屑监测方法",
    "轻量化输电线路缺陷检测方法",
    "基于关键点检测的服装尺寸测量方法",
    "基于YOLO的小目标检测算法研究"
]


def get_dynamic_params(session, url):
    """获取ASP.NET动态参数（__VIEWSTATE等）"""
    try:
        resp = session.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        viewstate = soup.find("input", {"id": "__VIEWSTATE"}).get("value", "")
        event_validation = soup.find("input", {"id": "__EVENTVALIDATION"}).get("value", "")
        return viewstate, event_validation
    except Exception as e:
        print(f"获取动态参数失败: {e}")
        return "", ""


def search_cnki(title):
    """精确搜索知网并提取第一篇结果的元数据"""
    session = requests.Session()
    search_url = "https://c61.oversea.cnki.net/kns/brief/brief.aspx"
    base_url = "https://c61.oversea.cnki.net"

    try:
        # 第一步：获取初始动态参数
        viewstate, event_validation = get_dynamic_params(session, search_url)

        # 构造搜索表单数据
        form_data = {
            "__VIEWSTATE": viewstate,
            "__EVENTVALIDATION": event_validation,
            "hidkey": "",
            "txt_1_sel": "SU$%=|",  # 按标题搜索
            "txt_1_value1": title,
            "btn_search": "检索"
        }

        # 随机延迟避免封禁
        time.sleep(random.uniform(3, 6))

        # 提交搜索请求
        response = session.post(search_url, data=form_data, headers=headers, timeout=20)
        response.raise_for_status()

        # 解析搜索结果页
        soup = BeautifulSoup(response.text, 'html.parser')
        first_result = soup.select_one("a.fz14")
        if not first_result:
            print(f"未找到文章: {title}")
            return None

        # 获取详情页链接
        detail_path = first_result['href']
        detail_url = base_url + detail_path if detail_path.startswith('/') else base_url + '/' + detail_path

        # 访问详情页
        time.sleep(random.uniform(4, 8))
        detail_resp = session.get(detail_url, headers=headers, timeout=25)
        detail_resp.raise_for_status()
        detail_soup = BeautifulSoup(detail_resp.text, 'html.parser')

        # 提取元数据（根据海外版页面结构调整选择器）
        title_elem = detail_soup.find("h1", class_="title")
        authors = [a.text.strip() for a in detail_soup.select(".author a, .author span") if a.text.strip()]
        abstract_elem = detail_soup.find("span", class_="abstract-text")
        source_elem = detail_soup.find("a", href=re.compile(r'knavi/journal/'))

        return {
            "title": title_elem.text.strip() if title_elem else title,
            "authors": authors if authors else ["未知"],
            "abstract": abstract_elem.text.strip() if abstract_elem else "无摘要",
            "source": source_elem.text.strip() if source_elem else "无来源",
            "url": detail_url
        }

    except Exception as e:
        print(f"爬取失败 ({title}): {str(e)}")
        return None


# 执行爬取
results = []
for title in titles:
    print(f"正在爬取: 《{title}》")
    data = search_cnki(title)
    if data:
        results.append(data)
    time.sleep(random.uniform(5, 10))  # 关键延迟避免IP封禁

# 输出结果
for res in results:
    print("\n" + "=" * 80)
    print(f"标题: {res['title']}")
    print(f"作者: {', '.join(res['authors'])}")
    print(f"摘要: {res['abstract'][:250]}...")
    print(f"来源: {res['source']}")
    print(f"链接: {res['url']}")
    print("=" * 80)