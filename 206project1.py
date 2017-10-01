#Mia Bonanno
#SI-206--002

import os
import filecmp


#Input: file name
#Ouput: return a list of dictionary objects where
#the keys will come from the first row in the data.

#Note: The column headings will not change from the
#test cases below, but the the data itself will
#change (contents and size) in the different test
#cases.
	#Your code here:

	file1 = open(file, "r")
	read_file = file1.readline().strip().split(',')
	file_list = []

	for data in file1.readlines():
		dictionary = {}
		x = 0
		file_list2 = data.strip().split(',')
		for keys in read_file:
			dictionary[keys] = file_list2[x]
			x += 1
		file_list.append(dictionary)
	return file_list




#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	list_sorted = sorted(data, key=lambda k: k[col])
	return list_sorted[0]["First"] + ' ' + list_sorted[0]["Last"]




#Create a histogram
def classSizes(data):
	class_size= {'Senior': 0, 'Junior': 0, 'Sophomore': 0, 'Freshman': 0}
	for student in data:
		if student['Class']== 'Senior':
			class_size['Senior'] += 1
		elif student['Class'] == 'Junior':
			class_size['Junior'] +=1
		elif student['Class'] == 'Sophomore':
			class_size['Sophomore'] +=1
		elif student['Class'] == 'Freshman':
			class_size['Freshman'] +=1
	class_sorted= sorted(class_size, key=lambda student: class_size[student], reverse= True)
	total= []
	for student in class_sorted:
		total.append((student, class_size[student]))
	return total

# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]



# Find the most common day of the year to be born
def findDay(a):
	dates_dict= {}
	for student in a:
		DOB= student["DOB"].split('/')
		birthday = DOB[1]
		if birthday in dates_dict:
			dates_dict[birthday] +=1
		else:
			dates_dict[birthday] =1
	sorted_dates= list()
	for student in dates_dict.keys():
		tuples=(student, dates_dict[student])
		sorted_dates.append(tuples)
	sorted_dates= sorted(sorted_dates, reverse=True, key= lambda k: k[1])
	mostcommon= sorted(dates_dict, key=dates_dict.get, reverse=True)
	return int(sorted_dates[0][0])



# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB




# Find the average age (rounded) of the Students
def findAge(a):
	ages_list=[]
	for numbers in a:
		birth_day= int(numbers['DOB'].split('/')[0])
		birth_month= int(numbers['DOB'].split('/')[1])
		birth_year= int(numbers['DOB'].split('/')[2])
		if birth_month <= 9:
			age= 2017-birth_year + 1
		if birth_month >9:
			age= 2017-birth_year
		ages_list.append(age)
	years= 0
	for age in ages_list:
		years +=age
	return int(years/len(ages_list))


# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB



#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
	my_csv=open(fileName, 'w')
	sorted_data= sorted(a, key=lambda x: x[col])
	for student in sorted_data:
		first_name= student['First']
		last_name= student['Last']
		email= student['Email']
		info= [first_name, last_name, email]

		my_csv.write(first_name + ',' + last_name + ',' + email + '\n')

	my_csv.close()

	return None

#For this last task, I believe that my code



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),35)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)

	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
