import pymysql.cursors
import load_properties as lp




def delete_null():
    config = lp.load_properties()
    connection= pymysql.connect(
        host=config.get('db_host').data,
        user= config.get('db_username').data,
        password= config.get('db_password').data,
        database= config.get('db_name').data
    )

    cursor= connection.cursor()

    sql="delete from donor_information where firstname='None'"
    cursor.execute(sql)
    connection.commit()