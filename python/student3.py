from tabulate import tabulate
from datetime import datetime

class Student:
	"""docstring for ClassName"""
	def __init__(self,roll_no,name,studDob,studStd,marks):
		self.roll_no =	 roll_no
		self.name	= name
		self.studDob = studDob
		self.studStd = studStd
		self.marks = marks

	
	def totalMarks(self):
		total = self.marks[0] + self.marks[1] + self.marks[2] + self.marks[3] + self.marks[4]
		return total
	def avgMarks(self,total):
		avg = float(total) / 5
		return avg
	def calculateGrade(self,total):
		totalMark = 500
		percentage = (total*100/float(totalMark))
		if percentage >= 80:
			return "distinction"
		elif percentage >= 60 and percentage < 80:
			return "First Class"
		elif percentage >= 40 and percentage < 60:
			return "Second Class"
		else:
			return "Fail"

	def scholarshipEligibility(self,total):
		totalMark = 500
		percentage = (total*100/float(totalMark))
		if percentage >= 90:
			return 1
		else:
			return 0

class Scholarship(Student):
	"""docstring for Scholarship"""
	def __init__(self, student,scholarshipno, scholarship_date, scholarship_duration, scholarshipAmount):
		self.studName = student.name
		self.roll_no = student.roll_no
		self.scholarshipno = scholarshipno
		self.scholarship_date = scholarship_date
		self.scholarship_duration = scholarship_duration
		self.scholarshipAmount = scholarshipAmount	
	def checkExpiry(self):
		scholarship_duration = self.scholarship_duration
		scholarshipDt = datetime.strptime(self.scholarship_date, "%d/%m/%Y").strftime('%Y-%m-%d')
		scholarshipDt = datetime.strptime(scholarshipDt, '%Y-%m-%d')
		now = datetime.now()
		datediff = (now - scholarshipDt).days
		totalday = scholarship_duration * 365
		if  totalday  - datediff > 1:
			return 0
		else:
			return 1

def viewStudents(studentList):
	studTable = []
	if len(studentList) <= 0:
		print "No Students"
		return
	for i in range (0,len(studentList)):

		total = studentList[i].totalMarks()
		avg = studentList[i].avgMarks(total)
		grade = studentList[i].calculateGrade(total)
		birthDate = datetime.strptime(studentList[i].studDob, "%d/%m/%Y").strftime('%Y-%m-%d')
		dt = datetime.strptime(birthDate, '%Y-%m-%d')
		age = datetime.now().year - dt.year
		scholarshipEligible = studentList[i].scholarshipEligibility(total)
		studTable.append([studentList[i].roll_no,studentList[i].name,studentList[i].studDob,age,studentList[i].studStd,studentList[i].marks[0],studentList[i].marks[1],studentList[i].marks[2],studentList[i].marks[3],studentList[i].marks[4],avg,grade,scholarshipEligible])

	print tabulate(studTable, headers=["RollNum","Name","Date of Birth", "Age", "Standerd","Mark 1" ,"Mark 2","Mark 3","Mark 4","Mark 5" ,"Average","Grade","Scholarship"])

	
def addStud():
	totalStudents = input("Enter number of students: ")
	i = 0
	
	for i in range(0,totalStudents):
		marks = []
		print "\n"
		roll_no = raw_input("Enter student Roll Number: ")
		
		if len(studentList) > 0:
			for k in range(0,len(studentList)):
				
				while roll_no == studentList[k].roll_no:
					print "RollNum %s already taken" %roll_no
					roll_no = raw_input("Enter student Roll Number: ")
							
			
		studName = raw_input("Enter student name: ")
		studDob = raw_input("Enter student Date of Birth dd/mm/yyyy: ")
		studStd = raw_input("Enter student Class: ")
		print "Enter Mark for Subject1: ",
	   	marks.append(input())
	   	print "Enter Mark for Subject2: ",
	   	marks.append(input())
	   	print "Enter Mark for Subject3: ",
	   	marks.append(input())
	   	print "Enter Mark for Subject4: ",
	   	marks.append(input())
	   	print "Enter Mark for Subject5: ",
	   	marks.append(input())
		stud = Student(roll_no,studName,studDob,studStd,marks)
		studentList.append(stud)

def entroll(id):

	if len(scholarshipList) > 0:
		for k in range(0,len(scholarshipList)):
			if id == scholarshipList[k].roll_no:
				print "This student already entrolled for scholarship"
				return
	flag = 0
	for i in range (0,len(studentList)):
		if id == studentList[i].roll_no:
			flag = 1
			total = studentList[i].totalMarks()
			grade = studentList[i].calculateGrade(total)
			scholarshipEligible = studentList[i].scholarshipEligibility(total)
			if scholarshipEligible == 1:
				Scholarship_no = raw_input("Enter Scholarship No :")
				Scholarship_date = raw_input("Enter date: ")
				Scholarship_amount = int(input("Enter Amount: "))
				Scholarship_duration = input("Enter Duration in year: ")
				scholarshipDetails = Scholarship(studentList[i],Scholarship_no,Scholarship_date,Scholarship_duration,Scholarship_amount)
				scholarshipList.append(scholarshipDetails)
				print "Entrolled for Scholarship!"
			else:
				print "Sorry this student is not eligible for scholarship"
		
	if(flag == 0):
		print "No Student with roll no %s" % (id)


def viewScholarship(scholarshipList):
	if len(scholarshipList) <= 0:
		print "No one entrolled for scholarship"
		return
	scholarshipTable = []
	j = 0
	for j in range(0,len(scholarshipList)):
		Scholarship_no = scholarshipList[j].scholarshipno
		studName = scholarshipList[j].studName
		Scholarship_date = scholarshipList[j].scholarship_date
		Scholarship_duration = scholarshipList[j].scholarship_duration
		ScholarshipAmount = scholarshipList[j].scholarshipAmount
		ScholarshipExpiry = scholarshipList[j].checkExpiry()
		if (ScholarshipExpiry == 1):
			ScholarshipExpiry = "Expired"
		else:
			ScholarshipExpiry = "Not Expired"
		scholarshipTable.append([studName,Scholarship_no,Scholarship_date,Scholarship_duration,ScholarshipAmount,ScholarshipExpiry])
		
	if (len(scholarshipList) > 0):
		print "Scholarship Details \n \n"
		print tabulate(scholarshipTable, headers=["Student Name","Scholarship No","Scholarship Date", "Scholarship Duration (in Years)", "Scholarship Amount","Scholarship Expiry"])


def DeleteStudent(id):
	for i in range (0,len(studentList)):
		if id == studentList[i].roll_no:
			del studentList[i]
			print "Deleted from Students list"
			break
	for j in range(0,len(scholarshipList)):
		if id == scholarshipList[j].roll_no:
			del scholarshipList[j]
			print "Deleted from Scholarship list"

			
		else:
			print "No student with id %s" %id



global studentList 
studentList = []
global scholarshipList 
scholarshipList = []
choice = 1
while choice:
	print ("""
	1.Add Students
	2.View Student Details
	3.Entroll Scholarship
	4.View Scholaship Details
	5.Delete Student
	6.Exit
	""")
	choice=raw_input("What would you like to do? ") 
	if choice=="1": 
		addStud()
	elif choice=="2":
		viewStudents(studentList)
	elif choice=="3":
		studId = raw_input("Enter student Id :")
		entroll(studId)
	elif choice=="4":
		viewScholarship(scholarshipList)
	elif choice == "5":
		if len(studentList) > 0:
			studId = raw_input("Enter student Id :")
			DeleteStudent(studId)
		else:
			print "Sorry, Students list is empty !"
	elif choice == "6":
		exit()
	else:
	  print("\n Not Valid Choice Try again")
	  continue