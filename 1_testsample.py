#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join("/home/pi/Python_workspace/e-Paper/RaspberryPi_JetsonNano/python/", 'pic')
libdir = os.path.join("/home/pi/Python_workspace/e-Paper/RaspberryPi_JetsonNano/python/", 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in7
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)
FONT_SIZE = 18
#FONT_TEXT = ImageFont.truetype("/home/pi/Python_workspace/Gentium_Book_Plus/GentiumBookPlus-Regular.ttf", FONT_SIZE)
FONT_TEXT = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), FONT_SIZE)
SCREEN_WIDTH = None
SCREEN_HEIGH = None

sample = "Những yếu tố gì cấu thành nên lòng trắc ẩn với chính mình? Chất liệu đầu tiên của nó, thú vị thay, theo nhà tâm lý học Kristin Neff, một nhà nghiên cứu hàng đầu trong lĩnh vực này, là chánh niệm. “Tôi đang đau khổ,” “mình đang bị tổn thương,” chánh niệm giúp chúng ta lùi lại một bước, nhận diện được những gì đang xảy ra bên trong mình mà không phán xét. Bước lùi này quan trọng để chúng ta bước ra ngoài dòng thác của những cảm xúc tiêu cực đang hòng nhấn chìm ta. Yếu tố thứ hai của nó là ý thức rằng câu chuyện của mình không độc nhất, rằng đau khổ là một phần của cuộc sống, rằng ai cũng có những ẩn ức của mình, kể cả những người đã và đang hành hạ ta. Ý thức này khiến ta bớt thấy lẻ loi, đơn độc, vốn là cảm giác thường trực của người không được yêu thương. Khi hướng cái nhìn ra bên ngoài và thấy những số phận khác, những nỗi đau khác, nỗi đau của ta nhỏ lại. Nó đã được đặt trong một tổng thể đời sống con người rộng lớn hơn, nó không còn khổng lồ, chiếm đoạt toàn bộ không gian và tâm trí của ta nữa. Ta cảm thấy dễ thở hơn, bình tĩnh hơn. Đến lúc này, ta tự nhắc nhở rằng mình hãy dịu dàng với chính mình, hãy chấp nhận bản thân, với tất cả những khiếm khuyết, những vụng về và tổn thương. Nhẹ nhàng với bản thân (self-kindness), theo Neff, chính là yếu tố thứ ba của lòng trắc ẩn với chính mình. Nó giúp ta có thế cư xử với chính mình như với một người bạn quý đang trong một hoàn cảnh khó khăn. Thay vì tự sỉ vả mình là kém cỏi và ngu dốt, ta tự an ủi và động viên. Ta cũng nhắc nhở bản thân về quyền được mưu cầu hạnh phúc của mình, thay vì chạy theo nghĩa vụ sống hộ người khác, dù người đó là cha mẹ mình."
class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        else:
            logging.info("Prevent creating new epd2in7 singleton. Return the former object.") 
        return cls._instances[cls]


class DisplaytoEink(metaclass=SingletonMeta):
    """
        Should be Singleton
    """
    def __init__(self):
        logging.info("Creating new epd2in7 singleton")   
        self.epd = epd2in7.EPD()
        self.epd.init()
        self.epd.Clear(0xFF)
        self.image = Image.new('1', (self.epd.height, self.epd.width), 255)  # 255: clear the frame
        self.imagedraw = ImageDraw.Draw(self.image)

    #def display(self, str):
    #    """
    #    Finally, any singleton should define some business logic, which can be
    #    executed on its instance.
    #    """
    #    self.imagedraw.text((10, 0), str, font = FONT_TEXT, fill = 0)
    #    self.epd.display(self.epd.getbuffer(self.image))
    #    time.sleep(2)

    def __enter__(self):
        logging.info("Entering Eink")
        return self.epd

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.epd.Clear(0xFF)
        epd2in7.epdconfig.module_exit()
        logging.info("Safely clean and exit ")
        if exc_type or exc_value or exc_tb:
            print(exc_type)
            print(exc_value)
            print(exc_tb)
        exit()

import datetime
WIDTH = 264
HEIGH = 176
image = Image.new('1', (WIDTH, HEIGH), 255)  # 255: clear the frame
imagedraw = ImageDraw.Draw(image)
lines = [[]]
from subprocess import check_output
scanoutput = check_output(["iwgetid"]).decode("utf-8").split(":")[1]

IPAddr = check_output(["hostname", "-I"]).decode("utf-8") 
line_number = 0
FONT_SIZE = 18
MAGIC_NUMBER =10
def pagging():
    global line_number
    sample = "Những yếu tố gì cấu thành nên lòng trắc ẩn với chính mình? Chất liệu đầu tiên của nó, thú vị thay, theo nhà tâm lý học Kristin Neff, một nhà nghiên cứu hàng đầu trong lĩnh vực này, là chánh niệm. “Tôi đang đau khổ,” “mình đang bị tổn thương,” chánh niệm giúp chúng ta lùi lại một bước, nhận diện được những gì đang xảy ra bên trong mình mà không phán xét. Bước lùi này quan trọng để chúng ta bước ra ngoài dòng thác của những cảm xúc tiêu cực đang hòng nhấn chìm ta. Yếu tố thứ hai của nó là ý thức rằng câu chuyện của mình không độc nhất, rằng đau khổ là một phần của cuộc sống, rằng ai cũng có những ẩn ức của mình, kể cả những người đã và đang hành hạ ta. Ý thức này khiến ta bớt thấy lẻ loi, đơn độc, vốn là cảm giác thường trực của người không được yêu thương. Khi hướng cái nhìn ra bên ngoài và thấy những số phận khác, những nỗi đau khác, nỗi đau của ta nhỏ lại. Nó đã được đặt trong một tổng thể đời sống con người rộng lớn hơn, nó không còn khổng lồ, chiếm đoạt toàn bộ không gian và tâm trí của ta nữa. Ta cảm thấy dễ thở hơn, bình tĩnh hơn. Đến lúc này, ta tự nhắc nhở rằng mình hãy dịu dàng với chính mình, hãy chấp nhận bản thân, với tất cả những khiếm khuyết, những vụng về và tổn thương. Nhẹ nhàng với bản thân (self-kindness), theo Neff, chính là yếu tố thứ ba của lòng trắc ẩn với chính mình. Nó giúp ta có thế cư xử với chính mình như với một người bạn quý đang trong một hoàn cảnh khó khăn. Thay vì tự sỉ vả mình là kém cỏi và ngu dốt, ta tự an ủi và động viên. Ta cũng nhắc nhở bản thân về quyền được mưu cầu hạnh phúc của mình, thay vì chạy theo nghĩa vụ sống hộ người khác, dù người đó là cha mẹ mình."
    words = sample.split(" ")

    while len(words)>0:
        lines[line_number].append(words[0])
        words.pop(0)
        if sum([len(word) + 1 for word in lines[line_number]])*MAGIC_NUMBER >= WIDTH:
            line_number+=1
            lines.append(list())
pagging()
with DisplaytoEink() as eink:
    while True:
        imagedraw.text((10, 0), f'{datetime.datetime.now().strftime("%H:%M:%S")}', font = FONT_TEXT, fill = 0)
        imagedraw.text((10, 0), str(scanoutput), font = FONT_TEXT, fill = 0)
        imagedraw.text((10, 20), str(IPAddr), font = FONT_TEXT, fill = 0)
        imagedraw.text((10, 40), " ".join(lines[0]), font = FONT_TEXT, fill = 0)
        imagedraw.text((10, 60), " ".join(lines[1]), font = FONT_TEXT, fill = 0)
        # image = Image.open('/home/pi/Python_workspace/lighttick.bmp')
        #epd.display(epd.getbuffer(Himage))
        eink.display(eink.getbuffer(image))
        time.sleep(10)
        eink.Clear(0xFF)
    #print("Current Time =", datetime.now().strftime("%H:%M:%S"))
    #print("something")

"""
try:

    logging.info("epd2in7 Demo")   
    epd = epd2in7.EPD()
    
    '''2Gray(Black and white) display'''
    logging.info("init and Clear")
    epd.init()
    epd.Clear(0xFF)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font35 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 35)
    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...")
    Himage = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Himage)
    draw.text((10, 0), 'hello world', font = font24, fill = 0)
    draw.text((150, 0), u'微雪电子', font = font24, fill = 0)    
    draw.line((20, 50, 70, 100), fill = 0)
    draw.line((70, 50, 20, 100), fill = 0)
    draw.rectangle((20, 50, 70, 100), outline = 0)
    draw.line((165, 50, 165, 100), fill = 0)
    draw.line((140, 75, 190, 75), fill = 0)
    draw.arc((140, 50, 190, 100), 0, 360, fill = 0)
    draw.rectangle((80, 50, 130, 100), fill = 0)
    draw.chord((200, 50, 250, 100), 0, 360, fill = 0)
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)
    
    # Drawing on the Vertical image
    logging.info("2.Drawing on the Vertical image...")
    Limage = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(Limage)
    draw.text((2, 0), 'hello world', font = font18, fill = 0)
    draw.text((20, 50), u'微雪电子', font = font18, fill = 0)
    draw.line((10, 90, 60, 140), fill = 0)
    draw.line((60, 90, 10, 140), fill = 0)
    draw.rectangle((10, 90, 60, 140), outline = 0)
    draw.line((95, 90, 95, 140), fill = 0)
    draw.line((70, 115, 120, 115), fill = 0)
    draw.arc((70, 90, 120, 140), 0, 360, fill = 0)
    draw.rectangle((10, 150, 60, 200), fill = 0)
    draw.chord((70, 150, 120, 200), 0, 360, fill = 0)
    epd.display(epd.getbuffer(Limage))
    time.sleep(2)
    
    logging.info("3.read bmp file")
    Himage = Image.open(os.path.join(picdir, '2in7.bmp'))
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)
    
    logging.info("4.read bmp file on window")
    Himage2 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    bmp = Image.open(os.path.join(picdir, '100x100.bmp'))
    Himage2.paste(bmp, (50,10))
    epd.display(epd.getbuffer(Himage2))
    time.sleep(2)
    
    '''4Gray display'''
    logging.info("4Gray display--------------------------------")
    epd.Init_4Gray()
    
    Limage = Image.new('L', (epd.width, epd.height), 0)  # 255: clear the frame
    draw = ImageDraw.Draw(Limage)
    draw.text((20, 0), u'微雪电子', font = font35, fill = epd.GRAY1)
    draw.text((20, 35), u'微雪电子', font = font35, fill = epd.GRAY2)
    draw.text((20, 70), u'微雪电子', font = font35, fill = epd.GRAY3)
    draw.text((40, 110), 'hello world', font = font18, fill = epd.GRAY1)
    draw.line((10, 140, 60, 190), fill = epd.GRAY1)
    draw.line((60, 140, 10, 190), fill = epd.GRAY1)
    draw.rectangle((10, 140, 60, 190), outline = epd.GRAY1)
    draw.line((95, 140, 95, 190), fill = epd.GRAY1)
    draw.line((70, 165, 120, 165), fill = epd.GRAY1)
    draw.arc((70, 140, 120, 190), 0, 360, fill = epd.GRAY1)
    draw.rectangle((10, 200, 60, 250), fill = epd.GRAY1)
    draw.chord((70, 200, 120, 250), 0, 360, fill = epd.GRAY1)
    epd.display_4Gray(epd.getbuffer_4Gray(Limage))
    time.sleep(2)
    
    #display 4Gra bmp
    Himage = Image.open(os.path.join(picdir, '2in7_Scale.bmp'))
    epd.display_4Gray(epd.getbuffer_4Gray(Himage))
    time.sleep(2)

    logging.info("Clear...")
    epd.Clear(0xFF)
    logging.info("Goto Sleep...")
    epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in7.epdconfig.module_exit()
    exit()
"""