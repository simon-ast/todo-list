import datetime as dt
from termcolor import colored


def print_todolist(reminder_list, event_list):
    """Call all print functions"""
    print_date_header()

    print_reminder_header()
    print_reminders(reminder_list)

    print_event_header()
    print_events(event_list)


def print_date_header():
    """Calling this generates the output: TODAY IS day, dd mon YYYY"""
    today = dt.datetime.today()
    today_string = colored(
        f"\n\n\t\t"
        f"TODAY IS {today.strftime('%A').upper()}, "
        f"{today.strftime('%d %b %Y')}\n\n",
        attrs=["bold"]
    )
    print(today_string)


def print_reminder_header():
    """Header for general reminders"""
    print("\t\tGENERAL REMINDERS\n")


def print_reminders(reminder_list):
    """List of general reminder items, printed in blue"""
    for entry in reminder_list:
        reminder_str = colored(
            f"\t{entry.idx}\t"
            f"{entry.comment:30s}\t\t "
            f"\t"
            f"\t "
            f"\t",
            color="cyan"
        )

        print(reminder_str)

    print("\n\n")


def print_event_header():
    """Calling this generates the output: TODAY IS day, dd mon YYYY"""
    descr = "DESCRIPTION"
    print(f"\t\t"
          f"{descr:30s}\t\t DUE DATE\t\t TIME REMAINING\n")

    return


def print_events(event_list):
    """Iteratively print events from todo-list file"""
    for entry in event_list:
        time_remaining = entry.remaining_time()
        print_color = set_color(int(time_remaining))

        event_str = colored(
            f"\t {entry.idx}\t"
            f"{entry.comment:30s}\t\t "
            f"{entry.due.strftime('%a')}, "
            f"{entry.due.strftime('%d %b %Y')}\t "
            f"{time_remaining} day(s)",
            color=print_color
        )

        print(event_str)

    print("\n\n")


def set_color(time_remaining):
    """Colour code entry display by remaining time"""
    text_color = "white"

    if time_remaining <= 14:
        text_color = "yellow"
    if time_remaining <= 7:
        text_color = "red"

    return text_color
