# from meter_data import LoadProfile
import datetime
# import csv
# import pandas as pd
# from random import *
# import math
# from csv import DictReader
# import numpy as np

# df_lp1 = pd.DataFrame()
# df_bil1 = pd.DataFrame()
# df_bil_d1 = pd.DataFrame()


# y = LoadProfile()
# meters = ['AD52007', 'AD52011', 'AD52016', 'AD52017', 'AD52020']
# st_date=0
# ed_date=0
def st_date_ip():
    print 'enter start date'
    yy=int(input('yy'))
    mm=int(input('mm'))
    dd=int(input('dd'))
    hh=int(input('hh'))
    mn=int(input('mn'))
    ss=int(input('ss'))
    # startdate_entry=input('eneter start date in form of yy,mm,dd,hh,mn,ss')
    # yy,mm,dd,hh,mn,ss= map(int, startdate_entry.split(','))
    startdate=datetime.datetime(yy, mm, dd, hh, mn, ss)
    return startdate
def ed_date_ip():
    print 'enter end date'
    yy=int(input('yy'))
    mm=int(input('mm'))
    dd=int(input('dd'))
    hh=int(input('hh'))
    mn=int(input('mn'))
    ss=int(input('ss'))
# enddate_entry=raw_input('eneter end date in form of yy,mm,dd,hh,mn,ss')
# yy,mm,dd,hh,mn,ss= enddate_entry.split(',')
    enddate=datetime.datetime(yy, mm, dd, hh, mn, ss)
    return enddate
    # global st_date
    # global ed_date
    # st_date=startdate
    # ed_date=enddate



# date_ip()
# print st_date,ed_date
# for i in meters:
#     y.mtr_no = i
#     y.start_date = startdate
#     y.end_date = enddate
#     y.loadprofile()
# # loadprofile("mtr1234",datetime.datetime(2017,03,04,00,00,00))
# df_lp1.to_csv("IP_2300v_load_prof_v_101.csv", index=False)
# df_bil1.to_csv("IP_230v_bil_monthly.csv", index=True)
# df_bil_d1.to_csv("IP_230v_bil_daily.csv", index=True)