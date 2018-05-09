from meter_data1 import LoadProfile
import os
import input as dt
import datetime
import csv
import pandas as pd
from random import *
import math
from csv import DictReader
import numpy as np
# from compress import Compress

df_mtr_no=pd.read_csv('Mtr_No.csv')
print df_mtr_no
mtr_no=df_mtr_no.mtr_no.tolist()
print mtr_no
startdate=dt.st_date_ip()
enddate=dt.ed_date_ip()

print startdate,enddate

x = LoadProfile()
for i in mtr_no:
    x.mtr_no = i
    x.start_date = startdate
    x.end_date = enddate
    df_lp=x.loadprofile()
    df_bil_m=x.billmonth()
    df_bil_d=x.bil_daily()

    lpf_file=str(i)+'_loadprofile.csv'
    bil_m_file=str(i)+'_bil_monthly.csv'
    bil_d_file = str(i) + '_bil_daily.csv'
    path_lpf= 'C:\\Users\\admin\\PycharmProjects\\AMI\\venv\\output\\loadprofile\\'
    path_bil_m= 'C:\\Users\\admin\\PycharmProjects\\AMI\\venv\\output\\billing_month\\'
    path_bil_d= 'C:\\Users\\admin\\PycharmProjects\\AMI\\venv\\output\\billing_daily\\'
    df_lp.to_csv(path_lpf+lpf_file, index=False)
    df_bil_m.to_csv(path_bil_m+bil_m_file, index=True)
    df_bil_d.to_csv(path_bil_d+bil_d_file, index=True)
# print df_lp
#
# path_lpf = 'C:\\Users\\admin\\PycharmProjects\\AMI\\venv\\output\\loadprofile\\'
# path_bil_m = 'C:\\Users\\admin\\PycharmProjects\\AMI\\venv\\output\\billing_month\\'
# path_bil_d = 'C:\\Users\\admin\\PycharmProjects\\AMI\\venv\\output\\billing_daily\\'
# y=Compress()
# pathl=[path_lpf,path_bil_m,path_bil_d]
# for p in pathl:
#     y.path=p
#     result = y.compress()
#     filename=str(p) + 'compressed.csv'
#     result.to_csv(filename)