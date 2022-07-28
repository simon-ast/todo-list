import datetime as dt
from termcolor import colored


def print_todolist(event_list):
	"""DOC"""
	print_header()
	print_events(event_list)


def print_header():
	"""
	Calling this generates the output:
	TODAY IS day, dd mon YYYY
	"""
	today = dt.datetime.today()
	today_string = colored(f"\n\n"
	                       f"\t\t"
	                       f"TODAY IS {today.strftime('%A').upper()}, "
	                       f"{today.strftime('%d %b %Y')}\n\n",
	                       attrs=["bold"])
	print(today_string)
	
	descr = "DESCRIPTION"
	print(f"\t\t"
	      f"{descr:30s}\t\t DUE DATE\t\t TIME REMAINING\n")
	
	return


def print_events(event_list):
	"""DOC"""
	for entry in event_list:
		time_remaining = entry.remaining_time()
		print_color = set_color(int(time_remaining))
		
		event_str = colored(
			f"\t\t"
			f"{entry.comment:30s}\t\t "
			f"{entry.due.strftime('%a')}, "
		    f"{entry.due.strftime('%d %b %Y')}\t "
		    f"{time_remaining} day(s)",
			color=print_color
		)
		
		print(event_str)
	
	print("\n\n")


def set_color(time_remaining):
	"""DOC!"""
	text_color = "white"
	
	if time_remaining <= 14:
		text_color = "yellow"
	if time_remaining <= 7:
		text_color = "red"
	
	return text_color
	