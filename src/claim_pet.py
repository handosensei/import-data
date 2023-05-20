import datetime

# Quantity 1
file_guardian = './data/claim_pet/guardian.csv'
file_judge = './data/claim_pet/judge.csv'
file_og = './data/claim_pet/og.csv'
file_whale = './data/claim_pet/whale.csv'

# Quantity each held NFT
file_council = './data/claim_pet/council.csv'
file_honorary = './data/claim_pet/honorary.csv'

# Quantity by nb token mint package
file_mint = './data/claim_pet/mint.csv'

files= [
    { 'path': file_guardian, 'type': 'guardian', 'quantity': 'one'},
    { 'path': file_judge, 'type': 'judge', 'quantity': 'one'},
    { 'path': file_og, 'type': 'og', 'quantity': 'one'},
    { 'path': file_whale, 'type': 'whale', 'quantity': 'one'},
    { 'path': file_council, 'type': 'council', 'quantity': 'multi'},
    { 'path': file_honorary, 'type': 'honorary', 'quantity': 'multi'},
    { 'path': file_mint, 'type': 'mint', 'quantity': 'multi'},
]

def getData(file):
    data = []
    with open(file) as ff:
        for line in ff:
            data.append(line)
    return data

def getInitClaimPet():
    return {
        'council': 0,
        'guardian': 0,
        'honorary': 0,
        'judge': 0,
        'mint': 0,
        'og': 0,
        'whale': 0,
    }

claim_data = {}
wallets = []
for file in files:
    data = getData(file['path'])
    if file['quantity'] == 'one':
        for row in data:
            wallet = row.replace('\n', '')
            if wallet not in claim_data:
                wallets.append(wallet)
                claim_data[wallet] = getInitClaimPet()
            claim_data[wallet][file['type']] += 1
    else:
        for row in data:
            row = row.replace('\n', '')
            values = row.split(';')
            wallet = values[0]
            quantity = values[1]
            if wallet not in claim_data:
                wallets.append(wallet)
                claim_data[wallet] = getInitClaimPet()
            claim_data[wallet][file['type']] += int(quantity)

date = datetime.datetime.now()
filename = "%s_claim_pet.csv" % (date.strftime('%Y%m%d-%H%M%S'))
f = open(filename, "a")
lines = []
index = 1
for wallet in wallets:
    rewards = claim_data[wallet]
    line = '%s;%s;%s;%s;%s;%s;%s;%s;%s\n' % (
        index,
        wallet,
        rewards['council'],
        rewards['guardian'],
        rewards['honorary'],
        rewards['judge'],
        rewards['mint'],
        rewards['og'],
        rewards['whale']
    )
    index += 1
    lines.append(line)
f.writelines(lines)
f.close()

