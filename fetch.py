import pylab as pl
import numpy as np
def fetch_csv(inputfile, adj = True):
    output = np.genfromtxt(inputfile,delimiter=",")
    output = output[1:,1:]
    if adj == True:
        output = split_adj(output)
    return output

def split_adj(stock):
    myshape = stock.shape
    if myshape[1] < 6:
        return stock
    else:
        for i in range(0,len(stock)):
            ratio = stock[i,5]/stock[i,3]
            for j in range(0,4):
                stock[i,j] *= ratio
            stock[i,4] /= ratio
        return stock

def plot_stock(stock):
    pl.figure()
    pl.plot(range(0,len(stock)),stock[:,3][::-1])
    pl.show()
    