for line in open("signed_artists.csv", encoding='utf-8'):
    strlist = line.split(',')
    artist_name = strlist[0].replace(' ', '')
    artist_id = strlist[1]
    user_id = strlist[2]