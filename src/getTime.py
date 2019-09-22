import time


def gettime():

    def activate(dec, bin):
        i = 0
        for j in bin:
            if j == '1':
                dec[i] = '●'
            i += 1

    hours = {'dec': ['○', '○'], 'init': ['○', '○', '○', '○']}
    minutes = {'dec': ['○', '○', '○'], 'init': ['○', '○', '○', '○']}
    seconds = {'dec': ['○', '○', '○'], 'init': ['○', '○', '○', '○']}

    H, M, S = time.strftime("%H"), time.strftime("%M"), time.strftime("%S")

    tobin = lambda x: ''.join(bin(int(x))[2:])

    Hbin = [tobin(H[0]), tobin(H[1])]
    Mbin = [tobin(M[0]), tobin(M[1])]
    Sbin = [tobin(S[0]), tobin(S[1])]

    # we have 3 variables, H M S
    # time in binary system

    activate(hours['dec'], Hbin[0])
    activate(hours['init'], Hbin[1])

    activate(minutes['dec'], Mbin[0])
    activate(minutes['init'], Mbin[1])

    activate(seconds['dec'], Sbin[0])
    activate(seconds['init'], Sbin[1])

    return {'h': hours, 'm': minutes, 's': seconds}
