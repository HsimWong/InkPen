import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb as sql 

db = pymysql.connect("localhost","sockettables","ppnn13%dkstFeb1","SocketTable")
cursor = db.cursor()

'''
create table TargetTable ( 
pair_id int not null auto_increment, 
target_sub_ip varchar(40) not null, 
target_sub_port int not null, 
target_pub_ip varchar(40) not null, 
target_pub_port int not null, 
primary key(pair_id) 
) default charset=utf8;
'''
def RegisterTarget(subIP, subPort, pubIP, pubPort):
    if len(subIP) >= 40 or len(pubIP) >= 40 subPort >= 65536 or pubPort >= 65536:
        return "Failed"

    DbCmd = """insert into TargetTable 
            (target_sub_ip, target_sub_port, 
            target_pub_ip, target_pub_port)
            values
            ('%s',%d,'%s',%d);"""%(subIP, subPort, pubIP, pubPort)

    cursor.execute(DbCmd)
    db.commit()
    return "Success"

def CheckTarget
