import re
import json

from helpers.file_helpers import *


# data = readDataFromTextFile('demofile.txt')
# saveDataToTextFile(data, filename)

data = readDataFromJsonFile('const/proxies.json')
saveDataToJsonFile(data, 'const/tmp.json')
