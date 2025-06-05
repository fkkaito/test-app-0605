import random

def generate_runner_data():
    # ダミーの選手名リスト
    names = [
        "田中太郎", "佐藤花子", "鈴木次郎", "高橋美咲", "伊藤健一",
        "山本陽子", "中村翔", "小林優子", "加藤大輔", "吉田真理",
        "松本拓也", "井上彩", "林健太", "清水香織", "森田直樹",
        "橋本美奈", "山田一郎", "石川真由美", "前田亮", "藤田美穂",
        "後藤誠", "岡田奈々", "村上智也", "長谷川舞", "近藤翔太",
        "坂本由美", "遠藤健", "青木美咲", "西村大輔", "福田真理",
        "三浦拓也", "藤井彩", "岡本健太", "中島香織", "原田直樹",
        "大野美奈", "武田一郎", "木村真由美", "石田亮", "金子美穂",
        "小川誠", "山崎奈々", "池田智也", "柴田舞", "安藤翔太",
        "宮崎由美", "川口健", "松田美咲", "平野大輔", "菊池真理"
    ]

    # タイムをランダムに生成
    runners = [{"name": name, "time": round(random.uniform(9.56, 12.99), 2)} for name in names]
    
    # タイムが良い順に並び替え
    sorted_runners = sorted(runners, key=lambda x: x["time"])
    
    return sorted_runners

def main():
    runners = generate_runner_data()
    print("100M走の結果（タイムが良い順）:")
    for i, runner in enumerate(runners, start=1):
        print(f"{i}位: {runner['name']} - {runner['time']}秒")

if __name__ == "__main__":
    main()