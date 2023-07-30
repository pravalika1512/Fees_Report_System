import pymysql as psq

'''def connect():
       con = psq.connect('fee.db')
       cur = con.cursor()

       cur.execute('CREATE TABLE IF NOT EXISTS fee(id INTEGER PRIMARY KEY, recpt integer, name text, admsn text, date integer, \
                    branch text, sem text, total integer, paid integer, due integer)')

       con.commit()
       con.close()


       	con=db.connect(host='localhost',user='root',passwd='',db='sswcoe',port=3306)
       	cur=con.cursor()
'''
def insert(id , recpt, name , admsn , date , branch , sem , total , paid , due ):
       con = psq.connect(host='localhost',user='root',passwd='',db='sswcoe',port=3306)
       cur = con.cursor()
       sql= "INSERT INTO fee VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
       values=(id,recpt,name,admsn,date,branch,sem,total,paid,due)
       cur.execute(sql,values)


       con.commit()
       con.close()

def view():
       con = psq.connect(host='localhost',user='root',passwd='',db='sswcoe',port=3306)
       cur = con.cursor()

       cur.execute('SELECT * FROM fee')
       row = cur.fetchall()
       return row

       con.commit()


def delete(id):
       con = psq.connect(host='localhost',user='root',passwd='',db='sswcoe',port=3306)
       cur = con.cursor()

       cur.execute('DELETE FROM fee WHERE id=%s',(id))

       con.commit()
       con.close()

'''def update(id ,recpt = ' ', name = ' ', admsn = ' ', date = ' ', branch = ' ', sem = ' ', total = ' ', paid = ' ', due = ' '):
       con = psq.connect(host='localhost',user='root',passwd='',db='sswcoe',port=3306)
       cur = con.cursor()

       cur.execute('UPDATE fee SET recpt = %s OR name = %s OR admsn = %s OR date = %s OR branch = %s OR sem = %s OR total = %s OR \
                    paid = %s OR due = %s',(recpt,name,admsn,date,branch,sem,total,paid,due))


       con.commit()
       con.close()

   def search(id, recpt = ' ', name = ' ', admsn = ' ', date = ' ', branch = ' ', sem = ' ', total = ' ', paid = ' ', due = ' '):
       con = psq.connect(host='localhost',user='root',passwd='',db='sswcoe',port=3306)
       cur = con.cursor()

       cur.execute('SELECT * FROM fee WHERE id=%s OR recpt = %s OR name = %s OR admsn = %s OR date = %s OR branch = %s OR sem = %s OR total = %s OR paid = %s OR due = %s',(id,recpt,name,admsn,date,branch,sem,total,paid,due))
       row = cur.fetchall()
       return row

       con.commit()
'''
#connect()
