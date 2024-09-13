import datetime
def calc():
    global burth_year
    burth_year = int(input("Enter burth year: ").strip())  # لإدخال سنة ميلاد المستخدم
    global burth_monthe
    burth_monthe = int(input("Enter burth monthe: ").strip())  # لإدخال شهر ميلاد المستخدم
    global burth_day
    burth_day = int(input("Enter burth day: ").strip())   # لإدخال يوم ميلاد المستخدم
    global data
    data = datetime.datetime(burth_year, burth_monthe, burth_day)   # لتجميع تاريخ ميلاد المستخدم
    now = datetime.datetime.now() # لجلب التاريخ الحالي
    global now_year
    now_year = int(datetime.datetime.now().year)    # لجلب تاريخ السنة الحالية
    global now_mounth
    now_mounth = int(datetime.datetime.now().month) # لجلب تاريخ الشهر الحالية
    global now_day
    now_day = int(datetime.datetime.now().day)    # لجلب تاريخ اليوم الحالية
    global tot
    tot = (now - data).days # لجلب عدد أيام حياة المستخدم

def calc2():
    global burth_hour
    burth_hour = int(input("Enter burth hour: ").strip())  # لإدخال ساعة ميلاد المستخدم
    global burth_minute
    burth_minute = int(input("Enter burth minute: ").strip())   # لإدخال دقيقة ميلاد المستخدم
    global burth_secend
    burth_secend = int(input("Enter burth secend: ").strip())   # لإدخال ثانية ميلاد المستخدم

def now():
    now = datetime.datetime.now() # لجلب التاريخ الحالي
    global now_year
    now_year = int(datetime.datetime.now().year)    # لجلب تاريخ السنة الحالية
    global now_mounth
    now_mounth = int(datetime.datetime.now().month) # لجلب تاريخ الشهر الحالية
    global now_day
    now_day =    int(datetime.datetime.now().day)    # لجلب تاريخ اليوم الحالية
    global now_hour
    now_hour = int(datetime.datetime.now().hour)    # لجلب الساعة  الحالية
    global now_minute
    now_minute = int(datetime.datetime.now().minute)
    global now_secend
    now_secend = int(datetime.datetime.now().second)

    global tot
    tot = (now - data).days  # لجلب عدد أيام حياة المستخدم

while True:
    try:
        print("1- لإدخال السنة واالشهر واليوم والساعة والدقيقة والثانية")
        print("2- لإدخال السنة واالشهر واليوم")
        select = int(input("enter 1 or 2 ? "))
    except:
        print("erorr")
    try:
        if select == 1:
            while True:
                try:
                    calc()
                    calc2()
                    now()
                    data = datetime.datetime(burth_year, burth_monthe, burth_day, burth_hour, burth_minute, burth_secend)   # لتجميع تاريخ ميلاد المستخدم
                    if now_year == burth_year and burth_monthe == now_mounth and burth_day > now_day:  # لعدم كتابة تارخ بالسالب
                        print("هذا التاريخ غير موجود")
                        continue
                    elif now_year == burth_year and burth_monthe > now_mounth:  # لعدم كتابة تارخ بالسالب
                        print("هذا التاريخ غير موجود")
                        continue
                    elif now_year < burth_year:  # لعدم كتابة تارخ بالسالب
                        print("هذا التاريخ غير موجود")
                        continue

                    age = int(tot / 365.25)  # لحساب  سنين العمر
                    monthe = int(age * 12)  # لحساب  شهور العمر
                    week = int(tot / 7)  # لحساب  أسابيع العمر
                    day = int(tot)  # لحساب  أيام العمر
                    hour = int((tot * 24) + datetime.datetime.now().hour -  burth_hour )  # لحساب  ساعات العمر
                    minute = int((hour * 60) + datetime.datetime.now().minute - burth_minute)  # لحساب  دقائق العمر
                    secend = int((minute * 60) + datetime.datetime.now().second - burth_secend)  # لحساب  ثواني العمر

                    print(f'age= {age} year. ')
                    print(f'weeks   = {week} week.')
                    print(f'monthes = {monthe:,} monthes.')
                    print(f'days    = {day:,} days.')
                    print(f'minutes  = {minute:,} minutes .')
                    print(f'secends = {secend:,} secends.')
                except:
                    print("Erorr Try agine.")

        elif select == 2:
            while True:
                try:
                    calc()
                    if now_year == burth_year and burth_monthe == now_mounth and burth_day > now_day:  # لعدم كتابة تارخ بالسالب
                        print("هذا التاريخ لم يأتي بعد")
                        continue
                    elif now_year == burth_year and burth_monthe > now_mounth:  # لعدم كتابة تارخ بالسالب
                        print("هذا التاريخ لم يأتي بعد")
                        continue
                    elif now_year < burth_year:  # لعدم كتابة تارخ بالسالب
                        print("هذا التاريخ لم يأتي بعد")
                        continue

                    age = int(tot / 365.25)  # لحساب  سنين العمر
                    monthe = int(age * 12)  # لحساب  شهور العمر
                    week = int(tot / 7)  # لحساب  أسابيع العمر
                    day = int(tot)  # لحساب  أيام العمر
                    hour = int((tot * 24) + datetime.datetime.now().hour)  # لحساب  ساعات العمر
                    minet = int((hour * 60) + datetime.datetime.now().minute)  # لحساب  دقائق العمر
                    secend = int((minet * 60) + datetime.datetime.now().second)  # لحساب  ثواني العمر

                    print(f'age= {age}سنة. ')
                    print("يا اللي ضاع من عمرك سنين")
                    print(f'weeks   = {week} أسبوع.')
                    print(f'monthes = {monthe:,}شهر .')
                    print(f'days    = {day:,} يوم.')
                    print(f'minets  = {minet:,} دقيقة تقريباً.')
                    print(f'secends = {secend:,} ثانية تقريبا.')
                except:
                    print("Erorr Try agine.")
        else:
            print("erorr please press 1 or 2 only")
    except:
        print("Erorr Try agine.")
#by_mohamed_galal