import csv
import requests
import os

status_dict = {"Website": "Status"}
sourceFileName = "websites.txt"
targetFileName = "website_status.csv"

def check():
    with open("websites.txt", "r") as fr:
        for line in fr:
            website = line.strip()
            status = requests.get(website).status_code
            if status == 200:
                status_dict[website] = "Working"
            else:
                status_dict[website] = "Not Working"
    # print(status_dict)
    
    with open(targetFileName, "w", newline="") as fw:
        csv_writer = csv.writer(fw)
        for key in status_dict.keys():
            csv_writer.writerow([key, status_dict[key]])
            

if __name__ == "__main__":
    check()