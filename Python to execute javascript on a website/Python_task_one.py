import urllib.request
import urllib.parse
from selenium import webdriver
driver = webdriver.Chrome()
try:
    url= 'https://s3-us-west-1.amazonaws.com/ra-training/test1.html'
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    saveFile= open('readData.txt','w')
    saveFile.write(str(respData))
    saveFile.close()
    driver.get(url)
    p_element = driver.find_element_by_id(id_='innerHTMLtxt')
    respData1= p_element.text
    saveFile=open('saveJavascript.txt','w')
    saveFile.write(str(respData1))
    saveFile.close()
except Exception as e:
        print(str(e))
