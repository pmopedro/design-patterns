from abc import ABCMeta, abstractmethod

class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):
    def describe():
        print("Personal Section")

class PatenetSection(Section):
    def describe(self):
        print("Patent Section")

class AlbumSection(Section):
    def describe(self):
        print("Album Section")

class PublicationSection(Section):
    def describe(self):
        print("Publication")


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections=[]
        self.createProfile()
    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections
    
    def addSections(self, section):
        self.sections.append(section)


class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatenetSection())
        self.addSections(PublicationSection())

class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


profile_type = input ("Select which profile type you'd like to create: [LinkedIn, Facebook]")
profile = eval(profile_type.lower())()
print("Creating profile...", type(profile).__name__)
print("Profile has sections: ", profile.getSections())