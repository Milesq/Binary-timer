import time
from toSystem import toSystem
def getTime():
    def activate(dec, bin):
        i = 0
        for j in bin:
            if j == '1':
                dec[i] = True
            i += 1
        
    hours = {'dec': [False, False], 'init': [False, False, False, False]}
    minutes = {'dec': [False, False, False], 'init': [False, False, False, False]}
    seconds = {'dec': [False, False, False], 'init': [False, False, False, False]}

    H, M, S = time.strftime("%H"), time.strftime("%M"), time.strftime("%S")

    Hbin, Mbin, Sbin = [toSystem(int(H[0])), toSystem(int(H[1]))], [toSystem(int(M[0])), toSystem(int(M[1]))],[toSystem(int(S[0])), toSystem(int(S[1]))]

    # we have 3 variables, H M S 
    # time in binary system

    activate(hours['dec'], Hbin[0])
    activate(hours['init'], Hbin[1])

    activate(minutes['dec'], Mbin[0])
    activate(minutes['init'], Mbin[1])

    activate(seconds['dec'], Sbin[0])
    activate(seconds['init'], Sbin[1])
