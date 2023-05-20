import datetime

#Création d'un fichier CSV qui réadapte les data pour être utiliser à l'import

def get_datetime(value):
    data = value.strip().split(' ')
    date = data[0].split('/')
    year = '20%s' % date[2]
    mouth = date[0]
    day = date[1]

    time = data[1].split(':')
    if len(time[0]) == 1:
        hour = '0%s' % time[0]
    else:
        hour = time[0]

    return datetime.datetime(int(year), int(mouth), int(day), int(hour), int(time[1]))

index = 1
data = []
with open("Mint_Packages_V10_to_be_live_Hando.csv") as ff:
    count = 0
    for line in ff:
        data.append(line)
        count += 1
        # if count == 10:
        #     break

date = datetime.datetime.now()
filename = "%s.csv" % (date.strftime('%Y%m%d-%H%M%S'))

f = open(filename, "a")
lines = []
for row in data:
    values = row.split(';')
    line = '%s;%s;%s;%s;%s;%s;%s' % (
        index,
        values[0].lower(),
        values[1].replace(',', '.'),
        values[2].replace(',', '.'),
        get_datetime(values[3]),
        values[4],
        values[5]
    )
    index += 1
    lines.append(line)
f.writelines(lines)
f.close()


