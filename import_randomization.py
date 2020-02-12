with open('randomization_list.csv', newline='', encoding='utf-8-sig') as imported_csv:
    rando_list = imported_csv.read().splitlines()
rando_list = [int(i) for i in rando_list]
