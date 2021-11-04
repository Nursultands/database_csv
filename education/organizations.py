from education.users import Human, Student, Teacher
import os
import csv
class School:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.address = kwargs["address"]
        self.phone = kwargs["phone"]
        self.email = kwargs["email"]
        self.num_students = 0
        self.num_teachers = 0
        self.list_students = []
        self.list_teachers = []
        self.set_students = set()
        self.set_teachers = set()
        if os.path.exists("{name_of_csv}.csv". format(name_of_csv=self.name)):
            self.load_csv()

    def set_name(self, name=None):
        if not name:
            return "You didn't provide full informataion about name properly"
        else:
            self.name = name

    def set_address(self, address=None):
        if not address:
            return "You didn't provide full informataion about address properly"
        else:
            self.address = address

    def set_phone(self, phone):
        if not phone:
            return "You didn't provide full informataion about phone properly"
        else:
            self.phone = phone

    def num_stud(self):
        return num_student

    def num_teachers(self):
        return num_teachers

    def set_email(self, email):
        if not emeil:
            return "You didn't provide full informataion about email properly"
        else:
            self.emeil = email

    def add_student(self,name=None, familyname=None, age=None, gender=None, nationality=None,school=None, profession=None, list_of_subjects = []):
        if not name or not familyname  or not age or not profession or not gender  or not nationality  or not school  or not list_of_subjects:
            return "You didn't provide full informataion about student properly"
        else:
            s = Student(name=name, familyname=familyname, gender=gender, age=age, nationality=nationality, school=school, profession=profession, list_of_subjects=list_of_subjects)
            if (name+familyname+str(age)) in self.set_students:
                return "This student already exist"
            else:
                self.list_students.append(s)
                self.set_students.add(name+familyname+str(age))
                self.num_students += 1

    def add_teacher(self, name=None, familyname=None, age=None, gender=None, nationality=None, school=None, profession=None,list_of_subjects=None):
        if not name or not familyname  or not age or not gender or not profession  or not nationality  or not school  or not list_of_subjects:
            return "You didn't provide full inforamtation about teacher proplely"
        else:
            t = Teacher(name=name, familyname=familyname, age=age, gender=gender, nationality=nationality,school=school, profession=profession, list_of_subjects=list_of_subjects)
            if (name+familyname+str(age)) in self.set_teachers:
                return "This teacher already exist"
            else:
                self.list_teachers.append(t)
                self.set_teachers.add(name+familyname+str(age))
                self.num_teachers += 1

    def load_csv(self):
        print("men keldim")
        with open ("{name_of_csv}.csv". format(name_of_csv=self.name), mode="r") as csv_file:
            reader = csv.DictReader(csv_file, delimiter = ",")
            for rows in reader:
                if rows["profession"] == "Student" and (rows["name"]+rows["familyname"]+rows["age"]) not in self.set_students:
                    student = Student(name=rows["name"], familyname=rows["familyname"], gender=rows["gender"], age=rows["age"], nationality=rows["nationality"],profession=rows["profession"], school=rows["school"], list_of_subjects=rows["list_of_subjects"])
                    self.set_students.add(rows["name"]+rows["familyname"]+rows["age"])
                    self.list_students.append(student)
                    self.num_students += 1
                elif rows["profession"] == "Teacher" and (rows["name"]+rows["familyname"]+rows["age"]) not in self.set_teachers:
                    teacher = Teacher(name=rows["name"], familyname=rows["familyname"], gender=rows["gender"], age=rows["age"], nationality=rows["nationality"],profession=rows["profession"], school=rows["school"], list_of_subjects=rows["list_of_subjects"])
                    self.set_teachers.add(rows["name"]+rows["familyname"]+rows["age"])
                    self.list_teachers.append(teacher)
                    self.num_teachers += 1

    def get_info(self):
        return {"name":self.name, "address":self.address, "phone":self.phone, "email":self.email, "num_students":self.num_students, "num_teachers":self.num_teachers}

    def get_report(self):
        information = [self.get_info()]
        for i in self.list_students:
            get_info = i.get_info()
            get_info["school"] = i.school
            get_info["list_of_subjects"] = i.list_of_subjects
            information.append(get_info)
        for i in self.list_teachers:
            get_info = i.get_info()
            get_info["school"] = i.school
            get_info["list_of_subjects"] = i.list_of_subjects
            information.append(get_info)
            with open("{name_of_csv}.csv".format(name_of_csv=self.name), mode="w") as csv_file:
                fieldnames = ["name", "familyname","profession","gender","age","nationality","school","list_of_subjects","email", "address", "num_students","num_teachers", "phone"]
                writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
                writer.writeheader()
                for i in information:
                    writer.writerow(i)







if __name__ == "__main__":
    print(f"name of class is {Human.__name__,}, here list of methods {dir(Human)}")
    print(f"name of class is {Student.__name__,} here list of methods {dir(Student)}")
    print(f"name of class is {Teacher.__name__,} here list of methods {dir(Teacher)}")
    print(f"name of class is {School.__name__,} here list of methods {dir(School)}")
else:
    print("Module organizations is imported successfully")
