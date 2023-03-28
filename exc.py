'''
Author: SoChichung
Date: 2023-03-28 23:10:50
LastEditors: SoChichung
LastEditTime: 2023-03-28 23:11:15
Description: 

Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
'''
from srtranslator import SrtFile
from srtranslator.translators.deepl import DeeplTranslator
from srtranslator.translators.translatepy import TranslatePy

translator = DeeplTranslator() # or TranslatePy()

filepath = "./filepath/to/srt"
srt = SrtFile(filepath)
srt.translate(translator, "en", "es")

# Making the result subtitles prettier
srt.wrap_lines()

srt.save(f"{os.path.splitext(filepath)[0]}_translated.srt")

translator.quit()