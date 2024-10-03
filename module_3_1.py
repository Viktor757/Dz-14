calls = 0

def count_calls () :
    global calls
    calls += 1


def  string_info (string):
    stroka = str(string)
    otvet = (len(stroka), stroka.upper(), stroka.lower())
    count_calls()
    return otvet


def  is_contains (string , list_to_search):
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            otvet = True
            break
        else:
            otvet = False
            continue
    return otvet


print(string_info('Praktika'))
print(string_info('Obuchenie'))
print(is_contains('Snikers', ['sniKERS', 'MarS', 'naTS']))
print(is_contains('iphone', ['xiaomi', 'huawei', 'nokia']))
print(calls)

