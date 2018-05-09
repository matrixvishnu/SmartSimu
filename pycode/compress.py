import glob
import os
import csv
import pandas as pd
from csv import DictReader

os.chdir("C:\\Users\\admin\\PycharmProjects\\AMI\\venv\\output\\loadprofile\\")
results_lp = pd.DataFrame()

for counter, file in enumerate(glob.glob("*.csv")):
    namedf = pd.read_csv(file, skiprows=0)
    results_lp = results_lp.append(namedf)

results_lp.to_csv('C:\\Users\\admin\\PycharmProjects\\AMI\\venv\\output\\loadprofile\\combined_load_profile.csv')


os.chdir("C:\\Users\\admin\\PycharmProjects\\AMI\\venv\\output\\billing_month\\")
results_b_m = pd.DataFrame()
for counter, file in enumerate(glob.glob("mtr*")):
    namedf = pd.read_csv(file, skiprows=0)
    results_b_m = results_b_m.append(namedf)

results_b_m.to_csv('C:\\Users\\admin\\PycharmProjects\\AMI\\venv\\output\\loadprofile\\combined_bill_monthly.csv')

os.chdir("C:\\Users\\admin\\PycharmProjects\\AMI\\venv\\output\\billing_daily\\")
results_b_d = pd.DataFrame()

for counter, file in enumerate(glob.glob("mtr*")):
    namedf = pd.read_csv(file, skiprows=0)
    results_b_d = results_b_d.append(namedf)

results_b_d.to_csv('C:\\Users\\admin\\PycharmProjects\\AMI\\venv\\output\\loadprofile\\combined_bill_daily.csv')
