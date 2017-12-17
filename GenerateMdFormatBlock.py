# coding=utf-8
import codecs
import operator
fileName="Coverage"

vertical='|'
def run():
	arr=['Integer','Double','Byte','Float','Short','Long','Boolean','String']
	with codecs.open(fileName+".java",'r','utf-8') as f:
		file=createFile()
		writeHead(file,'参数','是否必须','类型','描述')
		writeLine(file,'center','center','center','left')
		for line in f.readlines():
			str=line.strip()
			if str.find('private')==0:
				for type in arr:
					getCode(str,type,file)
		file.close() 
	readFile()
			
	
def getCode(str,type,file):
	arrs=[]
	if str.find(type)>-1:
		if str.find(';')>-1:
			parameter=str[str.find(type)+len(type)+1:str.find(';')]
			arrs.append(parameter)
			arrs.append('是')
			arrs.append(translateToChinese(type))
		a=str.find('//')
		if a>-1:
			description=str[a+2:len(str)]
			arrs.append(description)
		writeTr(file,arrs)
		   
		   
def writeTr(file,arrs):
	str='|'
	black='    '
	for att in arrs:
		str=str+att+black+vertical
	str+='\n'
	file.write(str)
	
def writeHead(file,*arrs):
	str='|'
	black='    '
	for att in arrs:
		str+=att+black+vertical
	str+='\n'
	file.write(str)

def writeLine(file,*line):
	str='|'
	left=':------------|'
	right='------------:|'
	center=':------------:|'
	for att in line:
		if operator.eq(att,'left'):
			str+=left
		if operator.eq(att,'right'):
			str+=right
		if operator.eq(att,'center'):
			str+=center
	str+='\n'
	file.write(str)
	
def translateToChinese(english):
	chinese=''
	if operator.eq(english,'Double') or operator.eq(english,'double'):
		chinese='浮点型'
	elif operator.eq(english,'Float') or operator.eq(english,'float'):
		chinese='浮点型'
	elif operator.eq(english,'String') or operator.eq(english,'string'):
		chinese='字符型'
	elif operator.eq(english,'Integer') or operator.eq(english,'int'):
		chinese='整型'
	elif operator.eq(english,'Short') or operator.eq(english,'short'):
		chinese='整型'
	elif operator.eq(english,'Long') or operator.eq(english,'long'):
		chinese='整型'
	elif operator.eq(english,'Boolean') or operator.eq(english,'boolean'):
		chinese='布尔型'
	elif operator.eq(english,'Byte') or operator.eq(english,'byte'):
		chinese='二进制'
	else:
		chinese='未知'
	
	return chinese
	
	
def readFile():
	with codecs.open(fileName+".md",'r','utf-8') as f:
		print(f.read())

def createFile():
	file=open(fileName+".md",'w+',encoding='utf-8')
	return file	

def main():
	run()

if __name__=="__main__":
	main()