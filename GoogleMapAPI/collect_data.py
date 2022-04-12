'''
Created on 2022年4月9日

@author: ning_lin
'''
import config as conf

import pandas as pd
import concurrent.futures
from tqdm import tqdm
import time
import random
from selenium import webdriver
import pyproj
options = webdriver.ChromeOptions()
options.add_argument("headless")

TWD97 = pyproj.Proj(init='epsg:3826') #定義TWD97坐標系
WGS84 = pyproj.Proj(init='epsg:4326') #定義WGS84坐標系

def get_twd97_of_addr(browser, address):
    browser.get(conf.get_twd97_url+address)
    time.sleep(2)
    try:
        exact_addr = browser.find_element_by_xpath(
        "//*[@id='LocateBox_FunctionWork_Addr_Reslut']/div[@class='hvrout'][1]").text
        browser.get(conf.get_twd97_url+exact_addr)
        time.sleep(random.randrange(3, 6))
    except:
        pass
    twd97_txt = browser.find_element_by_xpath("//*[@id='Map']/div[1]").text
    twd97_list = twd97_txt.split('\n')
    twd97_list = [i.split('：')[1] for i in twd97_list if '：' in i]
    return twd97_list

def crawl_multiprocessingly(key, group):
    browser = webdriver.Chrome(executable_path='chromedriver', options=options)
    addr_list = group['地址'].values[0].split('、') if '、' in group['地址'].values[0] else [group['地址'].values[0]]
    multi_addr_list = []
    for addr in addr_list:
        twd97_list = get_twd97_of_addr(browser, addr)
        multi_addr_list.append(twd97_list)
        multi_addr_df = pd.DataFrame(multi_addr_list, columns=['詳址', 'TWD97_X', 'TWD97_Y'])
        multi_addr_df['社區名稱'] = key
    browser.quit()
    return multi_addr_df

if __name__ == "__main__":
    data_df = pd.read_excel(conf.data_path)
    #### 將模糊地址資料轉成 TWD97 
    data_lst = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(crawl_multiprocessingly, key, group) for key, group in data_df.groupby('社區名稱')]
        for fut in tqdm(concurrent.futures.as_completed(futures)):
            data_lst.append(fut.result())
    result = pd.concat(data_lst, axis=0)
    #### 將 TWD97 轉成 WGS84
    result['WGS84'] = result.apply(lambda l: pyproj.transform(TWD97, WGS84, l['TWD97_X'], l['TWD97_Y']), axis=1)
    result['WGS84_X'] = result['WGS84'].map(lambda l:l[0])
    result['WGS84_Y'] = result['WGS84'].map(lambda l:l[1])
    result = result.drop(columns = ['WGS84'])
    result.to_csv(conf.latlon_path, index=False)