while True:
    var_name = input("請輸入變數名稱（輸入 exit 結束）：")
    
    if var_name == "exit":
        print("程式結束。")
        break
    
    if var_name.isidentifier():
        print("格式合法")
    else:
        print("格式錯誤，請重新輸入")
