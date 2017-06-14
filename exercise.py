'''
Python写一个统计学生考试成绩的分数段的函数：
ScoreCount();满分为100分，分数段为0-9.10-19
20-29…..90-99.100的11个段。
'''
'''
def ScoreCount():
	lists = [0] * 11
	while (1):
		try:
			grade = int(input())
			if(grade >= 0 and grade <= 100):
				lists[int(grade/10)] += 1
			else:
				print(lists)
				break
		except ValueError:
			print("not int,input again")
	return
	
if __name__ == '__main__':
	ScoreCount();
'''

