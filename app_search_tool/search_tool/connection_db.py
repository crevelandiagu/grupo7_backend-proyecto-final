import os
import psycopg2


class ConnectionDB():
    def __init__(self):
        self.url_posgres = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/')

    def connection_postgres(self):
        try:
            url_posgres = self.url_posgres
            conn = psycopg2.connect(database="candidate_db",
                                    host=url_posgres.split(':')[2].split('@')[1],
                                    user=url_posgres.split(':')[1].replace('/', ''),
                                    password=url_posgres.split(':')[2].split('@')[0],
                                    port="5432")
            cursor = conn.cursor()


            return (True, cursor)
        except Exception as e:
            return (False, {'message': e})

    def run_query(self, query_user):
        connection = self.connection_postgres()
        if connection[0]:
            cursor = connection[1]

            postgreSQL_select_Query = query_user
            cursor.execute(postgreSQL_select_Query)

            cv_skill_records = cursor.fetchall()
            return cv_skill_records
        return connection[1]