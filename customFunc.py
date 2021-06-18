import urllib.request as req
import discord
import datetime
import json


def tomorrowForecast():
    # 全国天気予報のjsonを取ってくる
    url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/010000.json'
    filename = 'tenki.json'
    req.urlretrieve(url, filename)

    # 取ってきた天気予報のjsonを開く
    t = open('tenki.json', 'r', encoding='utf-8')
    tenki_dic = json.load(t)

    # テロップ番号対応表を開く
    c = open('codes.json', 'r', encoding='utf-8')
    codes_dic = json.load(c)

    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)

    rdt = tenki_dic[0]['srf']['reportDatetime']
    rdt_datetime = datetime.datetime.strptime(rdt, '%Y-%m-%dT%H:%M:%S+09:00')
    reportDatetime = rdt_datetime.strftime('%m月%d日 %H時')

    forecast = discord.Embed(
        title='{}の天気'.format(tomorrow.strftime('%m月%d日')),
        color=0x219ddd,
        description='{}気象庁発表'.format(reportDatetime),
        url='https://www.jma.go.jp/bosai/forecast/',
    )

    # nameの数だけループして全都市引っ張り出す
    for area in tenki_dic:

        name = area['name']
        weatherCodes = area['srf']['timeSeries'][0]['areas']['weatherCodes'][1]
        weatherStr = codes_dic[weatherCodes][3]

        forecast.add_field(name=name, value=weatherStr)

    t.close()
    c.close()

    return forecast
