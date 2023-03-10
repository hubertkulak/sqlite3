import sqlite3
from sqlite3 import Error

# ponizsze funckje odpalone tylko raz - zeby utworzyc db


db_file = 'baza2.db'

def create_connection(db_file):
    '''create a database connection to a SQLite database'''
    # obiekt połączenia - póki co None
    conn = None
    try:
        # fcja connect zwraca obiekt Connection
        # na którym można wykonać operacje
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_user(conn, ud):
    sql = ''' INSERT INTO user(id, name, high_score, coins, games_played, time_spent)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, ud)
    conn.commit()


def create_car(conn, cd):
    sql = ''' INSERT INTO cars(id, name, price, is_unlocked, path_to_graphics)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, cd)
    conn.commit()


def create_mapowania(conn, md):
    sql = ''' INSERT INTO mapowania(user_id, car_id)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, md)
    conn.commit()




def main(db_file):
    conn = create_connection(db_file)

    # ponizszy kod tworzy trzy tabele w bazie danych 
    # tabela mapowanie odwołuje się do dwóch poprzednich i służy do opierdalania aktualnego użytkownika
    '''
    sql_create_user_table = """ CREATE TABLE IF NOT EXISTS user (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        high_score integer,
                                        coins integer CHECK (coins >= 0),
                                        games_played integer,
                                        time_spent integer
                                    ); """

    sql_create_cars_table = """ CREATE TABLE IF NOT EXISTS cars (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        price integer,
                                        is_unlocked integer,
                                        path_to_graphics text NOT NULL
                                    ); """
    
    sql_create_mapping_table = """CREATE TABLE IF NOT EXISTS mapowania (
                                    user_id integer,
                                    car_id integer,
                                    FOREIGN KEY (user_id) REFERENCES user (id),
                                    FOREIGN KEY (car_id) REFERENCES cars (id)
                                );"""
    '''


    sql = ''' INSERT INTO user(id, name, high_score, coins, games_played, time_spent)
              VALUES(?,?,?,?,?,?) '''
    sql2 = ''' INSERT INTO cars(id, name, price, is_unlocked, path_to_graphics)
              VALUES(?,?,?,?,?) '''

    user_data = (0, "ja", 0, 1, 0, 0)
    
    car0_data = (0, "gtr", 0, 1, "sciezka0")
    car1_data = (1, "lambo", 100, 0, "sciezka1")
    car2_data = (2, "supra", 500, 0, "sciezka2")
    
    mapdata = (0, 0)

    sql3 = '''SELECT user.name 
            FROM user INNER JOIN mapowania ON user.id == mapowania.user_id
            '''
    sql4 = '''SELECT cars.name 
            FROM cars INNER JOIN mapowania ON cars.id == mapowania.car_id
            '''

    #gamedata_id = create_gamedata(conn, game_data)

    with conn:
        # egzekucja poleceń bazodanowych tworzących poszczególne tabele
        # create_table(conn, sql_create_user_table)
        # create_table(conn, sql_create_cars_table)
        # create_table(conn, sql_create_mapping_table)
        # create_user(conn, user_data)
        # create_car(conn, car0_data)
        # create_car(conn, car1_data)
        # create_car(conn, car2_data)

        # tutaj tylko dla testu / pierwsze stworzenie:
        # create_mapowania(conn, mapdata)
        # mapowania powinny się tworzyć przy uruchomieniu programu
        
        # costam z tablicy:
        cur = conn.cursor()
        cur.execute(sql3)
        cur.execute(sql4)
        


if __name__ == "__main__":
    main(db_file)