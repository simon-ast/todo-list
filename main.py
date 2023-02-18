from MODULES import todo_file as tf
from MODULES import display

FILENAME = "ToDo_Entries.txt"


def main():
	"""Read list entries, print to screen, ask for input"""
	event_list = tf.read_todofile(FILENAME)
	display.print_todolist(event_list)
	
	answer = input("ADD (a) / REMOVE (r) / RELOAD (q)? ")
	
	if answer.lower() in ["a", "r"]:
		tf.update_todofile(FILENAME, event_list, answer.lower())
	
	elif answer.lower() == "q":
		exit(0)


if __name__ == "__main__":
	main()
