new_list = []
with open('1.txt', encoding="utf-8") as f:
    import os
    f_name = os.path.basename('pythonProject3/1.txt')

    f = f.readlines()
    for line in f:
        line = line.strip('\n')
        new_list.append(line)
        list_len = len(new_list)
    new_list.insert(0, f_name)
    new_list.insert(1, list_len)
    #print(new_list)

new_list_2 = []
with open('2.txt', encoding="utf-8") as f:
    import os
    f_name = os.path.basename('pythonProject3/2.txt')

    f = f.readlines()
    for line in f:
        line = line.strip('\n')
        new_list_2.append(line)
        list_len = len(new_list_2)
    new_list_2.insert(0, f_name)
    new_list_2.insert(1, list_len)
    #print(new_list_2)

new_list_3 = []
with open('3.txt', encoding="utf-8") as f:
    import os
    f_name = os.path.basename('pythonProject3/3.txt')

    f = f.readlines()
    for line in f:
        line = line.strip('\n')
        new_list_3.append(line)
        list_len = len(new_list_3)
    new_list_3.insert(0, f_name)
    new_list_3.insert(1, list_len)
    #print(new_list_3)

# new_list_5 = []
# new_list_5.append(new_list)
# new_list_5.append(new_list_2)
# new_list_5.append(new_list_3)
# new_list_5.sort(reverse=True)
# print(new_list_5)

with open('4.txt', 'w', encoding='utf-8') as f_4:
    if len(new_list) < len(new_list_2) and len(new_list) < len(new_list_3):
        f_4.write('\n'.join(str(line) for line in new_list))
        f_4.write('\n')
    elif len(new_list_2) < len(new_list) and len(new_list_2) < len(new_list_3):
        f_4.write('\n'.join(str(line) for line in new_list_2))
        f_4.write('\n')
    elif len(new_list_3) < len(new_list) and len(new_list_3) < len(new_list_2):
        f_4.write('\n'.join(str(line) for line in new_list_3))
        f_4.write('\n')
    if len(new_list_2) > len(new_list) > len(new_list_3) or len(new_list_2) < len(new_list) < len(new_list_3):
        f_4.write('\n'.join(str(line) for line in new_list))
        f_4.write('\n')
    elif len(new_list) > len(new_list_2) > len(new_list_3) or len(new_list_2) > len(new_list) and len(new_list_2) < len(
            new_list_3):
        f_4.write('\n'.join(str(line) for line in new_list_2))
        f_4.write('\n')
    elif len(new_list) > len(new_list_3) > len(new_list_2) or len(new_list_3) > len(new_list) and len(new_list_3) < len(
            new_list_2):
        f_4.write('\n'.join(str(line) for line in new_list_3))
        f_4.write('\n')
    if len(new_list) > len(new_list_2) and len(new_list) > len(new_list_3):
        f_4.write('\n'.join(str(line) for line in new_list))
        f_4.write('\n')
    elif len(new_list_2) > len(new_list) and len(new_list_2) > len(new_list_3):
        f_4.write('\n'.join(str(line) for line in new_list_2))
        f_4.write('\n')
    elif len(new_list_3) > len(new_list) and len(new_list_3) > len(new_list_2):
        f_4.write('\n'.join(str(line) for line in new_list_3))
        f_4.write('\n')





