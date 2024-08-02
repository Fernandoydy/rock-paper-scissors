brl = 0.17
eur = 1.08
jpy = 0.0067
cad = 0.72

currencies = [brl, eur, jpy, cad]

currency1 = None
currency2 = None
quantity = None



def converter():
    global currencies
    global currency1
    global currency2
    global quantity
    
    input = int(input('Choose the FIRST currency \nYou have: \nBRL: 0\nEUR: 1 \nJPY: 2 \nCAD: 3 \n'))
    '''currency1 = currencies[input]
    input = int(input('HOW MUCH?\n'))
    quantity = input
    input = int(input('Choose the SECOND currency \nYou have: \nBRL: 0\nEUR: 1 \nJPY: 2 \nCAD: 3 \n'))
    currency2 = currencies[input]'''

    #currency1 * quantity



converter()