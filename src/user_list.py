import datetime

files = [
    './data/user/legend.csv',
    './data/user/mint_package.csv',
    './data/user/og_pet.csv',
    './data/user/unstaked.csv',
]

def extractDistinctWallet():
    user_wallets = [];
    for file in files:
        with open(file) as ff:
            for wallet in ff:
                if wallet not in user_wallets:
                    wallet = wallet.replace('\n', '')
                    user_wallets.append(wallet)
    return user_wallets

wallets = extractDistinctWallet()


date = datetime.datetime.now()
filename = "%s_users.csv" % (date.strftime('%Y%m%d-%H%M%S'))
f = open(filename, "a")
lines = []
index = 1
for wallet in wallets:
    line = '%s;%s;%s;%s;%s\n' % (
        index,
        wallet,
        1,
        date.strftime('%Y-%m-%d %H:%M:%S'),
        date.strftime('%Y-%m-%d %H:%M:%S')
    )
    index += 1
    lines.append(line)
f.writelines(lines)
f.close()