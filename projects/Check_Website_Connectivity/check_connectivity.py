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
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            status = requests.get(website, headers=headers).status_code
            # status = requests.get(website).status_code
            if status == 200:
                status_dict[website] = "Working"
            else:
                print(status)
                status_dict[website] = "Not Working"
    # print(status_dict)
    
    with open(targetFileName, "w", newline="") as fw:
        csv_writer = csv.writer(fw)
        for key in status_dict.keys():
            csv_writer.writerow([key, status_dict[key]])
            

if __name__ == "__main__":
    check()