#!/usr/bin/python
import datetime
import csv
import pandas as pd
from random import *
import math
from csv import DictReader
import numpy as np

df_lp1 = pd.DataFrame()
df_bil1 = pd.DataFrame()
df_bil_d1 = pd.DataFrame()


class LoadProfile():
    # mtr_no = "mtr123"
    # start_date = datetime.datetime(2018, 01, 01, 00, 00, 00)
    # end_date = datetime.datetime(2018, 04, 13, 12, 12, 12)

    def loadprofile(self):
        range = pd.date_range(self.start_date, self.end_date, freq="30min")
        df_lp = pd.DataFrame(index=range)
        df_lp['Real_Time_clock_date'] = pd.date_range(self.start_date, self.end_date, freq="30min")
        df_lp['mtr_no'] = self.mtr_no
        df_lp['bat_vol'] = np.random.uniform(2, 7, len(df_lp.index)).round(2)
        df_lp['gsm_f_s'] = np.random.uniform(1, 6, len(df_lp.index)).round(2)
        df_lp['tel_ph_no'] = 9995999682
        df_lp['Ir'] = np.random.uniform(15, 25, len(df_lp.index)).round(2)
        df_lp['Iy'] = np.random.uniform(15, 25, len(df_lp.index)).round(2)
        df_lp['Ib'] = np.random.uniform(15, 25, len(df_lp.index)).round(2)
        df_lp['Vr'] = np.random.uniform(220, 260, len(df_lp.index)).round(2)
        df_lp['Vy'] = np.random.uniform(220, 260, len(df_lp.index)).round(2)
        df_lp['Vb'] = np.random.uniform(220, 260, len(df_lp.index)).round(2)
        df_lp['blck_kvah_imp'] = np.random.uniform(0.0200, 0.2100, len(df_lp.index)).round(4)
        df_lp['pf'] = np.random.uniform(0.90, 0.99, len(df_lp.index)).round(2)
        df_lp['blck_kwh_imp'] = df_lp.blck_kvah_imp * df_lp.pf.round(4)
        df_lp['blck_kvah_exp'] = 0
        df_lp['blck_kwh_exp'] = 0
        df_lp['blck_kvarh_q1'] = 0
        df_lp['blck_kvarh_q2'] = np.sqrt(np.power(df_lp.blck_kvah_imp, 2) - np.power(df_lp.blck_kwh_imp, 2)).round(4)
        df_lp['blck_kvarh_q3'] = 0
        df_lp['blck_kvarh_q4'] = 0
        df_lp['Real_Time_clock_date1'] = df_lp['Real_Time_clock_date']
        df_lp['reactive_energy_high'] = np.random.uniform(0.0100, 0.1000, len(df_lp.index)).round(2)
        df_lp['reactive_energy_low'] = np.random.uniform(0.0100, 0.05000, len(df_lp.index)).round(2)
        df_lp['cum_kvah_imp'] = df_lp.blck_kvah_imp.cumsum().round(2)
        df_lp['cum_kvah_exp'] = 0
        df_lp['cum_kwh_imp'] = df_lp.blck_kwh_imp.cumsum().round(2)
        df_lp['cum_kwh_exp'] = 0
        df_lp['cum_kvarh_q2'] = df_lp.blck_kvarh_q2.cumsum().round(2)
        df_lp['cum_kvarh_q1'] = 0
        df_lp['cum_kvarh_q3'] = 0
        df_lp['cum_kvarh_q4'] = 0
        return df_lp
        ########### Billing Data #######################

        ### billing Monthly####
    def billmonth(self):
        df_lp=self.loadprofile()
        df_bil_m = pd.DataFrame()
        df_bil_m['rtc'] = df_bil_m.index
        df_bil_m['pf'] = df_lp.pf.resample('MS').mean()
        df_bil_m['mtr_no'] = self.mtr_no
        # df_bil_m['real_time_clock_date']=
        # df_bil_m['billing_date']=
        df_bil_m['sys_pwr_fact_billing'] = df_lp.pf.resample('MS').mean().round(2)
        df_bil_m['blck_eng_kwh'] = df_lp.blck_kwh_imp.resample('MS').sum().round(2)
        df_bil_m['cum_eng_kwh'] = df_bil_m.blck_eng_kwh.cumsum().round(2)
        df_bil_m['cum_eng_kwh_tz_1'] = (df_bil_m.cum_eng_kwh / 16).round(2)
        df_bil_m['cum_eng_kwh_tz_2'] = (df_bil_m.cum_eng_kwh / 16).round(2)
        df_bil_m['cum_eng_kwh_tz_3'] = (df_bil_m.cum_eng_kwh / 4).round(2)
        df_bil_m['cum_eng_kwh_tz_4'] = (df_bil_m.cum_eng_kwh / 8).round(2)
        df_bil_m['cum_eng_kwh_tz_5'] = (df_bil_m.cum_eng_kwh / 4).round(2)
        df_bil_m['cum_eng_kwh_tz_6'] = (df_bil_m.cum_eng_kwh / 8).round(2)
        df_bil_m['cum_eng_kwh_tz_7'] = (df_bil_m.cum_eng_kwh / 16).round(2)
        df_bil_m['cum_eng_kwh_tz_8'] = (df_bil_m.cum_eng_kwh / 16).round(2)
        df_bil_m['blck_eng_kvah'] = df_lp.blck_kvah_imp.resample('MS').sum().round(2)
        df_bil_m['cum_eng_kvah'] = df_bil_m.blck_eng_kvah.cumsum().round(2)
        df_bil_m['cum_eng_kvah_tz_1'] = (df_bil_m.cum_eng_kvah / 16).round(2)
        df_bil_m['cum_eng_kvah_tz_2'] = (df_bil_m.cum_eng_kvah / 16).round(2)
        df_bil_m['cum_eng_kvah_tz_3'] = (df_bil_m.cum_eng_kvah / 4).round(2)
        df_bil_m['cum_eng_kvah_tz_4'] = (df_bil_m.cum_eng_kvah / 8).round(2)
        df_bil_m['cum_eng_kvah_tz_5'] = (df_bil_m.cum_eng_kvah / 4).round(2)
        df_bil_m['cum_eng_kvah_tz_6'] = (df_bil_m.cum_eng_kvah / 8).round(2)
        df_bil_m['cum_eng_kvah_tz_7'] = (df_bil_m.cum_eng_kvah / 16).round(2)
        df_bil_m['cum_eng_kvah_tz_8'] = (df_bil_m.cum_eng_kvah / 16).round(2)
        df_bil_m['cum_eng_kvarh_lag'] = np.sqrt(np.power(df_bil_m.cum_eng_kvah, 2) - np.power(df_bil_m.cum_eng_kwh, 2)).round(
            2)
        df_bil_m['cum_eng_kvarh_lead'] = 0
        df_bil_m['md_kw'] = df_bil_m.blck_eng_kwh.resample('MS').max().round(2)
        df_bil_m['md_kw_tz_1'] = (df_bil_m.md_kw / 16).round(2)
        df_bil_m['md_kw_tz_2'] = (df_bil_m.md_kw / 16).round(2)
        df_bil_m['md_kw_tz_3'] = (df_bil_m.md_kw / 4).round(2)
        df_bil_m['md_kw_tz_4'] = (df_bil_m.md_kw / 8).round(2)
        df_bil_m['md_kw_tz_5'] = (df_bil_m.md_kw / 4).round(2)
        df_bil_m['md_kw_tz_6'] = (df_bil_m.md_kw / 8).round(2)
        df_bil_m['md_kw_tz_7'] = (df_bil_m.md_kw / 16).round(2)
        df_bil_m['md_kw_tz_8'] = (df_bil_m.md_kw / 16).round(2)
        df_bil_m['md_kva'] = df_lp.blck_kvah_imp.resample('D').sum().resample('MS').max().round(2)
        df_bil_m['md_kva_tz_1'] = (df_bil_m.md_kva / 16).round(2)
        df_bil_m['md_kva_tz_2'] = (df_bil_m.md_kva / 16).round(2)
        df_bil_m['md_kva_tz_3'] = (df_bil_m.md_kva / 4).round(2)
        df_bil_m['md_kva_tz_4'] = (df_bil_m.md_kva / 8).round(2)
        df_bil_m['md_kva_tz_5'] = (df_bil_m.md_kva / 4).round(2)
        df_bil_m['md_kva_tz_6'] = (df_bil_m.md_kva / 8).round(2)
        df_bil_m['md_kva_tz_7'] = (df_bil_m.md_kva / 16).round(2)
        df_bil_m['md_kva_tz_8'] = (df_bil_m.md_kva / 16).round(2)
        df_bil_m['cum_eng_kwh_exp'] = 0
        df_bil_m['cum_eng_kvah_exp'] = 0
        df_bil_m['cum_eng_kvarh_q1'] = 0
        df_bil_m['cum_eng_kvarh_q2'] = df_bil_m.cum_eng_kvarh_lag.round(2)
        df_bil_m['cum_eng_kvarh_q3'] = 0
        df_bil_m['cum_eng_kvarh_q4'] = 0
        return df_bil_m
        ######Daily billing data############
    def bil_daily(self):
        df_lp=self.loadprofile()
        df_bil_d = pd.DataFrame()
        df_bil_d['rtc'] = df_bil_d.index
        df_bil_d['pf'] = df_lp.pf.resample('D').mean()
        df_bil_d['mtr_no'] = self.mtr_no
        df_bil_d['sys_pwr_fact_billing'] = df_lp.pf.resample('D').mean().round(2)
        df_bil_d['blck_eng_kwh'] = df_lp.blck_kwh_imp.resample('D').sum().round(2)
        df_bil_d['cum_eng_kwh'] = df_bil_d.blck_eng_kwh.cumsum().round(2)
        df_bil_d['cum_eng_kwh_tz_1'] = (df_bil_d.cum_eng_kwh / 16).round(2)
        df_bil_d['cum_eng_kwh_tz_2'] = (df_bil_d.cum_eng_kwh / 16).round(2)
        df_bil_d['cum_eng_kwh_tz_3'] = (df_bil_d.cum_eng_kwh / 4).round(2)
        df_bil_d['cum_eng_kwh_tz_4'] = (df_bil_d.cum_eng_kwh / 8).round(2)
        df_bil_d['cum_eng_kwh_tz_5'] = (df_bil_d.cum_eng_kwh / 4).round(2)
        df_bil_d['cum_eng_kwh_tz_6'] = (df_bil_d.cum_eng_kwh / 8).round(2)
        df_bil_d['cum_eng_kwh_tz_7'] = (df_bil_d.cum_eng_kwh / 16).round(2)
        df_bil_d['cum_eng_kwh_tz_8'] = (df_bil_d.cum_eng_kwh / 16).round(2)
        df_bil_d['blck_eng_kvah'] = df_lp.blck_kvah_imp.resample('D').sum().round(2)
        df_bil_d['cum_eng_kvah'] = df_bil_d.blck_eng_kvah.cumsum().round(2)
        df_bil_d['cum_eng_kvah_tz_1'] = (df_bil_d.cum_eng_kvah / 16).round(2)
        df_bil_d['cum_eng_kvah_tz_2'] = (df_bil_d.cum_eng_kvah / 16).round(2)
        df_bil_d['cum_eng_kvah_tz_3'] = (df_bil_d.cum_eng_kvah / 4).round(2)
        df_bil_d['cum_eng_kvah_tz_4'] = (df_bil_d.cum_eng_kvah / 8).round(2)
        df_bil_d['cum_eng_kvarh_lag'] = np.sqrt(
            np.power(df_bil_d.cum_eng_kvah, 2) - np.power(df_bil_d.cum_eng_kwh, 2)).round(2)
        df_bil_d['cum_eng_kvarh_lead'] = 0
        df_bil_d['md_kw'] = df_bil_d.blck_eng_kwh.max().round(2)
        df_bil_d['md_kw_tz_1'] = (df_bil_d.md_kw / 16).round(2)
        df_bil_d['md_kw_tz_2'] = (df_bil_d.md_kw / 16).round(2)
        df_bil_d['md_kw_tz_3'] = (df_bil_d.md_kw / 4).round(2)
        df_bil_d['md_kw_tz_4'] = (df_bil_d.md_kw / 8).round(2)
        df_bil_d['md_kw_tz_5'] = (df_bil_d.md_kw / 4).round(2)
        df_bil_d['md_kw_tz_6'] = (df_bil_d.md_kw / 8).round(2)
        df_bil_d['md_kw_tz_7'] = (df_bil_d.md_kw / 16).round(2)
        df_bil_d['md_kw_tz_8'] = (df_bil_d.md_kw / 16).round(2)
        df_bil_d['md_kva'] = df_bil_d.blck_eng_kvah.max().round(2) #df_lp.blck_kvah_imp.resample('D').sum().resample('D').max().round(2)

        df_bil_d['md_kva_tz_1'] = (df_bil_d.md_kva / 16).round(2)
        df_bil_d['md_kva_tz_2'] = (df_bil_d.md_kva / 16).round(2)
        df_bil_d['md_kva_tz_3'] = (df_bil_d.md_kva / 4).round(2)
        df_bil_d['md_kva_tz_4'] = (df_bil_d.md_kva / 8).round(2)
        df_bil_d['md_kva_tz_5'] = (df_bil_d.md_kva / 4).round(2)
        df_bil_d['md_kva_tz_6'] = (df_bil_d.md_kva / 8).round(2)
        df_bil_d['md_kva_tz_7'] = (df_bil_d.md_kva / 16).round(2)
        df_bil_d['md_kva_tz_8'] = (df_bil_d.md_kva / 16).round(2)
        df_bil_d['cum_eng_kwh_exp'] = 0
        df_bil_d['cum_eng_kvah_exp'] = 0
        df_bil_d['cum_eng_kvarh_q1'] = 0
        df_bil_d['cum_eng_kvarh_q2'] = df_bil_d.cum_eng_kvarh_lag.round(2)
        df_bil_d['cum_eng_kvarh_q3'] = 0
        df_bil_d['cum_eng_kvarh_q4'] = 0
        return df_bil_d
    def output(self):
        global df_lp1
        df_lp1 = df_lp1.append(self.loadprofile())
        global df_bil1
        df_bil1 = df_bil1.append(self.billmonth())
        global df_bil_d1
        df_bil_d1 = df_bil_d1.append(self.bil_daily())

    # df_lp.to_csv("load_prof_v_101.csv", index=False)
    # df_bil_m.to_csv("billing_v_101.csv", index=True)


# x = LoadProfile()
# meters = ['AD52007', 'AD52011', 'AD52016', 'AD52017', 'AD52020']
# for i in meters:
#     x.mtr_no = i
#     x.start_date = datetime.datetime(2018, 04, 01, 00, 00, 00)
#     x.end_date = datetime.datetime(2018, 04, 10, 12, 12, 12)
#     x.output()
# # loadprofile("mtr1234",datetime.datetime(2017,03,04,00,00,00))
# df_lp1.to_csv("DTR_2300v_load_prof_v_101.csv", index=False)
# df_bil1.to_csv("DTR_230v_bil_monthly.csv", index=True)
# df_bil_d1.to_csv("DTR_230v_bil_daily.csv", index=True)
# print df_lp1