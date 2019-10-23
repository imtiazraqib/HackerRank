class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here

    def __init__(self, fn, ln, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores
        
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        averageScore = 0
        for i in range(len(self.scores)):
            averageScore += self.scores[i]
        
        averageScore = averageScore/len(self.scores)

        if averageScore >= 90 and averageScore <= 100:
            return "O"
        if averageScore >= 80  and averageScore < 90:
            return "E"
        if averageScore >= 70  and averageScore < 80:
            return "A"
        if averageScore >= 55  and averageScore < 70:
            return "P"
        if averageScore >= 40  and averageScore < 55:
            return "D"
        if averageScore < 40:
            return "T"

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())