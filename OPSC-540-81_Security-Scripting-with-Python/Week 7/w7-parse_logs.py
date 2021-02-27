'''
Michael Epstein
OPSC-540-81
'''
# import statements
import os
import sqlite3


#code

def check_table():
    conn = sqlite3.connect('logs.db')
    c = conn.cursor()
                
    #get the count of tables with the name
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='attacks' ''')

    #if the count equals 1, then table exists; otherwise create the table and import the schema
    if c.fetchone()[0]==1 : {
        print('Table exists.')
    }
    else: 
        print('Table does not exist. attacks table will be created now.')
        c.execute(''' CREATE TABLE attacks(id INTEGER PRIMARY KEY, attack_line TEXT NOT NULL); ''')
                
    #commit the changes to db			
    conn.commit()
    #close the connection
    conn.close()




# db file
dir_name = os.path.dirname(__file__)
db_path = os.path.join(dir_name, 'logs.db')

try:
    sql_conn = sqlite3.connect(db_path)
except sql_conn.DatabaseError:
    print("Unable to establish connection to Database")
    exit(0)

print ('Database opened successfully')
#db pointer
curr = sql_conn.cursor()

#check if attacks table is created, if not create it
check_table()

dir_name = dir_name + 'logs/'
log_file1 = open(dir_name + 'modsec_audit.log', 'r')
log_file2 = open(dir_name + 'modsec_audit.log.1', 'r')
log_file3 = open(dir_name + 'modsec_audit.log.2', 'r')
        
      
lines = log_file1.readlines()
lines += log_file2.readlines()
lines += log_file3.readlines()

line = lines.pop(0)
id_value = 0
try:
    while line:
        if "-B--" in line:
            url_line = lines.pop(0)  # found a "-B--", so get the next line with the url
            if "/etc/passwd" in url_line or "script" in url_line or 'input' in url_line: # look for multiple "attacks" here
                print("Attack found on line " + str(id_value) + ": %s" % url_line.strip())
                # PUT your insert sql statement lines here to insert url_line
                id_value += 1
                sql_conn.execute('INSERT or IGNORE INTO attacks (id, attack_line) VALUES (?, ?)', (id_value, url_line))
                
                                 
        line = lines.pop(0)
                             
except Exception as e:
    print ("\n", e)    

#close open log files
log_file1.close()
log_file2.close()
log_file3.close()

#commit db changes and close the table
print("Records added to database.")
sql_conn.commit()
print ("Database changes committed.")
sql_conn.close()
print ("Database connection closed.")    