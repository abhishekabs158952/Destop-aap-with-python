import tkinter
from tkinter import *
import pandas as pd
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process 
import os 
from tkinter.ttk import *
os.system('clear')

def buttonPressThenWork():
	pgbar['value'] = 50
	myLable2['text']='2%'
	enterLabel = Label(root,text=" Work in progress... ")
	enterLabel.pack()
	print("i m in")
	df = pd.read_csv("Mappedsku.csv")

	df2=pd.DataFrame()
	df2["Distributor Item code"] = df["Distributor Item code"]
	df2["DITdsort"]="9999x9999"
	df2["DITcsort"]=""

	checkCD=0

	for ind in df2.index:
		itemCode=df2['Distributor Item code'][ind]
		check_type=isinstance(itemCode,float)
		if(check_type):
			continue
		checkCD=0
		ccheck1=""
		dcheck1=""
		dcheck1temp=""
		spaceval=0
		spacevalafterd=0
		dmencnt=0
		getdv=0
		for values in itemCode:
			if(values==" "):
				spaceval=1
			if(spaceval==1):
				if(values=="1"):
					checkCD=2
				elif(values=="2"):
					checkCD=2
				elif(values=="3"):
					checkCD=2
				elif(values=="4"):
					checkCD=2
				elif(values=="6"):
					checkCD=2
				elif(values=="8"):
					checkCD=2
			if(checkCD==0):
				ccheck1+=values
			if(checkCD==2):
				if(values==" "):
					if(getdv==0):
						spacevalafterd=1
						ccheck1+=dcheck1
						dcheck1=""
						continue
					if(dmencnt>6):
						break
				if(values=="X"):
					dcheck1+="x"
					getdv=1
					continue
				elif(values=="*"):
					dcheck1+="x"
					continue
				dcheck1+=values
				dmencnt+=1
		#print(ccheck1,dcheck1)
		if(dcheck1==""):
			dcheck1="9999x9999"
		df2.loc[(df2['Distributor Item code'] == itemCode),['DITcsort','DITdsort'] ] =  ccheck1,dcheck1
	pgbar['value'] = 10
	myLable2['text']='10%'
	df2.sort_values(by=['DITdsort','DITcsort'] , inplace=True)
	df2 = df2.reset_index(drop=True)
#	df2.to_csv('csv_example')

	print("done 2")

	df3=pd.DataFrame()
	df3["Company Dscription"] = df["Company Dscription"]
	df3["CDdsort"]="8888x8888"
	df3["CDcsort"]=""

	for ind in df3.index: 
		Companydes=df['Company Dscription'][ind]
		dcheck2=""
		ccheck2=""
		dcheck2cnt=0
		totake1=0
		for values1 in Companydes:
			if(totake1==0):
				if(values1=="3"):
					totake1=2;
			if(totake1==1):
				if(values1=="-"):
					break
			if(values1==" "):
				if(dcheck2!=""):
					totake1=1
				elif(totake1==4):
					totake1=1
			if(values1==" "):
				if(totake1==0):
					totake1=2
				continue
			if(totake1==1):
				ccheck2 +=values1
			if(totake1==2):
				if(dcheck2cnt>5):
					if(values1=="-"):	
						totake1=4
						continue
					elif(values1=="1"):
						totake1=4
						continue
					elif(values1==" "):
						totake1=4
						continue
				if(values1=="X"):
					dcheck2+="x"
					dcheck2cnt+=1
					continue
				elif(values1=="*"):
					dcheck2+="x"
					dcheck2cnt+=1
					continue
				dcheck2+=values1
				dcheck2cnt+=1
		#print(ccheck2,dcheck2)
		if(dcheck2!=""):
			df3.loc[(df3['Company Dscription'] == Companydes),['CDcsort','CDdsort'] ] =  ccheck2,dcheck2

	df3.sort_values(by=['CDdsort','CDcsort'] , inplace=True)
	df3 = df3.reset_index(drop=True)
#	df3.to_csv('csv_example2')
	pgbar['value'] = 20
	myLable2['text']='20%'
	print("done 3")

	df4=pd.DataFrame()

	df4['DITdsort']=df2["DITdsort"]
	df4["Distributor Item code"]=""
	df4["Company Dscription"]=""

	indexValForDf4=0
	i=2
	maxindex2=0
	array = [0]
	maxindex=0
	while i < len(df3.index):
		forstartloop=0
		firstfor=0
		secondfor=0
		entervalue=0
		entervalue2=0
		for ind1 in df3.index:
			if(forstartloop==0):
				tempDimVal = df3['CDdsort'][ind1]
				forstartloop=1
			if(df3['CDdsort'][ind1]==tempDimVal):
				entervalue=1
				if(indexValForDf4<15822):
					df4["Company Dscription"][indexValForDf4]=df3['Company Dscription'][ind1]
				else:
					df4.loc[indexValForDf4]=['','',df3['Company Dscription'][ind1]]
				indexValForDf4+=1
				firstfor+=1
				df3=df3.drop([ind1])
			elif(entervalue==1):
				break
		maxindex=indexValForDf4
		indexValForDf4-=firstfor
		for ind1 in df2.index:
			if(df2['DITdsort'][ind1]==tempDimVal):
				entervalue2=1
				if(indexValForDf4<15822):	
					df4["Distributor Item code"][indexValForDf4]=df2["Distributor Item code"][ind1]
				elif(indexValForDf4<=maxindex):
					df4["Distributor Item code"][indexValForDf4]=df2["Distributor Item code"][ind1]
				else:
					df4.loc[indexValForDf4]=['',df2["Distributor Item code"][ind1],'']
				indexValForDf4+=1
				secondfor+=1
				df2=df2.drop([ind1])
			elif(entervalue2==1):
				break
		indexValForDf4-=secondfor
		if(firstfor>secondfor):
			indexValForDf4+=firstfor
		else:
			indexValForDf4+=secondfor
		maxindex=indexValForDf4
		array.append(indexValForDf4)
		pgbar['value'] = indexValForDf4*7/2000
		myLable2['text']='30%...'
		print(indexValForDf4)
	
	print("yes their2")
	for ind in df2.index:
	#	entervalue2=1
	#	print("yes their3" , indexValForDf4)
		if(indexValForDf4<15822):
			df4["Distributor Item code"][indexValForDf4]=df2["Distributor Item code"][ind]
		else:
			df4.loc[indexValForDf4]=['',df2["Distributor Item code"][ind1],'']
		indexValForDf4+=1
	#	secondfor+=1
		df2=df2.drop([ind])
	array.append(indexValForDf4-1)
	pgbar['value'] = 70
	myLable2['text']='70%'
	#print(indexValForDf4)
	#df4.to_csv('csv_example4')
	#print(array)



	df4 = df4.reset_index(drop=True)



	i=1
	while i < len(array):
		firstValArr=array[0]
		print("workind",firstValArr)
		secondValArr=array[1]
		check_type=isinstance(df4["Distributor Item code"][firstValArr],float)
		check_type2=isinstance(df4["Company Dscription"][firstValArr],float)
		diff=secondValArr - firstValArr
		diff/=4
		if(diff<1):
			diff=1
		if(check_type):
			array.pop(0)
			continue
		if(check_type2):
			array.pop(0)
			continue

		j=firstValArr
		while j<secondValArr:
			check_type3=isinstance(df4["Distributor Item code"][j],float)
			if(check_type3):
				#array.pop(0)
				break
			k=j
			val1=0
			storeKvalue=k
			while k<secondValArr:
				print(secondValArr,k)
				print(type(df4["Company Dscription"][k]))
				print(df4["Company Dscription"][k])
				check_type4=isinstance(df4["Company Dscription"][k],float)
				if(check_type4):
					break
				if(val1<fuzz.WRatio(df4["Distributor Item code"][j] , df4["Company Dscription"][k])):
					val1=fuzz.WRatio(df4["Distributor Item code"][j] , df4["Company Dscription"][k])
					storeKvalue=k;
					if(val1==100):
						break
				k+=diff
			storeCDvalue=df4["Company Dscription"][storeKvalue]
			df4["Company Dscription"][storeKvalue]=df4["Company Dscription"][j]
			df4["Company Dscription"][j]=storeCDvalue
			j+=1
		array.pop(0)
	df4.to_csv('csv_example6')
	pgbar['value'] = 100
	myLable2['text']='100%'
	myLable3 = Label(root, text="Done. You can get file named csv_example6")
	myLable3.pack()


root = Tk()
root.title('Codemy.com - learn to code!')
root.geometry("400x600")

myLable = Label(root, text="Enter to Process Data")
myLable.pack()

myButton = Button(root,text="Enter To Run", command=buttonPressThenWork )
myButton.pack(pady=10)

pgbar = Progressbar(
	root,
	length = 200,
	orient = HORIZONTAL,
	maximum = 100,
	value = 1,
)
pgbar.pack()
myLable2 = Label(root, text=" 1% ")
myLable2.pack()


root.mainloop()