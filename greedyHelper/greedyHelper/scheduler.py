from datetime import datetime

'''
    Defines and activity's name (str), start date, and end date (datetime)
'''
class Activity:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end
    
    def __str__(self):
        return f"{self.name}"

# Greedy algorithm to get feasible activities for each day
def get_feasible_activities(task_list):
    # First sort based on start day
    task_list.sort(key=lambda x: x.start.day)

    # Now for each day, find the set of feasible activities to complete
    f_set = {}
    for activity in task_list:
        if activity.start.day not in f_set:
            f_set[activity.start.day] = [activity]
        else:
            f_set[activity.start.day].append(activity)

    # For each day, sort all activities based on their end times and keep track of all feasible activities (ones that don't overlap)
    for day in f_set:
        f_set[day].sort(key=lambda x: x.end.hour)
        res = [f_set[day][0]]
        for i in range(1, len(f_set[day])):
            if f_set[day][i].start.hour >= f_set[day][i-1].end.hour:
                res.append(f_set[day][i])
        f_set[day] = res
    
    return f_set

### HARDCODED TEST ###
# test_list = [Activity("third task", datetime(2023, 1, 2, 8), datetime(2023, 1, 2, 10)),
#                 Activity("first task", datetime(2023, 1, 1, 8), datetime(2023, 1, 1, 9)),
#                 Activity("second task", datetime(2023, 1, 1, 8), datetime(2023, 1, 1, 12))
#             ]

# res = get_feasible_activities(test_list)

# for key in res:
#     l = res[key]
#     print(f"{key}: ")
#     for item in l:
#         print(item.name)