# to test with factory-boy
import factory


class Account(object):
    """ Simple Model for testing """
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_UNKNOWN = 'unknown'

    def __init__(self, email, first_name, last_name, gender):
        self.email = email
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.username = self.first_name+"."+self.last_name

    def __str__(self):
        return '%s (%s)' % (self.username, self.email)


class AccountFactory(factory.Factory):
    """ Factory for generate Account """
    class Meta:
        model = Account

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.LazyAttribute(lambda o: '%s@example.org' % o.first_name)
    gender = factory.Iterator([Account.GENDER_MALE, Account.GENDER_FEMALE])


# acc = AccountFactory()
# print "\n----------"
# print "Account: "
# print "\tEmail:", acc.email
# print "\tUsername:", acc.username
# print "\tName:", acc.first_name, " ", acc.last_name
# print "\tGender:", acc.gender

def test_generate_username():
    """ Test to check if username is generated properly when new Account is created """
    acc = AccountFactory(first_name="Matthew", last_name="Willis")
    assert acc.username == "Matthew.Willis"
