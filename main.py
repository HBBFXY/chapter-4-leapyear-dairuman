try:
    year = int(input("请输入年份："))
    # 判断是否为闰年
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"{year} 是闰年")
    else:
        print(f"{year} 不是闰年")
except ValueError:
    print("输入的年份含有非数字字符，请输入正确的年份数字")# 在此处编写代码
