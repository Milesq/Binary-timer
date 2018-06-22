## @package getTime
# posiada funkcję gettime
#
## zwraca czas
#zwraca czas binarny
# @return list with 3 place - first hours in binary system, second minutes , third seconds
def getTime():
    import time
    from toSystem import toSystem
    def activate(dec, bin):
        i = 0
        for j in bin:
            if j == '1':
                dec[i] = 1
            i += 1
        
    hours = {'dec': [0, 0], 'init': [0, 0, 0, 0]}
    minutes = {'dec': [0, 0, 0], 'init': [0, 0, 0, 0]}
    seconds = {'dec': [0, 0, 0], 'init': [0, 0, 0, 0]}

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

    return {'h': hours, 'm': minutes, 's': seconds}
