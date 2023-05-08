test_design_writers = [1, 3, 5]
scripters = [2, 3, 4, 6, 7, 8]
reviewers = [1, 2, 3, 9, 10]
out_of_office_today = [2, 5, 6, 1]

all_testers = list(set(test_design_writers + scripters + reviewers + out_of_office_today))
can_write_scripts = []
at_work = []
all_strong_testers_today = []

for scripter in scripters:
    if scripters not in test_design_writers and scripter not in reviewers:
        can_write_scripts.append(scripter)
for all_testers_at_work in all_testers:
    if all_testers_at_work not in out_of_office_today:
        at_work.append(all_testers_at_work)
for all_testers_at_work in all_testers:
    if all_testers_at_work in scripters and all_testers_at_work in reviewers and all_testers_at_work in test_design_writers:
        all_strong_testers_today.append(all_testers_at_work)
print(all_testers)
print(can_write_scripts)
print(at_work)
print(all_strong_testers_today)

# всех тестировщиков в команде
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# могут писать только тест скрипты
# [4, 6, 7, 8]
# тестировщиков, которые сегодня на работе
# [3, 4, 7, 8, 9, 10]
# тестировщиков, которые могут писать и ревьюить скрипты, и которые сегодня на работе
# [3]


