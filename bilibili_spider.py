import urllib.request
import json
import pymysql


def insert_data(title, play, comment, favorites, video_review):
    db = pymysql.connect(host="localhost",
                         user="root",
                         passwd="root",
                         port=3306,
                         db="modian",
                         charset='utf8')
    cursor = db.cursor()
    start = "INSERT INTO bili (title,play,comment,favorites,video_review) VALUES ("
    mid = "','"
    end = ")"
    sql = start + "'" + title + mid + play + mid + comment + mid + favorites + mid + video_review + "'" + end
    # print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("success")
    except:
        # 如果发生错误则回滚
        print("??")
        db.rollback()
    db.close()


def get_html(size, page):
    start = "https://space.bilibili.com/ajax/member/getSubmitVideos?mid=1315101&pagesize="
    end = "&keyword=&order=pubdate"
    response = urllib.request.urlopen(
        start + size + "&tid=0&page=" + page +
        end)
    html = response.read().decode("utf-8")
    json_data = json.loads(html)
    data = json_data["data"]
    v_list = data["vlist"]
    # print(v_list)
    return v_list


v_list = get_html("30", "1")
for i in v_list:
    # print(i)
    insert_data(i["title"], str(i["play"]), str(i["comment"]), str(i["favorites"]), str(i["video_review"]))
