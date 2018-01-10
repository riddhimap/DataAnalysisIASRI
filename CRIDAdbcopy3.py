
#### Database read
import MySQLdb
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="",  	# your password
                     db="CridaDB")        # name of the data base
cur = db.cursor()
sumr=0.0
for i in range(5,9) :
	cur.execute("SELECT AVG(RF) FROM aicrpAgroMetMonthly where year='198%d'" % i)
	avg = cur.fetchall()
	#x1 = avg[0].replace(",", "").replace("(","").replace(")","") will not work as each element in avg is also a list individually
	x1 = avg[0]
	print "Average rainfall in the year 198%d = " % i, x1[0] 
	sumr=sumr+x1[0]

avgt=sumr/(i-4)
print "Average rainfall in the 4 years = ", avgt

db.close()




