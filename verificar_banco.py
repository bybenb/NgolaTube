import sqlite3


conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()


cursor.execute("SELECT * FROM videos")
videos = cursor.fetchall()

for vio in videos:
    for video in vio:
        print(video, end="\n")
    print("")

conexao.close()
# 2-5-14-25
