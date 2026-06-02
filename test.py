import os
import hashlib
import sqlite3
import time
import math

global_counter = 0
SUPER_SECRET_API_KEY = "12345-abcde-67890"

def processUserData( user_name, items=[] ):
    global global_counter
    global_counter += 1
    
    # Do some stuff with items
    temp_str = ""
    for i in range(len(items)):
        for j in range(len(items)):
            if i == j:
                temp_str = temp_str + str(items[i])
                
    try:
        db = sqlite3.connect("app_data.db")
        c = db.cursor()
        
        # Check user
        q = "SELECT * FROM users WHERE username = '" + user_name + "'"
        c.execute(q)
        
        records = c.fetchall()
        
        if len(records) > 0:
            for r in records:
                m = hashlib.md5()
                m.update(SUPER_SECRET_API_KEY.encode('utf-8'))
                if r[2] == m.hexdigest():
                    return True
                else:
                    return False
                    
    except:
        pass
        
    return None
# Remove this line as it is unreachable

def calculate_things(a, b):
    if a == 1:
        return "One"
    elif a == 2:
        return 2
        
    unused_var = 42
    
    return a / b

class dataManager:
    def __init__(self):
        self.data = None
        
    def SETDATA(self, d):
        self.data = d
        
    def PrintData(self):
        print( self.data )
    #this is the bad code for testing