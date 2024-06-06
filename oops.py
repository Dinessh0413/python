class school:
    #global variables
    schoolName = "petit"
    studentName="dhinesh"

    def __init__(self,studentname,DOB):
        self.studentName = studentname
        self.dob = DOB
        
    def getDetails(self):
        print(self.studentName)
    
    def makeEmail(self,domain):
        print(f"{self.studentName}{self.dob}{domain}")


objA = school("dhinesh","041103")
objA.getDetails()
objA.makeEmail("@yahoo.com")

