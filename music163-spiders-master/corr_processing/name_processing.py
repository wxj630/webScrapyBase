import re

def fuzzyfinder(user_input, collection):
    suggestions = []
    pattern = '.*'.join(user_input)  # Converts 'djm' to 'd.*j.*m'
    regex = re.compile(pattern)  # Compiles a regex.
    for item in collection:
        match = regex.search(item)  # Checks if the current item matches the regex.
        if match:
            suggestions.append(item)
    return suggestions

#
name_list=[]
id_list=[]
for line in open("all_closeness.csv", encoding='utf-8'):
    strlist = line.split(',')
    singer_id = strlist[0].strip(' ')
    singer_name1 = strlist[1].replace(' ','')
    id_list.append(singer_id)
    name_list.append(singer_name1)

print(id_list)
print(name_list)

for line in open("events_follows_fans_num.csv", encoding='utf-8'):
    strlist = line.split(',')
    singer_name2 = strlist[0].replace(' ', '')
    events = strlist[1]
    follows = strlist[2]
    fans = strlist[3].strip('\n')
    if singer_name2 in name_list:
        with open('singer_count.csv','a+',encoding='utf-8') as f:
            f.write(str(name_list.index(singer_name2)+1)+','+singer_name2+','+events+','+follows+','+fans+'\n')

