def invert(tab):
	ret = []
	for i in reversed(tab):
		ret.append(i)
	return ret
def getTemplate():
     return '''
 {1[3]}   {3[3]}  {5[3]}
 {1[2]} {2[2]}{3[2]} {4[2]}{5[2]}
{0[1]}{1[1]} {2[1]}{3[1]} {4[1]}{5[1]}
{0[0]}{1[0]} {2[0]}{3[0]} {4[0]}{5[0]}
     '''
def getDisplayText(time):
    tmplt = getTemplate()

    hoursDec = invert(time['h']['dec'])
    hoursInit = invert(time['h']['init'])
        
    minutesDec = invert(time['m']['dec'])
    minutesInit = invert(time['m']['init'])
        
    secondsDec = invert(time['s']['dec'])
    secondsInit = invert(time['s']['init'])
    return tmplt.format(hoursDec, hoursInit, minutesDec, minutesInit, secondsDec, secondsInit)
    # return hoursDec, hoursInit, minutesDec, minutesInit, secondsDec, secondsInit