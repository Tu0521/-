password = input("請輸入密碼：")

# 統計計數器
upper_count = 0
lower_count = 0
digit_count = 0

# 遍歷每個字元
for ch in password:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1
    elif ch.isdigit():
        digit_count += 1

# 輸出統計結果
print(f"大寫字母個數：{upper_count}")
print(f"小寫字母個數：{lower_count}")
print(f"數字個數：{digit_count}")

# 判斷密碼等級（只看是否存在，不計個數）
has_upper = upper_count > 0
has_lower = lower_count > 0
has_digit = digit_count > 0

category_count = has_upper + has_lower + has_digit

if category_count == 3:
    print("密碼等級：強")
elif category_count == 2:
    print("密碼等級：中")
else:
    print("密碼等級：弱")
