import datetime

if __name__ == "__main__":
    today = datetime.date.today()
    another = datetime.date(today.year, 6, 24)
    print(another - today)
