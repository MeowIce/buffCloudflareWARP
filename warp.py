import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
script_version = '3'
window_title = f"CLOUDFLARE WARP HACK"
os.system('title ' + window_title if os.name == 'nt' else 'PS1="\[\e]0;' +
          window_title + '\a\]"; echo $PS1')
os.system('cls' if os.name == 'nt' else 'clear')
print(
    'Script buff data Cloudflare WARP+. By MeowIce \n'
)
print("[I] Buff GB Cloudfalre WARP+")
referrer = input("[#] Vui long nhap WARP+ ID (KHONG PHAI KEY !!)/Please enter your WARP+ ID (NOT THE KEY):")


def progressBar():
    percent = 0
    while True:
        for i in range(10):
            percent += 1
            sys.stdout.write(f"\r[P] Dang cho phan hoi/Waiting for response...  " +
                             f" {percent}%")
            sys.stdout.flush()
            time.sleep(0.075)
        if percent == 100:
            sys.stdout.write("\r[S] Yeu cau thanh cong/Request successful 100%")
            break


def genString(stringLength):
    try:
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(stringLength))
    except Exception as error:
        print(error)


def digitString(stringLength):
    try:
        digit = string.digits
        return ''.join((random.choice(digit) for i in range(stringLength)))
    except Exception as error:
        print(error)


url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'


def run():
    try:
        install_id = genString(22)
        body = {
            "key": "{}=".format(genString(43)),
            "install_id": install_id,
            "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
            "referrer": referrer,
            "warp_enabled": False,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
            "type": "Android",
            "locale": "es_ES"
        }
        data = json.dumps(body).encode('utf8')
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Host': 'api.cloudflareclient.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.12.1'
        }
        req = urllib.request.Request(url, data, headers)
        response = urllib.request.urlopen(req)
        status_code = response.getcode()
        return status_code
    except Exception as error:
        print("")
        print(error)


g = 0
b = 0
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print("")
    print(f"\n[I] Dang chay bang ID/Running on ID: {referrer}")
    sys.stdout.write("\r[P] Dang gui yeu cau/Sending request... 0%")
    sys.stdout.flush()
    result = run()
    if result == 200:
        g += 1
        progressBar()
        print(f"\n[S] {g} GB da duoc them vao tai khoan cua ban.")
        print(f"\n[S] {g} GB has been successfully added to your account.")
        print(f"[T] Tong/Total: {g} OK {b} BAD")
        print(f"[I] Dang nap dan... Vui long doi 8s.")
        print(f"[I] Refreshing... Please wait 8s.")
        for i in range(1, 0, -1):
            time.sleep(8)
    else:
        b += 1
        print("[E] Loi khi ket noi den may chu.")
        print("[E] Error when connecting to server.")
        print(f"[T] Tong/Total: {g} OK {b} BAD")
        for i in range(1, 0, -1):
            sys.stdout.write(f"\r[I] Thu lai trong 10s/Retry in 10s...")
            sys.stdout.flush()
            time.sleep(10)
