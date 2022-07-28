import numpy as np
import MODULES.todo_entry as te


def generate_todofile(filename, entry_list):
	"""DOC!"""
	with open(filename, "w") as f:
		f.write("COMMENT\t DUE_Y\t DUE_M\t DUE_D\t REM\n")
		
		for event in entry_list:
			f.write(f"{event.comment}\t "
			        f"{event.due_raw[0]}\t "
			        f"{event.due_raw[1]}\t "
			        f"{event.due_raw[2]}\t "
			        f"{event.remaining_time()}\n")


def read_todofile(filename: str):
	"""DOC!"""
	full_file = []
	with open(filename, "r"):
		raw_data = np.genfromtxt(filename, skip_header=1, delimiter="\t",
		                         dtype=str)
		
		for entry in raw_data:
			comment = entry[0]
			date_list = [int(entry[i]) for i in [1, 2, 3]]
			
			todo_event = te.TodoEntry(comment, date_list)
			full_file.append(todo_event)
			
			full_file.sort(key=lambda x: int(x.remaining_time()))
	
	return full_file


def update_todofile(filename, old_entry_list, action_choice):
	"""DOC"""
	new_entry_list = old_entry_list
	
	if action_choice == "a":
		new_comment, new_date = te.generate_entry()
		new_todo = te.TodoEntry(new_comment, new_date)
	
		new_entry_list = old_entry_list + [new_todo]
	
	if action_choice == "r":
		order = input("WHICH TASK SHOULD BE REMOVED (# IN LIST)? ")
		order = int(order)
		
		# Sanity check
		if order > len(old_entry_list):
			print("NOT A VALID NUMBER!\n")
			exit()
		
		# COMMENT
		order -= 1
		new_entry_list.pop(order)
	
	generate_todofile(filename, new_entry_list)
	
	return
