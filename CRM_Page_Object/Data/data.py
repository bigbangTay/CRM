# Solar
# handsome
import pymysql
from CRM_Page_Object.Case.addyuangong import *
import unittest

class Selects (object) :
    def __init__ (self,ip,us,pw,data) :
        db = pymysql.connect (ip,us,pw,data)
        self.cursor = db.cursor ()

    def can (self,sqlyu) :
        global result1
        self.cursor.execute (sqlyu)
        result = self.cursor.fetchall ()
        result1 = result [0][0]
        return result1