#coding=utf-8
#Lession 1 数据库学习
import MySQLdb
conn = MySQLdb.connect(host='localhost', user='root',passwd='sun35741',charset="utf8")
cursor = conn.cursor()
count = cursor.execute('select * from jg_zjqs.bz_zxls') 
print  '共有 %s条数据' % count 
result = cursor.fetchone(); 
print result
print 'ID: %s info: %s' % (result[0],result[1])


