import sqlite3
from sqlite3 import Error

class DB_Users():
    """
    Class For CRUD(Create, Read, Update and delete) in Database
    """
    def __init__(self):
        try:
            self.db = sqlite3.connect("users.db")
            self.cursuser = self.db.cursor()
        except Error as e:
            print(e)
        
    def insertData(self,
                   email,
                   password,
                   dateTime,
                   firstName,
                   lastName,
                   dateOfBirth,
                   imageFile,
                   middleName=None):
        """
        Insert Datas in Database
        """
        if middleName:
            name = firstName +' '+ middleName +' '+ lastName
        else:
            name = firstName +' '+ lastName

        sql1 = '''INSERT INTO User (Email, Password, DateTime) VALUES (?, ?, ?);'''
        sql2 = '''INSERT INTO Person (Email, Name, FirstName, MiddleName, LastName, DateOfBirth, ImageFile) VALUES (?, ?, ?, ?, ?, ?, ?);'''

        try:
            self.cursuser.execute(sql1, (email, password, dateTime))
            self.cursuser.execute(sql2, (email, name, firstName, middleName, lastName, dateOfBirth, imageFile))
            self.db.commit()
        except Error as e:
            print(e)

    def fetchPassword(self, email):
        """
        Fetch Data for Log In account
        """
        password = ''
        sql = "SELECT Password FROM User WHERE Email = ?"
        self.cursuser.execute(sql, (email,))
        data = self.cursuser.fetchone()

        if data is None:
            password = None
        else:
            password = data[0]

        return password

    def fetchalldata(self, email):
        """
        Fetch data for show information after Log In
        """
        lis = []
        sql = "SELECT Name, DateOfBirth, ImageFile FROM Person WHERE Email = ?"
        self.cursuser.execute(sql, (email,))
        data = self.cursuser.fetchone()

        if data is None:
            lis = None
        else:
            lis = data

        return lis

    def updatePassword(self, email, password):
        """
        Forgot Password
        """
        sql = '''UPDATE User SET Password=? WHERE Email=?'''
        try:
            self.cursuser.execute(sql, (password, email))
            self.db.commit()
            return True
        except Error as e:
            return False