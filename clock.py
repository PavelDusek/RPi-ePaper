#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd2in7
import time
import datetime
from PIL import Image, ImageDraw, ImageFont
import traceback

def main():
    path   = "/home/pi/hodiny"
    days    = [u'Pondĕlí', u'Úterý', u'Středa', u'Čtvrtek', u'Pátek', u'Sobota', u'Nedĕle']
    months = [u'leden', u'únor', u'březen', u'duben', u'kvĕten', u'červen', u'červenec', u'srpen', u'září', u'říjen', u'listopad', u'prosinec']

    now           = datetime.datetime.now()
    today_name    = now.strftime("%Y-%m-%d")
    tomorrow      = now + datetime.timedelta(days=1)
    tomorrow_name = tomorrow.strftime("%Y-%m-%d")
    day           = days[now.weekday()]
    month         = now.month
    datum         = "{d}. {month} {rok}".format(d=now.day, month=month, rok=now.year)
    time_           = "{h}:{m:02d}".format(h=now.hour, m=now.minute)

    try:
        epd = epd2in7.EPD()
        epd.init()
        epd.Clear(0xFF)
        
        Himage = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255)  # 255: clear the frame
        draw = ImageDraw.Draw(Himage)
        font32 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 32)
        font26 = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf', 26)
        draw.text((2, 0), day, font = font32, fill = 0)
        draw.line((132, 0, 132, 40), fill = 0)
        draw.text((140, 0), datum, font = font26, fill = 0)
        draw.line((0, 40, 264, 40), fill = 0)
        draw.text((93, 40), time_, font = font32, fill = 0)
        draw.line((0, 80, 264, 80), fill = 0)
        epd.display(epd.getbuffer(Himage))
        epd.sleep()
            
    except:
        print('traceback.format_exc():\n%s',traceback.format_exc())
        exit()

if __name__ == "__main__":
    main()
