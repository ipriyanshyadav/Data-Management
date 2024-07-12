import pandas as pd
import matplotlib.pyplot as plt
import csv

print('---------------')
print('1.Read csv file')
print('2.Show all records')
print('------------------')
print('3.Search specific record')
print('4.Search specific column')
print('5.Show record of employee with highest salary')
print('---------------------------------------------')
print('6.Insert new record')
print('7.Modify record')
print('8.Delete record')
print('---------------')
print('9.Show the name of male employees')
print('10.Show the name of female employees')
print('------------------------------------')
print('11.Show salary chart using line graph')
print('12.Show salary chart using bar graph')
print('------------------------------------')

def Read_csv_file():
     a= csv.reader(open('Employee.csv'))
     for i in a:
          print(i)

def Show_all_records():
     print(pd.read_csv('Employee.csv'))

def Search_specific_record():
     a= pd.read_csv('Employee.csv')
     b= input('Enter ID: ')
     c= a[a.ID==b].index.values
     print(a.iloc[c])

def Search_specific_column():
     b= input('Enter column name: ')
     a= pd.read_csv('Employee.csv', usecols=[b])
     print(a)

def Show_record_of_employee_with_highest_salary():
     a= pd.read_csv('Employee.csv')
     b= a["SALARY"].idxmax()
     print(a.iloc[b])

def Insert_new_record():
     a= pd.read_csv('Employee.csv')
     b=input('Enter ID: ')
     c=input('Enter NAME: ')
     d=input('Enter SURNAME: ')
     e=input('Enter SEX: ')
     f=input('Enter DESIGNATION: ')
     g=input('Enter SALARY: ')
     h=input('Enter DOJ: ')
     d= pd.DataFrame({'ID':[b], 'NAME':[c], 'SURNAME':[d], 'SEX':[e], 'DESIGNATION':[f], 'SALARY':[g], 'DOJ':[h]})
     a= pd.concat([a,d], ignore_index=True)
     a.to_csv('Employee.csv', index=False)
     print(pd.read_csv('Employee.csv'))

def Modify_record():
     a= pd.read_csv('Employee.csv')
     b =int(input('Enter ID to modify: '))
     c =a[a.ID==b].index.values
     print()
     print('Enter new data')
     d =input('Enter ID: ')
     e =input('Enter NAME: ')
     f =input('Enter SURNAME: ')
     g =input('Enter SEX: ')
     h =input('Enter DESIGNATION: ')
     i =input('Enter SALARY: ')
     j =input('Enter DOJ: ')
     a.loc[c,'ID']=d
     a.loc[c,'NAME']=e
     a.loc[c,'SURNAME']=f
     a.loc[c,'SEX']=g
     a.loc[c,'DESIGNATION']=h
     a.loc[c,'SALARY']=i
     a.loc[c,'DOJ']=j
     print()
     print('Record modified')
     print()
     a.to_csv('Employee.csv', index=False)
     print(pd.read_csv('Employee.csv'))

def Delete_record():
     a= pd.read_csv('Employee.csv')
     b= int(input('Enter ID to delete: '))
     c= a[a.ID==b].index.values
     print()
     a=a.drop(a.index[c])
     a.to_csv('Employee.csv', index=False)
     print(pd.read_csv('Employee.csv'))

def Show_the_name_of_male_employees():
     a= pd.read_csv('Employee.csv')
     print(a[a['SEX']=='MALE']['NAME'])

def Show_the_name_of_female_employees():
     a= pd.read_csv('Employee.csv')
     print(a[a['SEX']=='FEMALE']['NAME'])

def Show_salary_chart_using_line_graph():
     a= pd.read_csv('Employee.csv')
     x=a['ID']
     y=a['SALARY']
     plt.title("Salary Chart")
     plt.xlabel('ID')
     plt.ylabel('SALARY')
     plt.plot(x,y,'b',marker='+',markersize='10',markeredgecolor='red')
     plt.grid(True)
     plt.legend
     plt.show()

def Show_salary_chart_using_bar_graph():
     a= pd.read_csv('Employee.csv')
     x=a['ID']
     y=a['SALARY']
     plt.bar(x,y)
     plt.xlabel('ID')
     plt.ylabel('SALARY')
     plt.title('Salary Chart')
     plt.grid(True)
     plt.legend
     plt.show()

print()
option= int(input('Enter your choice from above: '))
print()

if option==1:
     Read_csv_file()
elif option==2:
     Show_all_records()
elif option==3:
     Search_specific_record()
elif option==4:
     Search_specific_column()
elif option==5:
     Show_record_of_employee_with_highest_salary()
elif option==6:
     Insert_new_record()
elif option==7:
     Modify_record()
elif option==8:
     Delete_record()
elif option==9:
     Show_the_name_of_male_employees()
elif option==10:
     Show_the_name_of_female_employees()
elif option==11:
     Show_salary_chart_using_line_graph()
elif option==12:
     Show_salary_chart_using_bar_graph()
else:
     print('Invalid input')