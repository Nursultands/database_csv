class Human:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.familyname = kwargs["familyname"]
        self.age = kwargs["age"]
        self.gender = kwargs["gender"]
        self.nationality = kwargs["nationality"]
        self.profession = kwargs["profession"]

    def set_name(self, name=None):
        if not name:
            return "You didn't provide full informataion about name properly"
        else:
            self.name = name

    def set_familyname(self, familyname=None):
        if not familyname:
            return "You didn't provide full informataion about familyname properly"
        else:
            self.familyname = familyname

    def set_profession(self, profession=None):
        if not profession:
            return "You didn't provide full informataion about profession properly"
        else:
            self.profession = profession
    def set_age(self, age=None):
        if not age:
            return "You didn't provide full informataion about age properly"
        else:
            self.age = age

    def set_gender(self, gender=None):
        if not gender:
            return "You didn't provide full informataion about gender properly"
        else:
            self.gender = gender

    def set_nationality(self, nationality=None):
        if not nationality:
            return "You didn't provide full informataion about nationality properly"
        else:
            self.nationality = nationality

    def get_info(self):
        return {"name":self.name, "familyname":self.familyname, "age":self.age, "gender":self.gender, "nationality":self.nationality, "profession":self.profession}

class Student(Human):
    def __init__(self, name=None, familyname=None, age=None, gender=None,  nationality=None, school=None, profession=None, list_of_subjects=[]):
        super().__init__(name=name, familyname=familyname, age=age, gender=gender, nationality=nationality, profession=profession)
        self.school = school
        if not list_of_subjects:
            return "You didn't provide full informataion about subjects properly"
        else:
            self.list_of_subjects = list_of_subjects
    def add_subject(self, subject=None):
        self.subject = subject
        if self.subject in self.list_of_subjects:
            return "Already exist"
        elif not self.subject:
            return "Error, subject was empty"
        else:
            self.list_of_subjects.append(self.subject)

class Teacher(Human):
    def __init__(self, name=None, familyname=None, age=None, gender=None, nationality=None, school=None, profession=None, list_of_subjects = []):
        super().__init__(name=name, familyname=familyname, age=age, gender=gender, nationality=nationality, profession=profession)
        self.school = school
        if not list_of_subjects:
            return "You didn't provide full informataion about subjects properly"
        else:
            self.list_of_subjects = list_of_subjects

    def set_school(self, school=None):
        self.school = school

    def add_subject(self,subject=None):
        self.subject = subject
        if self.subject in self.list_of_subjects:
            return "Already exist"
        elif not self.subject:
            return "Error, subject was empty"
        else:
            self.list_of_subjects.append(self.subject)
