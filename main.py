from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson

data = readfromjson("info.json")
print(json2xml.Json2xml(data).to_xml())