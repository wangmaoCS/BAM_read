# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:19:50 2018

@author: wongwow
"""

import pandas as pd
import sqlite3
import requests
import os
import numpy as np

db_name = "20170509-bam-crowd-only-xQ3gXol5UR.sqlite"
#db_name = "20170509-bam-1m-18UThu3ICM.sqlite"
#db_name = "20170509-bam-2.2m-Nja9G.sqlite"

db_path =  "./data/" + db_name
db = sqlite3.connect(db_path)
cur = db.cursor()
cur.execute("select name from sqlite_master where type='table'")  
col_name_list = [tuple[0] for tuple in cur]  
print(col_name_list)
cur.close()

#Table name :
#['crowd_labels', 'crowd_raw_hits', 'crowd_raw_choices', 
#'crowd_raw_captions', 'modules', 'scores']

df = pd.read_sql("select * from modules", sqlite3.connect(db_path))

url_path = df['src']
num_img = len(url_path)

cur_url = url_path[0]
print(cur_url)

error_list = []
cur_idx = np.load('error_list_bam_img.npy')

for k1 in range(len(cur_idx)):
    error_list.append(cur_idx[k1])

for k in range(1000,2000):
    url_img = url_path[k]

    save_path_img = './img/%07d.jpg' % k       
    
    save_path     = save_path_img
    url           = url_img
    
    try:
        if not os.path.exists(save_path):       
            r = requests.get(url)
            r.raise_for_status()            
            with open(save_path,'wb') as f:
                f.write(r.content)
                f.close()
    except:
        print("img download error: k=%d" % k)
        error_list.append(k)
        continue
    print(k)
    
np.save('error_list_bam_img.npy',error_list)