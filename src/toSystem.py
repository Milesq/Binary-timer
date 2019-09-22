## @package toSystem
## funkcja
def invert(num):
	num = str(num)
	ret = ''
	for i in reversed(num):
		ret += i
	return ret

def toSystem(num, podst = 2):
	ret = ''
	while num != 0:
		ret += str(int(num % podst))
		num = int(num / podst)
	return invert(ret)