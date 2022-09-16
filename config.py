from distutils.log import debug


class Config(object):
  pass

class ProdConfig(Config):
  pass

class DevConfig(Config):
  debug = True

  # set info of data
  db_datatype = 'mysql+pymysql'
  db_user = 'root'
  db_password = 'Huan1997'
  db_ip = '127.0.0.1'
  db_port = '3306'
  db_name = 'sys'

  # summary name of database
  # formula: mysql+pymysql://user:password@ip:port/db_name
  db = db_datatype + '://' + db_user + ':' + db_password + '@' + db_ip + ':' + db_port + '/' + db_name

  SQLALCHEMY_DATABASE_URI = db
