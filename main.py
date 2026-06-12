@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉", "中吉", "小吉", "吉", "半吉",
        "末吉", "末小吉", "凶", "小凶", "大凶"
    ]
    # 辞書型で返すように変更
    return {"result": omikuji_list[random.randrange(10)]}
