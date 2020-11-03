import json

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __str__(self):
        return "email: {}; password: {}".format(self.email, self.password)

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)