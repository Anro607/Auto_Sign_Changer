def quote_change(ori):
    print('작은 따옴표 개수 : ' + str(ori.count("'")))
    print('큰 따옴표 개수 : ' + str(ori.count('"')))
    if ori.count("'")%2 == 0 and ori.count('"')%2 == 0:
        change = ori
        quote_list = ["‘", '’']
        quote_list2 = ["“", '”']
        i = 0
        while change.find("'") != -1 :
            change = change[:change.find("'")] + quote_list[i] + change[change.find("'") + 1:]
            if i == 0 :
                i = 1
            else :
                i = 0
        i = 0
        while change.find('"') != -1 :
            change = change[:change.find('"')] + quote_list2[i] + change[change.find('"') + 1:]
            if i == 0 :
                i = 1
            else :
                i = 0
    return print(change)


original = input('원문 입력: ')
quote_change(original)
