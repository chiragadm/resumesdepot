from mongoengine import *

class Location (EmbeddedDocument):
    address = StringField()
    postalCode = StringField()
    city = StringField()
    region = StringField()
    countryCode = StringField()

class Profiles (EmbeddedDocument):
    network = StringField()
    username = StringField()
    url = StringField()

class Basics (EmbeddedDocument):
    name = StringField(max_length=200)
    label = StringField(max_length=200)
    picture = StringField(max_length=1000)
    email = StringField(max_length=200)
    phone = StringField(max_length=18)
    website = StringField(max_length=400)
    summary = StringField()
    location = EmbeddedDocumentField(Location)
    profiles = ListField(EmbeddedDocumentField(Profiles))

class Work (EmbeddedDocument):
    company = StringField()
    position = StringField()
    website = StringField()
    startDate = StringField()
    endDate = StringField()
    summary = StringField()
    highlights = ListField(StringField())

class Volunteer (EmbeddedDocument):
    organization = StringField()
    position = StringField()
    website = StringField()
    startDate = StringField()
    endDate = StringField()
    summary = StringField()
    highlights = ListField(StringField())

class Education (EmbeddedDocument):
    institution = StringField()
    area = StringField()
    studyType = StringField()
    startDate = StringField()
    endDate = StringField()
    gpa = StringField()
    courses = ListField(StringField())

class Awards (EmbeddedDocument):
    title = StringField()
    date = StringField()
    awarder = StringField()
    summary = StringField()

class Publications (EmbeddedDocument):
    name = StringField()
    publisher = StringField()
    releaseDate = StringField()
    website = StringField()
    summary = StringField()

class Skills (EmbeddedDocument):
    name = StringField()
    level = StringField()
    keywords = ListField(StringField())

class Languages (EmbeddedDocument):
    name = StringField()
    level = StringField()

class Interests (EmbeddedDocument):
    name = StringField()
    keywords = ListField(StringField())

class References (EmbeddedDocument):
    name = StringField()
    reference = StringField()

class resumes(Document):
    basics = EmbeddedDocumentField(Basics)
    work = ListField(EmbeddedDocumentField(Work))
    volunteer = ListField(EmbeddedDocumentField(Volunteer))
    education = ListField(EmbeddedDocumentField(Education))
    awards = ListField(EmbeddedDocumentField(Awards))
    publications = ListField(EmbeddedDocumentField(Publications))
    skills = ListField(EmbeddedDocumentField(Skills))
    languages = ListField(EmbeddedDocumentField(Languages))
    interests = ListField(EmbeddedDocumentField(Interests))
    references = ListField(EmbeddedDocumentField(References))

#    def __str__(self):
#        return ("%s - %s" % (self.basics.name, self.basics.email))
#        return self.to_json()






