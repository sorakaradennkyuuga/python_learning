#このプログラムは、ユーザーが指定した日数、時間、分数を現在の日時に加算し、その結果を表示します。また、現在の日時との差も計算して表示します。
#"datetimeの練習として作成しました。"
import datetime

# 今の日にちから時間を表示させる
now = datetime.datetime.now()  # 今の日時を取得

plus_days = input("何日後の日にちを表示しますか？")  # 何日後にするか入力させる
plus_days = int(plus_days)  # int型に変換

plus_hours = input("それと何時間後の時間を表示しますか？")
plus_hours = int(plus_hours)  # int型に変換

plus_minute = input("それと何分後の時間を表示しますか？")  # 何分後にするか入力させる
plus_minute = int(plus_minute)  # int型に変換

nowtime = now + datetime.timedelta(
    days=plus_days, hours=plus_hours, minutes=plus_minute)

print("その時の日時は", nowtime, "です")

sabun = nowtime - now
print(f"その時間との差は{sabun}です")
