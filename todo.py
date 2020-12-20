import sys
from datetime import date
import os
n = len(sys.argv)

command = ''
item =  ''
if n==2:
	command=sys.argv[1]

elif n==3:
	command=sys.argv[1]
	item = sys.argv[2]	



if command=='add':
	if item=='':
		print("Error: Missing todo string. Nothing added!")
	else:
		if 'todo.txt' not in os.listdir():
			x = open('todo.txt','x')
			x.close()
		with open('todo.txt','r+') as contents:
			save = contents.read()
		with open('todo.txt','w') as contents:
			contents.write(item+'\n')
		with open('todo.txt','a') as contents:
			contents.write(save)
		print('''Added todo: "{}"'''.format(item))


elif command=='del':
	if item=='':
		print("Error: Missing NUMBER for deleting todo.")
	else:

		item = int(item)-1
		with open('todo.txt','r') as f:
			lines = f.readlines()
		l = len(lines)
		if l==0 or item+1 > l or item<0: 
			print("Error: todo #{} does not exist. Nothing deleted.".format(item+1))
		else:
			lines.reverse()
			del lines[item]
			print('Deleted todo #{}'.format(item+1))
			lines.reverse()
		with open('todo.txt','w') as f:
			f.writelines(lines)



elif command=='done':
	if item=='':
		print("Error: Missing NUMBER for marking todo as done.")
	else:
		item = int(item)-1
		print("item : ",item)
		with open('todo.txt','r+') as f:
			lines = f.readlines()
			l = len(lines)
			# print("lines : ",lines)
			if l < item or l==0 or item<0:
				print("Error: todo #{} does not exist.".format(item+1))
			else:
				lines.reverse()
				with open('done.txt','a') as g:
					g.write('x {} {}'.format(date.today(),lines[item]))
				print("Marked todo #{} as done.".format(item+1))
				del lines[item]
				lines.reverse()
			f.seek(0)
			f.writelines(lines)
			f.truncate()


elif command=='report':
	if 'todo.txt' not in os.listdir():
		x = open('todo.txt','x')
		x.close()
	if 'done.txt' not in os.listdir():
		y = open('done.txt','x')
		y.close()
	with open('todo.txt','r') as f:
		lines = f.readlines()
	with open('done.txt','r') as g:
		lines_ = g.readlines()
	# print(lines,lines_)
	sys.stdout.buffer.write("{} Pending : {} Completed : {}".format(date.today(),len(lines),len(lines_)).encode('utf8'))

elif command =='ls':
	if 'todo.txt' not in os.listdir():
		x = open('todo.txt','x')
		x.close()
	with open('todo.txt','r') as f:
		lines = f.readlines()
	l = len(lines)
	if l==0:
		print("There are no pending todos!")
	else:
		for line in lines:
			sys.stdout.buffer.write('[{}] {}'.format(l,line).encode('utf8'))
			l-=1


elif command=='help' or (command=='' and item==''):
	s = '''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics'''

	sys.stdout.buffer.write(s.encode('utf8'))



	

