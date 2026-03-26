
schedule = {
    "Art": ["9:30 a.m.", "11:30 a.m."],
    "Literature": ["12:00 p.m.", "1:30 p.m."],
    "Math": ["8:00 a.m.", "10:00 a.m."],
    "Physics": ["9:00 a.m.", "10:00 a.m."],
    "History": ["8:30 a.m.", "9:30 a.m."],
    "Biology": ["2:00 p.m.", "3:00 p.m."],
    "Latin": ["12:30 p.m.", "2:00 p.m."]
}


print("Class Schedule:")
for subject, times in schedule.items():
    print(subject, ":", times[0], "-", times[1])


def current_class(time_str):
    for subject, times in schedule.items():
        if times[0] == time_str or times[1] == time_str:
            return "It's time for " + subject
    return "No class exactly at this time."


print("\nCheck current class:")
print(current_class("9:30 a.m.")) 
print(current_class("12:30 p.m."))  
print(current_class("3:30 p.m."))  