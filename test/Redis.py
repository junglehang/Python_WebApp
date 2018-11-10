import redis



def get_value(rd):
    sex = rd.get("sex")
    addres = rd.get("addres")
    person = rd.mget("music","attr","tag")
    print(sex)
    print(addres)
    print(person)

def set_key(rd):
    rd.setex("sex","man",10)
    rd.psetex("addres",10000,"shenzhen")
    rd.mset({"music":"feed","attr":"manly","tag":"撸猫"})


def main():
    #使用连接池
    pool = redis.ConnectionPool(host="localhost",port=6379,decode_responses=True)
    rd = redis.Redis(connection_pool=pool)
    #ex过期时间秒  px过期时间毫秒 nx key不存在时操作  xx key存在时操作
    rd.set("gender","lili",ex=10)
    set_key(rd)
    get_value(rd)
    print(rd.get("gender"))

if __name__ == '__main__':
    main()