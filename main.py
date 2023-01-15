import requests

proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}
domain = 'https://gradua11y.145321.xyz/'
login_url = domain + 'api/v1/passport/auth/login'
admin_path = domain + 'api/v1/admin/config/fetch'

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/108.0.0.0 '
                      'Safari/537.36'}
post_data = {'email': 'test@gmail.com',
             'password': '12345678',
             }

resp = requests.post(url=login_url, data=post_data, headers=headers, proxies=proxies, timeout=20)
auth_data = resp.json()['data']['auth_data']
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) '
                  'Chrome/108.0.0.0 '
                  'Safari/537.36', 'Authorization': auth_data}

# resp1 = requests.get(url=userinfo_link, headers=header, proxies=proxies, timeout=20)
resp2 = requests.get(url=admin_path, headers=header, proxies=proxies, timeout=20)
# print(resp2.text)
admin_link = domain + resp2.json()["data"]["frontend"]["frontend_admin_path"]
print("后台路径为：" + admin_link)
