'''
Created on 2022年4月11日

@author: ning_lin
'''
import config as conf
import pandas as pd
import time
import random
import concurrent.futures
from tqdm import tqdm
from selenium import webdriver

pd.set_option('max_columns', 50)
options = webdriver.ChromeOptions()
options.add_argument("headless")

def calculate_distance_multiprocessingly(addr):
    browser = webdriver.Chrome(executable_path='chromedriver', options=options)
    browser.get(conf.distance_url.format(addr, conf.destination))
    time.sleep(random.randrange(3,6))
    distance_str = browser.find_element_by_xpath("//*[@id='section-directions-trip-0']").text
    distance_int = int(distance_str.split('分')[0])
    browser.quit()
    return [addr, distance_int]

if __name__ == '__main__':
    raw_df = pd.read_excel(conf.data_path)
    latlon_df = pd.read_csv(conf.latlon_path)

    data_lst = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(calculate_distance_multiprocessingly, addr) for addr in latlon_df['詳址'].values]
        for fut in tqdm(concurrent.futures.as_completed(futures)):
            data_lst.append(fut.result())

    distance_df = pd.DataFrame(data_lst, columns=['詳址', '距目的地(分)'])
    distance_df = pd.merge(distance_df, latlon_df, on='詳址', how='left')
    final_df = pd.merge(raw_df, distance_df, on='社區名稱', how='right')
    final_df.to_csv(conf.final_path, index=False)