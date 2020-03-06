import urllib3
import os
from urllib import parse
import ast
import zipfile
http = urllib3.PoolManager()
root = 'C:/Users/brucelee/Documents/python'
url='http://thm.market.xiaomi.com/thm/download/v2/'
url2 = 'http://zhuti.xiaomi.com/detail/7d5e9aba-315c-410f-b933-3aec192357f1'
url3 = url+url2.split('/')[-1]
response = http.request('GET', url3)
user_dict = ast.literal_eval(response.data.decode())
downloadUrl=user_dict.get('apiData')['downloadUrl']
tname = downloadUrl.split('/')[-1].split('-')[0]
tname = parse.unquote(tname)
# print(downloadUrl)
response = http.request('GET', downloadUrl)
with open(root+'/'+tname+'.zip', 'wb') as f:
    f.write(response.data)
response.release_conn()
print('下载完成')
z = zipfile.ZipFile(root+'/'+tname+'.zip', 'r')
# print(z.filelist)
z.extract('wallpaper/default_wallpaper.jpg',root)
os.rename(root+'/wallpaper/default_wallpaper.jpg', root+'/wallpaper/'+tname+'.jpg')
