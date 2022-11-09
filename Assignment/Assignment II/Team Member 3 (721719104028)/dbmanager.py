import ibm_db

class DBManager():
  def __init__(self, HOSTNAME, PORT, UID, PWD):
    try:
      self.conn = ibm_db.connect('DATABASE=bludb;'
                                f'HOSTNAME={HOSTNAME};'
                                f'PORT={PORT};'
                                 'SECURITY=SSL;'
                                 'PROTOCOL=TCPIP;'
                                f'UID={UID};'
                                f'PWD={PWD};', '', '')
    except:     
      print("no connection:", ibm_db.conn_errormsg())
    else:
      print("The connection was successful")

    
  # Userdata - username(50), password(50), name(50), workplaceid(10), role(20), email(320), phone(15)
  def add_user(self, username, password, name, role, email, phone):
    sql = f"""insert into userdata (username,password,name,role,email,phone) 
              values ('{username}','{password}','{name}','{role}','{email}','{phone}');"""
    ibm_db.exec_immediate(self.conn, sql)
  
  def get_user(self, username, password):
    sql = f"select * from userdata where username='{username}' and password='{password}';"
    d = ibm_db.fetch_both(ibm_db.exec_immediate(self.conn, sql))
    return (d['USERNAME'],d['PASSWORD'],d['NAME'],d['WORKPLACEID'],d['ROLE'],d['EMAIL'],d['PHONE']) if d else None
  
  def update_user(self, username, password, storename, role, email, phone):
    sql = f"""update userdata set (username,password,name,workplaceid,role,email,phone) 
              = ('{username}', '{password}', '{storename}', '{role}', '{email}', '{phone}');"""
    ibm_db.exec_immediate(self.conn, sql)
  
  def remove_user(self, username, password):
    sql = f"delete from userdata where username='{username}' and password='{password}';"
    ibm_db.exec_immediate(self.conn, sql)
  
  def check_user(self, username, password):
    sql = f"select * from userdata where username='{username}' and password='{password}';"
    return True if ibm_db.fetch_both(ibm_db.exec_immediate(self.conn, sql)) else False

  def check_username(self, username):
    sql = f"select * from userdata where username='{username}';"
    return True if ibm_db.fetch_both(ibm_db.exec_immediate(self.conn, sql)) else False
  
  def get_users(self):
    sql = "select * from userdata;"
    d = ibm_db.fetch_both(ibm_db.exec_immediate(self.conn, sql))
    print(d)
  
  
  # workplace - workplaceid(10), name(50), type(20), address(255), email(320), phone(15)
