import sqlite3
from datetime import datetime

#Code to generate timestamp
now=datetime.now()
ts = datetime.timestamp(now)


conn = sqlite3.connect('database.db')
user_id=1
ts=str(ts)
noun='bill'
verb='pay'
location='10.21.13.15'
timespent='10'
properties='{"Bank": "HDFC"}'

#c=conn.execute('CREATE TABLE events ( user_id INTEGER NOT NULL , ts TEXT NOT NULL, noun TEXT NOT NULL, verb TEXT NOT NULL, location TEXT NOT NULL, timespent InTEGER , properties TEXt NOT NULL )')
ins_statment="INSERT INTO events (user_id,ts,noun,verb,location,timespent,properties) VALUES ({},'{}','{}','{}','{}',{},'{}')".format(user_id,ts,noun,verb,location,timespent,properties)

#ins=conn.execute("""INSERT INTO events (user_id,ts,noun,verb,location,timespent,properties) VALUES (1,'1604926997.647401','bill','pay','10.21.13.15',50,'{"Bank": "HDFC","Value":"3035","mode":"netbanking"}')""")
#conn.commit()
cur = conn.cursor()


sel=cur.execute("Select * from events where user_id=1  and  noun='bill' and verb=='pay'")
sel_data = cur.fetchall(); 

for s in sel_data:
    print(s)
conn.close()



#####
"""
SQL Commands
To create table
CREATE TABLE events ( user_id INTEGER NOT NULL, ts TEXT NOT NULL, noun TEXT NOT NULL, verb TEXT NOT NULL, location TEXT NOT NULL, timespent InTEGER , properties TEXt NOT NULL )

DROP TABLE EVENTS

Insert

INSERT INTO events (user_id,ts,noun,verb,location,timespent,properties) VALUES (1,'1604925997.647401','bill2','pay','10.21.13.15',10,'{"Bank": "HDFC","Value":"135","mode":"netbanking"}')

"""