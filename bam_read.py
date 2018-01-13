# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 19:38:12 2018

@author: wongwow
"""

import pandas as pd
import sqlite3

# read the table name
#db = sqlite3.connect("./data/20170509-bam-crowd-only-xQ3gXol5UR.sqlite")
#cur = db.cursor()
#cur.execute("select name from sqlite_master where type='table'")  
#col_name_list = [tuple[0] for tuple in cur]  
#print(col_name_list)
#cur.close()

#result :'crowd_labels', 'crowd_raw_hits', 'crowd_raw_choices', 'crowd_raw_captions', 'modules', 'scores'

#CREATE TABLE modules (
#        mid int primary key,
#        project_id int,
#        src text,
#        mature_content boolean,
#        license text);

#CREATE TABLE scores (
#    mid int,
#    content_bicycle real, content_cat real,      content_tree real,
#    emotion_scary real,   media_oilpaint real,   content_bird real,
#    content_dog real,     emotion_gloomy real,   media_3d_graphics real,
#    media_pen_ink real,   content_building real, content_flower real,
#    emotion_happy real,   media_comic real,      media_vectorart real,
#    content_cars real,    content_people real,   emotion_peaceful real,
#    media_graphite real,  media_watercolor real
#);

#CREATE TABLE crowd_labels (
#    mid int,
#    attribute text,
#    label text,
#    primary key (mid, attribute)
#);
#CREATE TABLE crowd_raw_hits (
#    assignment_id text,
#    attribute text,
#    worker_id text,
#    n_clicks int,
#    n_seconds real,
#    last_modified text
#);
#CREATE TABLE crowd_raw_choices (
#    assignment_id text,
#    mid int,
#    attribute text,
#    label bool
#);
#CREATE TABLE crowd_raw_captions (
#    assignment_id text,
#    mid int,
#    attribute text,
#    caption text,
#    label bool
#);


#col_name_list = [tuple[0] for tuple in cur.description]  


#df = pd.read_sql("select * from scores", sqlite3.connect("./data/20170509-bam-crowd-only-xQ3gXol5UR.sqlite"), index_col="mid")

#df = pd.read_sql("select * from crowd_labels", sqlite3.connect("./data/20170509-bam-crowd-only-xQ3gXol5UR.sqlite"), index_col="mid")

#df = pd.read_sql("select * from crowd_raw_choices", sqlite3.connect("./data/20170509-bam-crowd-only-xQ3gXol5UR.sqlite"), index_col="mid")

#df = pd.read_sql("select * from crowd_raw_captions", sqlite3.connect("./data/20170509-bam-crowd-only-xQ3gXol5UR.sqlite"), index_col="mid")

#df = pd.read_sql("select * from crowd_raw_hits", sqlite3.connect("./data/20170509-bam-crowd-only-xQ3gXol5UR.sqlite"))

#df = pd.read_sql("select mid, caption from crowd_raw_captions where attribute = 'content_cat' and label=1 limit 10", sqlite3.connect("./data/20170509-bam-crowd-only-xQ3gXol5UR.sqlite"))

#df = pd.read_sql("select * from modules", sqlite3.connect("./data/20170509-bam-crowd-only-xQ3gXol5UR.sqlite"))


#print(df)



# select * from crowd_labels
# Index attribute label 
# (393022 rows x 2 columns)

# select * from crowd_raw_choices
# 819476 rows x 3 columns
# Index assignment_id attribute label

# select * from crowd_raw_captions
# Index assignment_id attribute caption label
# 74582 rows x 4 columns

# select * from crowd_raw_hits
# Index assignment_id attribute worker_id n_clicks n_seconds last_modified
# 24314 rows x 6 columns

#select * from modules

# 389040 x 5 



############  20170509-bam-2.2m-Nja9G.sqlite
#db_name = "20170509-bam-1m-18UThu3ICM.sqlite"
#db_path =  "./data/" + db_name
#db = sqlite3.connect(db_path)
#cur = db.cursor()
#cur.execute("select name from sqlite_master where type='table'")  
#col_name_list = [tuple[0] for tuple in cur]  
#print(col_name_list)
#cur.close()

#df = pd.read_sql("select * from modules", sqlite3.connect(db_path))
#print(df)

#['crowd_labels', 'crowd_raw_hits', 'crowd_raw_choices', 
#'crowd_raw_captions', 'modules', 'scores']
#[1379284 rows x 5 columns]


db_name = "20170509-bam-2.2m-Nja9G.sqlite"
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

df = pd.read_sql("select * from modules limit 10", sqlite3.connect(db_path))
print(df)
#[2289817 rows x 5 columns]