#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Database operation modules

データベース操作
"""

import os
import configparser
import MySQLdb


class DatabaseWith():
    """
    Databaseクラス (fetchのたびにカーソルを取得)

    pymysql, mysqldbモジュールを使用
    """

    def __init__(self, path_to_cfg):
        self.path_to_cfg = path_to_cfg
        self._load_cfg()
        self._connect()

    def _load_cfg(self):
        # parse the database informations
        perser = configparser.ConfigParser()
        with open(self.path_to_cfg) as f:
            perser.read_file(f)
            self.host = perser.get('database', 'host')
            self.db = perser.get('database', 'db')
            self.user = perser.get('database', 'user')
            self.passwd = perser.get('database', 'password')

    def _connect(self):
        # make connection with MtSQLab
        self.con = MySQLdb.connect(
                host=self.host,
                db=self.db,
                user=self.user,
                passwd=self.passwd)

    def fetchone(self, table, select, where="", option=""):
        # fetch one row for the given SQL table
        sql = "SELECT %s" % select
        sql += " FROM %s" % table
        if where != "":
            sql += " WHERE %s" % where
        if option != "":
            sql += " %s" % option
        print(sql)
        with self.con.cursor() as cur:
            cur.execute(sql)
            return cur.fetchone()

    def fetchall(self, table, select, where="", option=""):
        # fetch all of rows for the given SQL table
        sql = "SELECT %s" % select
        sql += " FROM %s" % table
        if where != "":
            sql += " WHERE %s" % where
        if option != "":
            sql += " %s" % option
        with self.con.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()

    def get_maxid(self, table):
        sql = "SELECT MAX(id) FROM %s" % table
        with self.con.cursor() as cur:
            cur.execute(sql)
            res = cur.fetchone()[0]
        if res is None:
            return 0
        return res

    def insert(self, table, itemvalues):
        items = [i[0] for i in itemvalues]
        sitem = ", ".join(items)
        values = ["'%s'" % i[1] for i in itemvalues]
        svalue = ", ".join(values)
        sql = "INSERT INTO %s" % table
        sql += " (%s)" % sitem
        sql += " VALUES (%s)" % svalue
        print(sql)
        self.execute_sqls(table, [sql])

    def execute_sqls(self, table, sqls):
        sql = "LOCK TABLES %s WRITE" % table
        with self.con.cursor() as cur:
            cur.execute(sql)
            for sql in sqls:
                cur.execute(sql)
            sql = "COMMIT"
            cur.execute(sql)
            sql = "UNLOCK TABLES"
            cur.execute(sql)


class Database():
    """
    Databaseクラス

    pymysql, mysqldbモジュールを使用
    """

    def __init__(self, path_to_cfg):
        self.path_to_cfg = path_to_cfg
        self._load_cfg()
        self._connect()

    def _load_cfg(self):
        # parse the database informations
        perser = configparser.ConfigParser()
        with open(self.path_to_cfg) as f:
            perser.read_file(f)
            self.host = perser.get('database', 'host')
            self.db = perser.get('database', 'db')
            self.user = perser.get('database', 'user')
            self.passwd = perser.get('database', 'password')

    def _connect(self):
        # make connection with MtSQLab
        con = MySQLdb.connect(
                host=self.host,
                db=self.db,
                user=self.user,
                passwd=self.passwd)
        self.cur = con.cursor()

    def fetchone(self, table, select, where="", option=""):
        # fetch one row for the given SQL table
        sql = "SELECT %s" % select
        sql += " FROM %s" % table
        if where != "":
            sql += " WHERE %s" % where
        if option != "":
            sql += " %s" % option
        print(sql)
        self.cur.execute(sql)
        return self.cur.fetchone()

    def fetchall(self, table, select, where="", option=""):
        # fetch all of rows for the given SQL table
        sql = "SELECT %s" % select
        sql += " FROM %s" % table
        if where != "":
            sql += " WHERE %s" % where
        if option != "":
            sql += " %s" % option
        self.cur.execute(sql)
        return self.cur.fetchall()

    def get_maxid(self, table):
        sql = "SELECT MAX(id) FROM %s" % table
        self.cur.execute(sql)
        res = self.cur.fetchone()[0]
        if res is None:
            return 0
        return res

    def insert(self, table, itemvalues):
        items = [i[0] for i in itemvalues]
        sitem = ", ".join(items)
        values = ["'%s'" % i[1] for i in itemvalues]
        svalue = ", ".join(values)
        sql = "INSERT INTO %s" % table
        sql += " (%s)" % sitem
        sql += " VALUES (%s)" % svalue
        print(sql)
        self.execute_sqls(table, [sql])

    def execute_sqls(self, table, sqls):
        sql = "LOCK TABLES %s WRITE" % table
        self.cur.execute(sql)
        for sql in sqls:
            self.cur.execute(sql)
        sql = "COMMIT"
        self.cur.execute(sql)
        sql = "UNLOCK TABLES"
        self.cur.execute(sql)


class Table():
    def __init__(self, id=None):
        for key in self.items:
            self.__dict__[key] = ""
        if id is not None:
            self.id = id
            self.pull()

    def pull(self):
        """
        Pull status from database
        """
        sql_select = ', '.join(self.items)
        sql_where = "id=%s" % self.id

        db = Database()
        res = db.fetchone(self.tablename, sql_select, sql_where)
        if res is None:
            print("error: database")
            print("%s id = %s の読み込みに失敗" % (self.tablename, self.id))
            exit(1)
        for item, value in zip(self.items, res):
            self.__dict__[item] = value

    def update(self):
        """
        Update status to database
        """
        sql = "UPDATE %s SET " % self.tablename
        conts = []
        for item in self.items:
            value = self.__dict__[item]
            conts += ["%s = '%s'" % (item, value)]
        sql += ", ".join(conts)
        sql += " WHERE id=%s" % self.id

        db = Database()
        db.execute_sqls(self.tablename, [sql])

    def insert(self):
        """
        Insert item into database
        """
        sql = "INSERT INTO %s" % self.tablename
        sql += " (%s)" % ", ".join(self.items)
        sql += " VALUES"
        cont = ["'%s'" % self.__dict__[i] for i in self.items]
        sql += " (%s)" % ", ".join(cont)
        db = Database()
        db.execute_sqls(self.tablename, [sql])

    def remove(self):
        """
        Remove item from database
        """
        sql = "DELETE FROM %s" % self.tablename
        sql += " WHERE id=%s" % self.id

        db = Database()
        db.execute_sqls(self.tablename, [sql])

    def set_maxid(self):
        db = Database()
        sql = "SELECT MAX(id) FROM %s" % self.tablename
        db.cur.execute(sql)
        res = db.cur.fetchone()[0]
        if res is None:
            self.id = 1
        else:
            self.id = res + 1

    def clean(self):
        sqls = ["DELETE FROM scanner WHERE id=%s" % self.id,
                "INSERT INTO scanner (id) VALUES (%s)" % self.id]
        db = Database()
        db.execute_sqls(self.tablename, sqls)


def get_maxid(table):
    db = Database()
    sql = "SELECT MAX(id) FROM %s" % table
    db.cur.execute(sql)
    res = db.cur.fetchone()[0]
    if res is None:
        return 0
    return res


def does_db_have_data(db, table, name_pos, data):
    sql = "SELECT * FROM %s WHERE %s=%s" % (table, name_pos, data)
    db.cur.execute(sql)
    res = db.cur.fetchone()
    if res:
        # print("update")
        return 1
    else:
        # print("insert")
        return 0


def check_data_exist(db, table, exp_id):
    # db = connect(db)
    sql = "SELECT gr_id FROM %s WHERE exp_id=%s" % (table, exp_id)
    db.cur.execute(sql)
    res = db.cur.fetchone()
    if res:
        # print("update")
        return 1
    else:
        # print("insert")
        return 0


def make_sql(db, table, update, names_p, names_v, datas_p, datas_v):
    if update:
        list_p = ["%s=%s" % (
                names_p[i], str(datas_p[i])) for i in range(len(names_p))]
        sql_p = " AND ".join(list_p)
        list_v = ["%s=%s" % (
                names_v[i], str(datas_v[i])) for i in range(len(names_v))]
        sql_v = ", ".join(list_v)
        sql = "UPDATE %s SET %s WHERE %s" % (table, sql_v, sql_p)
    else:
        list_name = list(names_p) + list(names_v)
        sql_name = ", ".join(list_name)
        list_data = list(datas_p) + list(datas_v)
        sql_data = ", ".join(map(str, list_data))
        sql = "INSERT INTO %s (%s) VALUES(%s)" % (table, sql_name, sql_data)
    return sql


def execute_sqls(db, table, sqls):
    sql = "LOCK TABLES %s WRITE" % table
    db.cur.execute(sql)
    for sql in sqls:
        db.cur.execute(sql)
    sql = "UNLOCK TABLES"
    db.cur.execute(sql)


def get_datas(db, table, names_p, names_v, datas_p):
    list_p = ["%s=%s" % (
            names_p[i], str(datas_p[i])) for i in range(len(names_p))]
    sql_p = " AND ".join(list_p)
    sql_v = ", ".join(names_v)

    sql = "SELECT %s FROM %s WHERE %s" % (sql_v, table, sql_p)
    print(sql)
    db.cur.execute(sql)
    datas = db.cur.fetchall()
    return datas


if __name__ == "__main__":
    # prepare to path
    abs_path = os.path.dirname(os.path.realpath(__file__))
    path_to_cfg = os.path.join(abs_path,
                               './../../colonylive_copied_by_wata.cfg')
    # prepare to access into DB
    db = Database(path_to_cfg)

    # set SQL string
    sql = "SELECT * FROM exp"

    # send SQL string
    db.cur.execute(sql)
    res = db.cur.fetchone()
    print(res)

    dbw = DatabaseWith(path_to_cfg)
    res = dbw.fetchone(select='*', table='exp')
    print(res)
