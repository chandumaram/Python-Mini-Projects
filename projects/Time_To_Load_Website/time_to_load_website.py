from urllib.request import urlopen
import time

def get_load_time(url):
    if ("https" or "http") in url:
        open_url = urlopen(url)
    else:
        open_url = urlopen("https://"+url)
    start_time = time.time() # Time stamp before reading the url
    open_url.read() # reading the url
    end_time = time.time() # Time stamp after reading the url
    open_url.close()
    time_to_load = end_time - start_time
    return time_to_load


if __name__ == "__main__":
    url = input("Enter the url whose loading time you want to check: ")
    loadtime = get_load_time(url)
    print(f"\nThe time taken to load {url} is {loadtime} seconds.")