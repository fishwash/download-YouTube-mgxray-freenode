import os
import gdown
import requests
from zipfile import ZipFile

# 设置 网址 和 密码
url = ''
passwd = ''

print('🏄请每月更新视频地址和密码')
print('🏄‍♂️梦歌视频地址：'+url)
print('🏄‍♀️密码：'+passwd)
print('🏄如果卡在这里，请科学上网！')

# 下载
response = requests.get(url)
strResponse = response.text
start = strResponse.find('V2ray+Clash+winxray+ios小火箭，科学上网免费节点订阅下载：https://drive.google.com')
end = strResponse.find('解压码视频内语音播报',start)
urlGoogle = strResponse[start+40:end-1]
print('Google Drive 地址：'+urlGoogle)
urlDownload = 'https://drive.google.com/uc?id=' + urlGoogle[32:urlGoogle.find('/view?usp=share_link')]
output = 'node.zip'
gdown.download(urlDownload, output, quiet=False)
print('已下载'+output)

# 解压
print('解压中...')
def support_gbk(zip_file: ZipFile):
    name_to_info = zip_file.NameToInfo
    # copy map first
    for name, info in name_to_info.copy().items():
        try:
            real_name = name.encode('cp437').decode('gbk')
        except:
            real_name = name.encode('utf-8').decode('utf-8')
        if real_name != name:
            info.filename = real_name
            del name_to_info[name]
            name_to_info[real_name] = info
    return zip_file

with support_gbk(ZipFile(output)) as myzip:
    myzip.extractall(pwd=passwd.encode('utf-8'))


# 删除压缩包
print('解压完毕，删除压缩包')
os.remove(output)
