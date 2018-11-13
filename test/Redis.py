import redis



def get_value(rd):
    sex = rd.get("sex")
    addres = rd.get("addres")
    person = rd.mget("music","attr","tag")
    name = rd.get("name")
    key = rd.get("key")
    lol = rd.hget("lol","top")
    print("sex:",sex)
    print("addres:",addres)
    print("person:",person)
    print("name:",name)
    print("key:",key)
    print("lol:",lol)
    print("timor:",rd.hkeys("timor"))


def set_key(rd):
    #rd.set("name","惜君大大")
    #多少秒过期
    rd.setex("sex","man",10)
    #多少毫秒过期
    rd.psetex("addres",10000,"shenzhen")
    #存储多个键值
    rd.mset({"music":"feed","attr":"manly","tag":"撸猫"})
    #根据key获取出来的值索引拼接
    #rd.setrange("name",2,"惜君大大")
    #设置为true name不存在时执行
    print(rd.set("test_name","zed",nx=True))
    #设置为true name存在时操作
    print(rd.set("test_name", "zed", xx=True))

    #正常存储
    rd.set("key",123)
    rd.set("foo",678)
    #根据key设置键值
    rd.hset("lol","top","adc")
    rd.hset("data","attr","lili")
    #根据key设置多个键值
    rd.hmset("timor",{"attr":"apc","addr":"top","tag":"lovely"})


def set_amount(rd):
    #根据获取出来的值做加法运算
    rd.incr("foo",amount=3)
    print(rd.mget("foo"))


def main():
    #使用连接池
    pool = redis.ConnectionPool(host="localhost",port=6379,decode_responses=True)
    rd = redis.Redis(connection_pool=pool)
    #ex过期时间秒  px过期时间毫秒 nx key不存在时操作  xx key存在时操作
    rd.set("gender","lili",ex=10)
    set_key(rd)
    get_value(rd)
    print(rd.get("gender"))
    set_amount(rd)
if __name__ == '__main__':
    main()