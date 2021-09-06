employees = [
    {"e_id": 1000, "e_name": "ram", "salary": 25000, "department": "testing", "exp": 1},
    {"e_id": 1001, "e_name": "ravi", "salary": 22000, "department": "ba", "exp": 1},
    {"e_id": 1002, "e_name": "raj", "salary": 20000, "department": "mrkt", "exp": 1},
    {"e_id": 1003, "e_name": "nikil", "salary": 26000, "department": "developer", "exp": 1},
    {"e_id": 1004, "e_name": "nivi", "salary": 28000, "department": "developer", "exp": 2},

]
for employee in employees:
    print(employee['e_name'])
for employee in employees:
    print(employees['e_name'].Upper())
for employee in employees:
    if(employees['department']=='developer'):
        print('devemployee["e_name"])
#total of salaries
total=0
for employee in employees:
    total+=employee['salary']
print(total)
