import random2
import openpyxl
import matplotlib.pyplot as graph

random_list=[]

for n in range(30):
    #random_list.append(random2.givemenumber(1,10))
print(random_list)

excel = openpyxl.load_workbook('C:\\Users\\jfdr1\\Desktop\\Python_I\\Python_basics\\random_numbers.xlsx')

sheet = excel['numbers']

sheet.append(random_list)

excel.save('C:\\Users\\jfdr1\\Desktop\\Python_I\\Python_basics\\random_numbers.xlsx')

grade_card= sheet['A1':'AD1']

passed = 0
failed = 0

for row in grade_card:
    for grade in row:
        if grade.value >= 5:
            passed = passed + 1
        else:
            failed = failed + 1

x= ['pass', 'fail']
y = [passed, failed]

print("There are " + str(passed) + ' students who passed and  ' + str(failed) + ' students who failed.')

graph.bar(x, y, color=['blue', 'red'])

graph.show()
