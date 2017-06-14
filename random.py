import random

class Congratulation(object):
	def __init__(self):
		pass
		
	def CatchStu(self, srcfd):
		srcfd = open(srcfd, 'r')
		strlines = srcfd.readlines()
		srclen = len(strlines)
		
		s = random.randint(0, srclen - 1)

		strStu = strlines[s]

		nPos = strlines[s].index('\t')
		nPosEnd = strlines[s].index('\t', nPos + 1)
		print(strlines[s][nPos + 1 : nPosEnd + 1])

	
if __name__ == '__main__':
	test = Congratulation()
	test.CatchStu('g:\\data.txt')