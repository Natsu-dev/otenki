# coding: UTF-8

import discord
import otenki
import datetime

activity = 't:info'

info = discord.Embed(
    title='おてんき Version {}\n'.format(otenki.VERSION),
    description='毎日22時に気象庁発表の翌日の天気の情報を書き込むbotです。\nより詳細な天気の情報は気象庁ホームページ( https://www.jma.go.jp/ )等を確認してください。また、このbotは気象庁非公式かつ非公認であることにご留意ください。\n詳しい仕様はGitHubリポジトリ( https://github.com/Natsu-dev/otenki )に掲載していますので、必ずご一読ください。')
