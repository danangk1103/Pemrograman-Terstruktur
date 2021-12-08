from datetime import *
tgl = '2021-12-24'
def diffDate(x):
    target = datetime.strptime(x, '%Y-%m-%d')
    skrg = datetime.strptime(str(datetime.date(datetime.now())), '%Y-%m-%d')
    selisih = target - skrg
    return selisih.days

diffDate(tgl)