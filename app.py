from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from tools import spider

app = Flask(__name__)
CORS(app)


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/spider", methods=["POST"])
def spider():
    data = request.get_json()
    url = data.get("url")
    cookies = "api_uid=Ck5AeWLC372yMgBnXXUAAg==; webp=1; _nano_fp=XpE8X0XxnqmJnpTon9_sF25HahbC0AZsckfHxSi3; jrpl=YevdW5JszEehd16ZYA3H2RrvqqK56FNn; njrpl=YevdW5JszEehd16ZYA3H2RrvqqK56FNn; dilx=8Rsjuwv68xH6skZTrWADR; PDDAccessToken=JC2F5IQ4USVKSGKXWLSTENGBHA7PVSNSGT5IYS2UMKROO5IUSXOA112f5b1; pdd_user_id=3926947573; pdd_user_uin=MBJTHFBP6ZZCUCOH27JCBYLFKQ_GEXDA; rec_list_brand_amazing_price_group=rec_list_brand_amazing_price_group_R7epQC; pdd_vds=gaApjCSugZJvSqAfXhKhkvHqkfFdKrjqJfWdqcVfpTSvgvzdXuHYKcSvAfXu"
    # data = spider(url=url, cookies=cookies)
    return jsonify(url=url)


if __name__ == "__main__":
    app.run(debug=True, port=666)
