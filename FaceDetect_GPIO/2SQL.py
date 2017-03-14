filename = sys.argv[1]+".txt"
f = open(filename,"r").readlines()
data = []
for i in f : 
	#.strip('\n\r'): skip "\n" and "\r"
	#.split(','):make string to array,like: "1,1,1" -> ["1","1","1"]
	# print i.strip('\n\r').split(',')
	data.append(i.strip('\n\r').split(','))

SqlText=""

#sql config-action
SqlText+=data[0][0]+" `"+data[0][1]+"` ("

#sql config-structature
for i in range(len(data[1])):
	if i!=0:
		SqlText+=","
	SqlText+="`"+data[1][i]+"`"

SqlText+=") VALUES\n"
#sql config-end
#sql data
for i in range(len(data)):
	if i>2:			
		SqlText+="("
		for q in range(len(data[i])):
			if q!=0:
				SqlText+=","
			SqlText+=data[i][q]	
		if i==len(data)-1:
			SqlText+=");"
		else:
			SqlText+="),\n"

#open("test.txt",'a') -> add
#open("test.txt",'w') -> new
#open("test.txt",'r') -> read
w = open("output_"+filename,'w')
w.writelines(SqlText)
w.close()
