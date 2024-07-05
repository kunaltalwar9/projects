import pymysql
from amazon.src.helpers.config_helpers import get_database_credentials
from amazon.src.configs.generic_configs import GenericConfigs


def read_from_db(sql):
    db_creds = get_database_credentials()
    # connect to database
    connection = pymysql.connect(host=db_creds['db_host'], port=db_creds['db_port'],
                                 user=db_creds['db_user'], password=db_creds['db_password'])
    # connection = pymysql.connect(host='127.0.0.1', port=8889, user='root', password='root')
    try:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        db_data = cursor.fetchall()
        cursor.close()
    finally:
        connection.close()

    # read from database
    # return the result
    return db_data


def get_order_from_db_by_order_no(order_no):
    schema = GenericConfigs.DATABASE_SCHEMA
    table_prefix = GenericConfigs.DATABASE_TABLE_PREFIX
    sql = f"SELECT * FROM {schema}.{table_prefix} WHERE ID = {order_no} AND post_type = 'shop_order';"
    # sql = f"SELECT * FROM localdemostore.wp_posts WHERE ID = {order_no} AND post_type = 'shop_order';"
    db_order = read_from_db(sql)
    # import pdb; pdb.set_trace()
    # print(db_order)
    return db_order


get_order_from_db_by_order_no(65)