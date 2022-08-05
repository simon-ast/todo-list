import datetime as dt


class TodoEntry:
	"""Parent class for individual todo entry"""
	def __init__(self, description: str, due_date_list):
		self.comment = description
		self.due_raw = due_date_list
		self.due = dt.datetime(year=due_date_list[0],
		                       month=due_date_list[1],
		                       day=due_date_list[2])
	
	def remaining_time(self):
		"""Calculate remaining time from current date and due date"""
		today = dt.datetime.today()
		remaining = self.due - today
		
		# By adding 1, if day = current then it will result in 0 (not -1)
		return remaining.days + 1


def generate_entry():
	"""Generate todo list entry with comment and due date"""
	input_descr = input("PLEASE DESCRIBE TODO ENTRY [30 CHARS]: ")
	if len(input_descr) > 30:
		print(f"PLEASE STAY WITHIN 30 CHARS "
		      f"(YOU WROTE {len(input_descr)} CHARS)\n")
		generate_entry()
	
	input_duedate = ask_for_date()
	
	return input_descr, input_duedate


def ask_for_date():
	"""Ask for due date in correct format"""
	input_duedate = input("PLEASE INPUT DUE DATE [YYYY/MM/DD]: ")
	due_year, due_month, due_day = input_duedate.split("/")
	
	# Convert to int values
	due_date_list = [int(due_year), int(due_month), int(due_day)]
	
	# Sanity check for due time
	due_date = None
	try:
		due_date = dt.datetime(due_date_list[0], due_date_list[1],
		                       due_date_list[2])
	except ValueError:
		print("\nDATE NOT RECOGNIZED!\n")
		ask_for_date()
	
	# By adding 1, if day = current then it will result in 0 (not -1)
	remaining = int((due_date - dt.datetime.today()).days) + 1
	if int(remaining) < 0:
		print("IM SORRY, THAT EVENT HAS PASSED.")
		ask_for_date()
	
	return due_date_list
	