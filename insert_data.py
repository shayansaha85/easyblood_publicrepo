import pymysql.cursors
import load_properties as lp


def insert_data(l):
    
    config = lp.load_properties()
    connection= pymysql.connect(
        host=config.get('db_host').data,
        user= config.get('db_username').data,
        password= config.get('db_password').data,
        database= config.get('db_name').data
    )


    cursor= connection.cursor()

    sql="insert into donor_information(firstname, blood_group, district, phone) values (%s, %s, %s, %s)"

    cursor.execute(sql, (l[0], l[1], l[2], l[3]))

    connection.commit()
    print("DATA INSERTED")