from ast import Num
from asyncio.windows_events import NULL
import urllib.request as req
import discord
import datetime
import json

import otenki
import phrases

# option: 週間天気予報の何番目を取り出すか
def forecast(option = NULL):
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

    # 何月何日何時気象庁発表
    rdt = tenki_dic[0]['week']['reportDatetime']
    rdt_datetime = datetime.datetime.strptime(rdt, '%Y-%m-%dT%H:%M:%S+09:00')
    reportDatetime = rdt_datetime.strftime('%m月%d日 %H時')

    # optionが空欄の場合は今日の予報を出す
    if not option:
        for td in tenki_dic[0]['week']['timeSeries'][0]['timeDefines']:
            array = 0
            td_datetime = datetime.datetime.strptime(td, '%Y-%m-%dT%H:%M:%S+09:00')
            td_date = datetime.date(td_datetime.year, td_datetime.month, td_datetime.day)

            # 今日の日付に該当する項目があればその番号をoptionに控える
            if datetime.datetime.today() == td_date:
                option = array
                break

            array += 1

    od = tenki_dic[0]['week']['timeSeries'][0]['timeDefines'][option]
    od_datetime = datetime.datetime.strptime(od, '%Y-%m-%dT%H:%M:%S+09:00')
    optionDate = datetime.date(od_datetime.year, od_datetime.month, od_datetime.day)


    forecast = discord.Embed(
        title='{}の天気'.format(optionDate.strftime('%m月%d日')),
        color=0x219ddd,
        description='{}気象庁発表'.format(reportDatetime),
        url='https://www.jma.go.jp/bosai/forecast/',
    )

    # nameの数だけループして全都市引っ張り出す
    for area in tenki_dic:

        name = area['name']
        weatherCodes = area['week']['timeSeries'][0]['areas']['weatherCodes'][option]
        weatherStr = codes_dic[weatherCodes][3]

        forecast.add_field(name=name, value=weatherStr)

    t.close()
    c.close()

    return forecast


def botInfo():
    info = discord.Embed(
    title='おてんき bot',
    color=0x219ddd,
    description='Version {}\n'.format(otenki.VERSION),
    url='https://github.com/Natsu-dev/otenki'
    )

    info.add_field(name='About', value=phrases.aboutText, inline=False)

    info.add_field(name='Commands', value=phrases.commandList, inline=False)

    return info
