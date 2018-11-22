import pymysql


def insert(cur, db):
    #插入操作
    sql = """insert into user(username,password,phone,email) values 
                ('Loss','123456','1234456','manlyhang@163.com')"""
    try:
        #执行语句 提交
        cur.execute(sql)
        db.commit()
    except Exception as e:
        #错误反馈
        db.rollback()




def select(cur, db):
    # 查询操作
    sql = "select * from user"
    select_sql = "select * from user where username = '%s'"
    try:
        # 执行sql语句`
        cur.execute(select_sql %("jack"))
        #cur.execute(sql)
        # 获取查询结果
        #用于获取单个查询
        result_one = cur.fetchone()
        #result = cur.fetchall()
        print(result_one)
        # for row in result:
        #     print("username:%s    password:%s    phone:%s   email:%s" % (row[1], row[2], row[3], row[4]))
    except Exception as e:
        raise e



def update(cur, db):
    #修改操作
    sql  = "update user set password = '%s' where username = '%s'"
    try:
        cur.execute(sql %("987654321","Loss"))
        db.commit()
    except Exception:
        db.rollback()



def delete(cur, db):
    #删除操作
    sql = "delete from user where id = %d"
    try:
        cur.execute(sql %(2))
        db.commit()
    except Exception:
        db.rollback()


def set_data(cur,db):
    #插入数据
    username = ["timor", "rita", "leesin", "ruler"]
    password = []
    phone = []
    email = []
    sql = """insert into user(username,password,phone,email) values 
                              ('%s','%s','%s','%s')"""
    for i in range(4):
        password.append("123456"+str(i))
        phone.append("987654"+str(i))
        email.append("manlyhang@163.com")
        try:
            cur.execute(sql %(username[i],password[i],phone[i],email[i]))
            db.commit()
        except Exception as e:
            db.rollback()
            print(e)


def create_table(cur, db):
    #创建表
    sql = """create table if not EXISTS money(userid int(11) PRIMARY KEY ,username varchar(20))"""
    try:
        cur.execute(sql)
    except Exception as e:
        raise e

def main():
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root",
                         password="yh981114", db="test", port=3306)
    #获取游标
    cur = db.cursor()
    create_table(cur,db)
    #set_data(cur,db)
    #查询
    select(cur, db)
    #插入
    #insert(cur,db)
    #修改
    #update(cur,db)
    #删除
    #delete(cur,db)
    cur.close()
    db.close()



if __name__ == '__main__':
    main()