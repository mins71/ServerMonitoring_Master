from models.issue import Issue
from time import strftime, localtime

issue_class = Issue()

def select_issue(pc=None):
    issue_data = issue_class.select_issue(pc)
    return issue_data

def call_issue(pc=None):
    d = select_issue(pc)
    pcname = list(map(lambda i : i[1], d))
    pc_time = list(map(lambda i : strftime("%Y-%m-%d %I:%M:%S", localtime(float(i[0]))), d))
    pc_info_type = list(map(lambda i : i[2], d))
    pc_info_message = list(map(lambda i : i[3], d))

    issue_list = []
    for i in range(len(pcname)):
        issue_list.append([pcname[i], pc_time[i], pc_info_type[i], pc_info_message[i]])
        
    return issue_list