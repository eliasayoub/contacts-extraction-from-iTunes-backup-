'''
This script Extracts Contacts from iTunes backup for an iphone with iOS 13, and save it as CSV file(google format).
You can upload it easly to google acount.
The name of the file is 31bb7ba8914766d4ba40d6dfb6113c8b614be442 and it should be under 31 folder.
You can find the file path by searching Google!(it depends on your system).
It works fine for me.
Backup the itunes backup(or just the file we use) for safety reasons.
'''
import sqlite3
import csv

# *** IMPORTANT: change the full path, depends on your platform MAC/PC. I personally put the file (31bb7ba8914766d4ba40d6dfb6113c8b614be442) on desktop
conn = sqlite3.connect('C://Users//elias//Desktop//31bb7ba8914766d4ba40d6dfb6113c8b614be442') # Full Path
c = conn.cursor()

# Query table 
c.execute('SELECT ABPerson.First,ABPerson.Last,ABMultiValue.value FROM ABPerson INNER JOIN  ABMultiValue ON ABPerson.ROWID = ABMultiValue.record_id')
queryList = c.fetchall()
first_l = []
last_l = []
number_l = []
for v in queryList:
    if v[0] != 'SPAM': # Ignoring SPAM
        first_l.append(' ') if (v[0] == None) else first_l.append(v[0]) # Replacing None to ' ' 
        last_l.append(' ') if (v[1] == None) else last_l.append(v[1])
        number_l.append(v[2])
    # else:
        # print(v[0])

conn.close()

length = len(first_l)
# You can change the file name whatever you want.
with open('D://contacts.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # It shuld be this format.
    fieldnames = ['Name', 'Given name', 'Additional Name', 'Family Name', 'Yomi Name', 'Given name Yomi', 'Additional Name Yomi', 'Family Name Yomi', 'Name Prefix', 'Name Suffix', 'Initials', 'Nickname', 'Short Name', 'Maiden Name', 'Birthday', 'Gender', 'Location', 'Billing Information', 'Directory Server', 'Mileage', 'Occupation', 'Hobby', 'Sensitivity', 'Priority', 'Subject', 'Notes', 'Language', 'Photo', 'Group Membership', 'Phone 1 - Type', 'Phone 1 - Value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(length):
        writer.writerow({'Given name': str(first_l[i]), 'Family Name': str(last_l[i]), 'Phone 1 - Value': str(number_l[i])})
    


