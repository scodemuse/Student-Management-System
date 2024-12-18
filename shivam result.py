
print()
print()
print('''                     ******************************************************************
                    \t    STUDENT REPORT CARD MANAGEMENT SYSTEM
                     ******************************************************************''')
print()
#============================ sql connection ==================================
import mysql.connector as mc
connect=''
try:
    db=mc.connect(host="localhost",user ="root",password="1008",database="result")
    cur=db.cursor()
    connect='ok'
except:
    print('====connection to sql failed====')
    print('...Program not connected to sql please check program and database.....')
if connect=='ok':
    cur.execute('show tables')
    rec=cur.fetchall()
    table=''
    if ('details',) in rec:
        if ('marks',) in rec:
            if ('result',) in rec:
                table='ok'
    else:
        print('Tables not found in my sql please check correctly')
#=========================== functions ======================================
def insert_details():
    roll=int(input('Enter roll no of student;'))
    sql='select * from details where roll=%s'
    data=(roll,)
    cur.execute(sql,data)
    record=cur.fetchall()
    if len(record)!=0:
         print('Record already exist for this roll no;')
    else:
        while True:
            name=input('Enter name of student;')
            mot=input('Enter mother\'s name;')
            ft=input('Enter father\'s name;')
            dob=input('Enter date of birth;')        
            sql1='insert into details values(%s,%s,%s,%s,%s)'
            data1=(mot,ft,dob,roll,name)
            cur.execute(sql1,data1)
            db.commit()
            ch=input('Do you want to enter more record say(y/n)')
            if ch=='y' or ch=='Y':
                continue
            elif ch=='n' or ch=='N':
                print('Record sucessfully inserted...')
                break
            else:
                print('Enter right choice.....')

def display_details():
    roll=int(input('Enter roll no of student for display details;'))
    sql='select * from details where roll=%s'
    data=(roll,)
    cur.execute(sql,data)
    record=cur.fetchall()
    if len(record)==0:
        print('NO record found for this roll no;')
    else:
        print('[Mother\'s name,Father\'s name,DOB,Roll no,Name]')
        print(record)
def modify_details():
    roll=int(input('Enter roll no of student for modify/delete details;'))
    sql='select * from details where roll=%s'
    data=(roll,)
    cur.execute(sql,data)
    record=cur.fetchall()
    if len(record)==0:
        print('NO record found for this roll no;')
    else:
        cho=input('Do you want to delete or modify record;')
        if cho=='delete' or cho=='Delete':
            sql='delete from details where roll=%s'
            data=(roll,)
            cur.execute(sql,data)
            db.commit()
            print('Record sucessfully deleted.....')
        elif cho=='modify' or cho=='Modify':
            chi=input('what you want to modify-\n1.Name\n2.Mother\'s name\n3.Father\'s name\n4.D.O.B\n')
            if chi=='1':
                name=input('Enter new name of student ;')
                sql='update details set name=%s where roll=%s'
                data=(name,roll)
                cur.execute(sql,data)
                db.commit()
                print('Record sucessfully modify.....')
            
            elif chi=='2':
                mot=input('Enter new mother\'s name;')
                sql='update details set mother_name=%s where roll=%s'
                data=(mot,roll)
                cur.execute(sql,data)
                db.commit()
                print('Record sucessfully modify.....')
            elif chi=='3':
                ft=input('Enter new father\'s name;')
                sql='update details set father_name=%s where roll=%s'
                data=(ft,roll)
                cur.execute(sql,data)
                db.commit()
                print('Record sucessfully modify.....')
            elif chi=='4':
                dob=input('Enter new date of birth;')
                sql='update details set d_o_b=%s where roll=%s'
                data=(dob,roll)
                cur.execute(sql,data)
                db.commit()
                print('Record sucessfully modify.....')
            else:
                print('Enter right choice.....')
        else:
            print('Enter right choice.....')


            
            
    
def insert_marks():
    roll=int(input('Enter roll no of student for insert marks;'))
    sql='select * from details where roll=%s'
    data=(roll,)
    cur.execute(sql,data)
    record=cur.fetchall()
    if len(record)==0:
        print('NO record found for this roll no;')
    else:
        ms1=int(input('Enter marks of English;'))
        ms2=int(input('Enter marks of Hindi;'))
        ms3=int(input('Enter marks of Math;'))
        ms4=int(input('Enter marks of Science;'))
        ms5=int(input('Enter marks of Social Science;'))
        ms6=int(input('Enter marks of computer;'))
        sql1='insert into marks values(%s,%s,%s,%s,%s,%s,%s)'
        data1=(ms1,ms2,ms3,ms4,ms5,ms6,roll)
        cur.execute(sql1,data1)
        db.commit()
        print('Record sucessfully inserted....')
def display_marks():
    roll=int(input('Enter roll no of student for display marks;'))
    sql='select * from marks where roll=%s'
    data=(roll,)
    cur.execute(sql,data)
    
    record=cur.fetchall()
    if len(record)==0:
        print('NO record found for this roll no;')
    else:
        print('[English,Hindi,Math,Science,social,computer]')
        print(record)
def modify_marks():
    roll=int(input('Enter roll no of student for modify/delete marks;'))
    sql='select * from marks where roll=%s'
    data=(roll,)
    cur.execute(sql,data)
    record=cur.fetchall()
    if len(record)==0:
        print('NO record found for this roll no;')
    else:
        cho=input('Do you want to delete or modify marks;')
        if cho=='delete' or cho=='Delete':
            sql='delete from marks where roll=%s'
            data=(roll,)
            cur.execute(sql,data)
            db.commit()
            print('Record sucessfully delete.....')
        elif cho=='modify' or cho=='Modify':
            chi=input('what you want to modify marks of -\n1.English\n2.Hindi\n3.Maths4.Science\n5.Social\n6.Computer\nEnter-')
            if chi=='1':
                ms1=int(input('Enter marks of English;'))
                sql='update marks set english=%s where roll=%s'

                data=(ms1,roll)
                cur.execute(sql,data)
                db.commit()
                print('Record sucessfully modify.....')
            
            elif chi=='2':
                ms2=int(input('Enter marks of Hindi;'))
                sql='update marks set hindi=%s where roll=%s'
                data=(ms2,roll)
                cur.execute(sql,data)
                db.commit()
                print('Record sucessfully modify.....')
            elif chi=='3':
                ms3=int(input('Enter marks of Math;'))
                sql='update marks set maths=%s where roll=%s'
                data=(ms3,roll)
                cur.execute(sql,data)
                db.commit()
                print('Record sucessfully modify.....')
            elif chi=='4':
                ms4=int(input('Enter marks of Science;'))
                sql='update marks set science=%s where roll=%s'
                data=(ms4,roll)
                cur.execute(sql,data)
                db.commit()
                print('Record sucessfully modify.....')
            elif chi=='5':
                ms5=int(input('Enter marks of Social;'))
                sql='update marks set sst=%s where roll=%s'
                data=(ms5,roll)
                cur.execute(sql,data)
                db.commit()
                print('Record sucessfully modify.....')
            elif chi=='6':
                ms6=int(input('Enter marks of computer;'))
                sql='update marks set computer=%s where roll=%s'
                data=(ms6,roll)
                cur.execute(sql,data)
                db.commit()
                print('Record sucessfully modify.....')
            else:
                print('Enter right choice.....')
        else:
            print('Enter right choice.....')

def result_creator():
    total=0
    count=0
    percentage=0
    
    roll=int(input('Enter roll no of student for result creation;'))
    sql='select * from marks where roll=%s'
    data=(roll,)
    cur.execute(sql,data)
    record=cur.fetchall()
    if len(record)==0:
        print('Record not found for this roll no;')
    else:
        sql='select * from result where roll=%s'
        data=(roll,)
        cur.execute(sql,data)
        record=cur.fetchall()
        if len(record)!=0:
            print('Result already created...')
        else:
            sql='select * from marks where roll=%s'
            data=(roll,)
            cur.execute(sql,data)
            record=cur.fetchall()
            for i in range(len(record[0])-1):
                total+=int(record[0][i])
                if record[0][i]<33:
                    count+=1
            if count>=3:
                status='FAIL'
            else:
                status='PASS'
            percentage=str(total/5)
            sql='insert into result values(%s,%s,%s,%s)'
            data=(percentage,total,roll,status)
            cur.execute(sql,data)
            db.commit()
            print('Result sucessfully created...')

def display_result():
    cho=input('Want to see all result say(y/n);')
    if cho=='Y' or cho=='y':
        cur.execute( 'select * from details,marks,result where details.roll=marks.roll=result.roll;')
        record=cur.fetchall()
        for rec in record:
            print(' _________________________________________________')
            print('|')
            print('|  student name :  ','\t',rec[4])
            print('|  roll         :  ','\t',rec[3])
            print('|  date of birth:  ','\t',rec[2])
            print('|  mother\'s name  :  ','\t',rec[0])
            print('|  father\'s name  :  ','\t',rec[1])
            print('|................................................')
            print('|  subject          marks')
            print('|................................................')
            print('|  science      :  \t',rec[8])
            print('|  hindi      :  \t',rec[6])
            print('|  social studies  :\t',rec[9])
            print('|  maths        :  \t',rec[7])
            print('|  computer      :  ','\t',rec[10])
            print('|  englis       :  \t',rec[5])
            print('|  total        :  \t',rec[13])
            print('|  percent      :  \t',rec[12],'%')
            print('|  status        :  \t',rec[15])
            
            
    elif cho=='N' or cho=='n':
        roll=int(input('Enter roll no of student for display result;'))
        sql=' select * from details,marks,result where details.roll=%s=marks.roll=result.roll;'
        data=(roll,)
        cur.execute(sql,data)
        rec=cur.fetchall()
        if len(rec)==0:
            print('NO record found for this roll no;')
        else:
            print(' _________________________________________________')
            print('|')
            print('|  student name :  ','\t',rec[0][4])
            print('|  roll         :  ','\t',rec[0][3])
            print('|  date of birth:  ','\t',rec[0][2])
            print('|  mother\'s name  :  ','\t',rec[0][0])
            print('|  father\'s name  :  ','\t',rec[0][1])
            print('|................................................')
            print('|  subject          marks')
            print('|................................................')
            print('|  science      :  \t',rec[0][8])
            print('|  hindi      :  \t',rec[0][6])
            print('|  social studies  :\t',rec[0][9])
            print('|  maths        :  \t',rec[0][7])
            print('|  computer      :  ','\t',rec[0][10])
            print('|  englis       :  \t',rec[0][5])
            print('|  total        :  \t',rec[0][13])
            print('|  percent      :  \t',rec[0][12],'%')
            print('|  status        :  \t',rec[0][15])
            
if connect=='ok' and table=='ok':
    while True:
        print('|....................................|')
        print('|  ******MENU FOR OPERATION******    |')
        print('|....................................|')
        print('|   1.To insert                      |')
        print('|....................................|')
        print('|   2.To display                     |')
        print('|....................................|')
        print('|   3.To modify/delete               |')
        print('|....................................|')
        print('|   4.To create result               |')
        print('|....................................|')
        print('|   5.To displsy result              |')
        print('|....................................|')
        print('|   6.EXIT                           |')
        print('|.....................................')
        cho=int(input('Enter your choice(1,2,3,4,5,6);'))
        if cho==1:
            while True:
                print('|....................................|')
                print('|  *****SUBMENU FOR OPERATION*****   |')
                print('|....................................|')
                print('|  1.To insert details of student    |')
                print('|....................................|')
                print('|  2.To insert marks of syudent      |')
                print('|....................................|')
                print('|  3.EXIT                            |')
                print('|....................................|')
                cho=int(input('Enter your choice(1,2,3);'))
                if cho==1:
                    insert_details()
                elif cho==2:
                    insert_marks()
                elif cho==3:
                    break
                else:
                    print('Enter right choice...')
          
        elif cho==2:
            while True:
                print('|....................................|')
                print('|  *****SUBMENU FOR OPERATION*****   |')
                print('|....................................|')
                print('|  1.To display details of student   |')
                print('|....................................|')
                print('|  2.To display marks of student     |')
                print('|....................................|')
                print('|  3.EXIT                            |')
                print('|....................................|')
                cho=int(input('Enter your choice(1,2,3);'))
                if cho==1:
                     display_details()
                elif cho==2:
                    display_marks()
                elif cho==3:
                    break
                else:
                    print('Enter right choice...')    
        elif cho==3:
             while True:
                 print('|.....................................|')
                 print('|  *****SUBMENU FOR OPERATION*****    |')
                 print('|.....................................|')
                 print('|1.To modify/delete details of student|')
                 print('|.....................................|')
                 print('|2.To modify/delete marks of student  |')
                 print('|.....................................|')
                 print('|3.EXIT                               |')
                 print('|.....................................|')
                 cho=int(input('Enter your choice(1,2,3);'))
                 if cho==1:
                     modify_details()
                 elif cho==2:
                     modify_marks()
                
                 elif cho==3:
                     break
                 else:
                     print('Enter right choice...')
        elif cho==4:         
            result_creator()
        elif cho==5:
            display_result()
        elif cho==6:
            break
        else:
            print('Enter right choice...')
        
    

    
