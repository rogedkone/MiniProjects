def converterStrToTelegram(str):
    for i in str.split("\n"):
        if i != "":
            print(f"```{i}.py```")
        else:
            print("")
# Путь глав в stepik курсе, который конвертируется в ```n.n.n.py``` для телеграмма. 1.1.2 -> ```1.1.2.py```
vale = '''
1.1.2
'''
print(converterStrToTelegram(vale))
