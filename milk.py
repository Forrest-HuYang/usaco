"""
ID: tony_hu1
PROG: milk
LANG: PYTHON3
"""
def read_in(infile):
    a = []
    with open(infile) as filename:
        for line in filename:
            a.append(line.rstrip())
    return a

def milk_main(filein):
    plan = filein[0].split(' ')
    quantity = int(plan[0])
    num_farmers = int(plan[1])
    price_quantity = {}
    list_price = []
    for i in range(1,num_farmers+1):
        a = filein[i].split(' ')
        price = int(a[0])
        if price in price_quantity:
            price_quantity[price] += int(a[1])
        else:
            price_quantity[price] = int(a[1])
            list_price.append(price)
    list_price.sort()
    return greedy(list_price,price_quantity,quantity)

def greedy(list_price,price_quantity,quantity):
    purchased = 0
    total_price = 0
    for i in range(len(list_price)):
        price = list_price[i]
        purchased += price_quantity[price]
        total_price += price_quantity[price]*price
        if purchased >= quantity:
            total_price -= (purchased-quantity)*price
            return total_price
    return 0
            
def write_out(outfile,outstring):
    fout = open (outfile, 'w')
    fout.write(str(outstring)+'\n')

write_out('milk.out',milk_main(read_in('milk.in')))