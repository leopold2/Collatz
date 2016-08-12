from tkinter import *

root=Tk()
row=40
col=20
numbers=[i for i in range(1,row*col)]
st=""

def toString(array):
	st=""
	for k in range(0,row*col,col):
		st=st + ('  '.join(str(e) for e in array[k:k+col])) + "\n"
	return st

st=toString(numbers)

theLabel=Label(root,text=st)
theLabel.pack()

def collatz(): 
	global numbers
	st1=""
	for j in range(row*col):
		if numbers[j]!=1:
			if numbers[j]%2==0:
				numbers[j]=int(numbers[j]/2)
			else:
				numbers[j]=int(3*numbers[j]+1)
	st1=toString(numbers)
	theLabel.config(text=st1)
	theLabel.pack()
	root.after(1000,collatz)
root.after(1000,collatz)
root.mainloop()
