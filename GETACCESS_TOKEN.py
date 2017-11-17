#coding=utf-8
import  requests
"""获取access_token"""
def GetAccess_token(url,param):
    responses=requests.get(url,params=param)
    access_token=eval(responses.text)['access_token']
    return  access_token;

"""调用GetAccess_token()"""

GetAccess_token(url,param);

'''
    def functionname(parameters):
        "函数_文档字符串"
        function_suite
        return [expression]
'''

'''
注释：'''   '''或"""xsww"""
param={'grant_type':'client_credential','appid':'wx17e38aaacef957cb','secret':'9aec0f939e713d5c5cea17ff4bc7662e'}
responses=requests.get('https://api.weixin.qq.com/cgi-bin/token',params =param )
# json格式的字符串可以通过eval函数转换成dict格式
res=eval(responses.text)
access_token=res['access_token']

print  res
print  access_token
print  responses.json()
'''