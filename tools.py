import requests
import json
import pendulum
from bs4 import BeautifulSoup
from lxml import etree


def math_time(str_time: str):
    now_time = pendulum.now()
    hour = 24 - int(str_time.split(":")[0])
    minute = int(str_time.split(":")[1])
    second = int(str_time.split(":")[2].split(".")[0])
    start_time = now_time.subtract(hours=hour, minutes=minute, seconds=second)
    return start_time.to_datetime_string()


def spider(url: str, cookies: str):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62",
        "cookie": cookies
    }
    response = requests.get(url, headers=headers)
    bs = BeautifulSoup(response.text, "lxml")
    html = etree.HTML(response.text)
    global json_data
    while True:
        try:
            json_data = json.loads(html.xpath('//script[13]')[1].text.replace("window.rawData=", "")[:-1])
            break
        except Exception:
            continue

    if json_data["store"]["extraInfo"]["focusText"] != "":
        return False
    title = json_data["store"]["goodsInfo"]["goodsName"]  # 标题
    pic = json_data["store"]["goodsInfo"]["hdThumbUrl"]  # 图片
    originalprice = json_data["store"]["goodsInfo"]["activityPrice"]  # 原始价格
    discountprice = json_data["store"]["goodsInfo"]["originPrice"]  # 打折价格
    # timeon = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(
    #     int(json_data["store"]["endTimeMs"]) / 1000 - 86400)
    # )  # 开始时间
    timeon = math_time(str_time=bs.find_all(class_="VXsVzAXU")[0].text)
    groupid = json_data["store"]["group_order_id"]
    goodsid = json_data["store"]["goodsInfo"]["goodsId"]
    return {
        "title": title,
        "pic": pic,
        "originalprice": originalprice,
        "discountprice": discountprice,
        "timeon": timeon,
        "groupid": groupid,
        "goodsid": goodsid
    }


if __name__ == "__main__":
    data = spider(
        url="https://mobile.yangkeduo.com/pincard_ask.html?_wv=41729&_wvx=10&__rp_name=brand_amazing_price_group&_pdd_tc=ffffff&_pdd_sbs=1&group_order_id=2061413170410411636&refer_share_id=zbz3wqojclbp2w42uhihrmnom20fokuv&refer_share_uin=ERKDFG5UAZDIVT33NS74R3XRSQ_GEXDA&refer_share_channel=message",
        cookies="api_uid=Ck5AeWLC372yMgBnXXUAAg==; webp=1; _nano_fp=XpE8X0XxnqmJnpTon9_sF25HahbC0AZsckfHxSi3; jrpl=YevdW5JszEehd16ZYA3H2RrvqqK56FNn; njrpl=YevdW5JszEehd16ZYA3H2RrvqqK56FNn; dilx=8Rsjuwv68xH6skZTrWADR; PDDAccessToken=JC2F5IQ4USVKSGKXWLSTENGBHA7PVSNSGT5IYS2UMKROO5IUSXOA112f5b1; pdd_user_id=3926947573; pdd_user_uin=MBJTHFBP6ZZCUCOH27JCBYLFKQ_GEXDA; rec_list_brand_amazing_price_group=rec_list_brand_amazing_price_group_R7epQC; pdd_vds=gaApjCSugZJvSqAfXhKhkvHqkfFdKrjqJfWdqcVfpTSvgvzdXuHYKcSvAfXu")
    print(data)
