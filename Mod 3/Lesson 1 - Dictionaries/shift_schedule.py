import copy

def deepcopy_schedule(copied_week, new_week):
    schedule[new_week] = copy.deepcopy(schedule[copied_week])

def shallowcopy_schedule(copied_week, new_week):
    schedule[new_week] = schedule[copied_week].copy()

def modify_schedule(week, employee, shift):
    if week in schedule and employee in schedule[week]:
        schedule[week][employee] = shift
        print(f"Shift updated for {employee} in week {week}: {shift}.")
    else:
        print(f"Schedule not found for {employee} in Week {week}.")

def display_schedule():
    for week, sched in schedule.items():
        print(f"{week}:")
        for employee, shift in sched.items():
            print(f"    {employee} : {shift}")

schedule = {"Week 1" : {"John" : "Morning", "Alice" : "Afternoon", "Bob" : "Night"}}
shallowcopy_schedule("Week 1", "Week 2")
deepcopy_schedule("Week 1", "Week 3")
modify_schedule("Week 2", "John", "Night")
display_schedule()