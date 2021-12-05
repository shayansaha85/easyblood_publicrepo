import pymysql.cursors
import load_properties as lp


def fetch_data(l):
    config = lp.load_properties()
    connection= pymysql.connect(
        host=config.get('db_host').data,
        user= config.get('db_username').data,
        password= config.get('db_password').data,
        database= config.get('db_name').data
    )

    cursor= connection.cursor()
    sql="select firstname, district, phone from donor_information where blood_group = %s and district = %s;"
    cursor.execute(sql, (l[0], l[1]))
    result = cursor.fetchall()
    print(sql)
    return result