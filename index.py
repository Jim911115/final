from flask import Flask, render_template, request
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資管二B 411016953 呂政佑的求職相關資訊</h1>"
    homepage += "<a href=/myself>我的個人簡介</a><br>"
    homepage += "<a href=/classschedule>MIS相關工作介紹</a><br>"
    homepage += "<a href=/www>職涯測驗結果</a><br>"
    homepage += "<a href=/person>求職履歷自傳</a><br>"
    return homepage

