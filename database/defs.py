import pymysql

# 购买武器


def purchase_weapon(PNO, WNO, VALUE):
    db = pymysql.connect(host='localhost', user='root',
                         password='abcdefg123.', database='gamemanager', charset='utf8')
    cursor = db.cursor()
    sql = "insert PV (PNO,WNO,VALUE) values ('%s','%s',%d)" % (PNO, WNO, VALUE)
    try:
        cursor.execute(sql)
        db.commit()  # 事务提交
    except Exception as e:
        db.rollback()  # 失败则事务回滚
        print("违背了触发器操作，不能重复购买，插入失败！")
    db.close()

# 出售武器


def sell_weapon(PNO, WNO):
    db = pymysql.connect(host='localhost', user='root',
                         password='abcdefg123.', database='gamemanager', charset='utf8')
    cursor = db.cursor()
    sql = "delete from PV where PNO = '%s' and WNO = '%s'" % (PNO, WNO)
    cursor.execute(sql)
    try:
        cursor.execute(sql)
        db.commit()  # 事务提交
    except Exception as e:
        db.rollback()  # 失败则事务回滚
    db.close()

# 打印玩家信息


def display_player(text, PNO):
    db = pymysql.connect(host='localhost', user='root',
                         password='abcdefg123.', database='gamemanager', charset='utf8')
    cursor = db.cursor()
    sql = "SELECT P.PNO,P.PNAME,P.SEX,P.AGE,P.ELEMENT FROM P where P.PNO='%s'" % PNO
    cursor.execute(sql)
    for rec in cursor:
        text.insert('', 'end', value=rec)

    db.close()

# 显示可购买武器


def display_weapon(text, PNO):
    db = pymysql.connect(host='localhost', user='root',
                         password='abcdefg123.', database='gamemanager', charset='utf8')
    cursor = db.cursor()
    sql = "select * from W where WNO not in (select W.WNO from  P,PV,W where P.PNO=PV.PNO and W.WNO=PV.WNO and P.PNO='%s')" % PNO
    cursor.execute(sql)
    for rec in cursor:
        text.insert('', 'end', value=rec)
    db.close()

# 显示已购买武器


def display_purchase_weapon(text, PNO):
    db = pymysql.connect(host='localhost', user='root',
                         password='abcdefg123.', database='gamemanager', charset='utf8')
    cursor = db.cursor()
    sql = "select W.WNO,W.WNAME,W.LEVEL,W.ELEMENT,W.ANAME from  P,PV,W where P.PNO=PV.PNO and W.WNO=PV.WNO and P.PNO='%s'" % PNO
    cursor.execute(sql)
    for rec in cursor:
        text.insert('', 'end', value=rec)
    db.close()

# 显示玩家武器库


def display_value(text, PNO):
    db = pymysql.connect(host='localhost', user='root',
                         password='abcdefg123.', database='gamemanager', charset='utf8')
    cursor = db.cursor()
    sql = "select W.WNO,W.WNAME,VALUE from  P,PV,W where P.PNO=PV.PNO and W.WNO=PV.WNO and P.PNO='%s'" % PNO
    cursor.execute(sql)
    for rec in cursor:
        text.insert('', 'end', value=rec)
    db.close()

# 管理者所管理的武器


def find_admin_weapon(name):
    db = pymysql.connect(host='localhost', user='root',
                         password='abcdefg123.', database='gamemanager', charset='utf8')
    cursor = db.cursor()
    sql = "SELECT WNAME FROM W where ANAME='%s'" % name
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()
    return result

# 查询购买了该管理员该武器的玩家


def find_player_value(player_text, WNAME, ANAME):
    db = pymysql.connect(host='localhost', user='root',
                         password='abcdefg123.', database='gamemanager', charset='utf8')
    cursor = db.cursor()

    """
    sql = "select P.PNO,P.PNAME,PV.VALUE from  P,PV,W where P.PNO=PV.PNO and W.WNO=PV.WNO and W.WNAME='%s' and W.ANAME='%s'" % (WNAME, ANAME)
    cursor.execute(sql)
    """

    # 用视图查询
    sql = " select PNO,pname,value from PWV where WNAME='%s' and ANAME='%s' " % (
        WNAME, ANAME)
    cursor.execute(sql)

    for rec in cursor:
        player_text.insert('', 'end', value=rec)

    db.close()

# 管理员修改价值


def change_value(PNO, VALUE, WNAME):
    db = pymysql.connect(host='localhost', user='root',
                         password='abcdefg123.', database='gamemanager', charset='utf8')
    cursor = db.cursor()
    sql = "select WNO from  W where WNAME='%s'" % (WNAME)
    cursor.execute(sql)
    result = cursor.fetchall()
    # sql = "replace into PV (PNO,WNO,VALUE) values ('%s','%s',%d)" % (PNO, result[0][0], int(VALUE))
    # 调用创建好的procedure----updatavalue用来更新价值
    sql = "call updatavalue('%s','%s',%d)" % (PNO, result[0][0], int(VALUE))
    try:
        cursor.execute(sql)
        db.commit()  # 事务提交
    except Exception as e:
        db.rollback()  # 失败则事务回滚
        print("价值不能超过128，那样超出市场价啦！")
    db.close()
