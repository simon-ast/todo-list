import numpy as np
import MODULES.todo_entry as te


def generate_todofile(filename, entry_list):
	"""Generate todo list file with header"""
	with open(filename, "w") as f:
		f.write("COMMENT\t DUE_Y\t DUE_M\t DUE_D\t REM\n")
		
		for event in entry_list:
			f.write(
				f"{event.comment}\t "
				f"{event.due_raw[0]}\t "
				f"{event.due_raw[1]}\t "
				f"{event.due_raw[2]}\t "
				f"{event.remaining_time()}\n"
			)


def read_todofile(filename: str):
	"""Read in all entries in todo list file"""
	full_file = []
	with open(filename, "r"):
		raw_data = np.genfromtxt(
			filename, skip_header=1, delimiter="\t", dtype=str
		)
		
		# If less than two entries in file, make sure routine below
		# still works
		if len(raw_data.shape) == 1:
			raw_data = [raw_data]
		
		for entry in raw_data:
			comment = entry[0]
			date_list = [int(entry[i]) for i in [1, 2, 3]]
			
			todo_event = te.TodoEntry(comment, date_list)
			full_file.append(todo_event)
			
			full_file.sort(key=lambda x: int(x.remaining_time()))

		# Generate a unique index for each entry
		for idx in range(len(full_file)):
			full_file[idx].idx = idx + 1

	# TODO: Make this a bit nicer
	reminders = []
	events = []
	for entry in full_file:
		if entry.due.year == int(9999):
			reminders.append(entry)
		else:
			events.append(entry)

	return reminders, events


def update_todofile(filename, old_entry_list, action_choice):
	"""Update existing todo file entries"""
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
