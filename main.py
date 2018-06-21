from ball import ball
import time
from toSystem import toSystem

def activateBall(dec, bin):
    i = 0
    for j in bin:
        if j == '1':
            dec[i].setActive()
        i += 1
    
hours = {'dec': [ball(), ball()], 'init': [ball(), ball(), ball(), ball()]}
minutes = {'dec': [ball(), ball(), ball()], 'init': [ball(), ball(), ball(), ball()]}
seconds = {'dec': [ball(), ball(), ball()], 'init': [ball(), ball(), ball(), ball()]}

H, M, S = time.strftime("%H"), time.strftime("%M"), time.strftime("%S")

Hbin, Mbin, Sbin = [toSystem(int(H[0])), toSystem(int(H[1]))], [toSystem(int(M[0])), toSystem(int(M[1]))],[toSystem(int(S[0])), toSystem(int(S[1]))]

# we have 3 variables, H M S 
# time in binary system

activateBall(hours['dec'], Hbin[0])
activateBall(hours['init'], Hbin[1])

activateBall(minutes['dec'], Mbin[0])
activateBall(minutes['init'], Mbin[1])

activateBall(seconds['dec'], Sbin[0])
activateBall(seconds['init'], Sbin[1])

for hour in hours['dec']:
    print(hour.bgcolor)

print()
for hour in hours['init']:
    print(hour.bgcolor)