# coding=utf-8
# FTP操作
import ftplib
import sys
import time
import os

host = '10.8.2.129'
username = 'hszjqs'
password = 'hszjqs#888'

bufsize = 1024  # 设置缓冲器大小

ftp = ftplib.FTP(host)  # 实例化FTP对象
ftp.login(username, password)  # 登录

# 欢迎信息
print(ftp.getwelcome().encode('latin1').decode('GBK'))

today = time.strftime("%Y%m%d", time.localtime())

# FTP服务器路径
sever_path = "/1013/直销核对数据/" + today

# 需要传递的文件列表
file_list = ['交易确认查询.xls' ,'交易申请查询.xls','柜台资金存入查询.xls'] 

# 上传文件地址
upload_path = 'M:\\5-数据复核岗\\' + today + '\\'

# 下载文件地址
download_path = 'Z:\\33-2数据复核岗业务流程\\直销核对数据\\' + today + '\\'


def ftp_upload(file):
    
    # 创建远程目录
    try:
        ftp.dir(sever_path.encode('GBK').decode('latin1'))
    except ftp.error as e:
        print(e)
        ftp.mkd(sever_path.encode('GBK').decode('latin1'))
    
    # 进入远程目录
    ftp.cwd(sever_path.encode('GBK').decode('latin1'))
    # 取得当前目录地址
    pwd_path = ftp.pwd()
    print("FTP当前路径:", pwd_path.encode('latin1').decode('GBK'))
    
    fp = open(upload_path + file, 'rb', bufsize)
    
    print(file.encode('utf-8'))
    print(file.encode('utf-8').decode('latin1'))
    
    ftp.storbinary('STOR %s' % file.encode('GBK').decode('latin1'), fp, bufsize)
    fp.close()


def ftp_download(file):
    
    isExists=os.path.exists(download_path.rstrip("\\"))
    if not isExists:
        os.makedirs(download_path)
    # 进入远程目录
    ftp.cwd(sever_path.encode('GBK').decode('latin1'))
    
    fp = open(download_path + file, 'wb')
    ftp.retrbinary('RETR %s' % file.encode('GBK').decode('latin1'), fp.write, bufsize)
    fp.close()


# 系统默认编码
# print(sys.getdefaultencoding())
#for f in file_list :
#    ftp_upload(f)
#ftp_download()
for f in file_list :
    ftp_download(f)

ftp.quit()

