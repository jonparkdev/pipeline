#!/usr/bin/python

import csv
import psycopg2
import argparse
from config import config

#command line argument options
parser = argparse.ArgumentParser(description= 'Datapipeline options, must be executed within relative path')
parser.add_argument('function', choices=['upload','read'], help='functions')
parser.add_argument('filename', help='* upload: name of file being uploaded --- '
                                     'read: name of file where query result is being stored --- include .csv extension')

parser.add_argument('user', help='who is accessing the data base')
parser.add_argument('password', help='to authenticate user')
args = parser.parse_args()



def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # write to database
        if args.function == "upload":
            with open('./%s' %(args.filename), 'r') as f:
                reader = csv.reader(f)
                next(reader) # Skip the header row.

                for row in reader:

                    cur.execute('SELECT uuid_generate_v4()')
                    id = cur.fetchone();

                    cur.execute('INSERT INTO test VALUES (%s, %s, %s,%s, %s)',
                    (id, row[0], row[1] ,row[2],'battery' ))

                    cur.execute("INSERT INTO battery VALUES (%s, %s, %s, %s,%s,%s,%s)",
                    (id, row[3], float(row[4]),float(row[5]),
                    psycopg2.Binary(row[6]),psycopg2.Binary(row[7]),
                    psycopg2.Binary(row[8])))
        #read to file
        else:
            cur.execute('SELECT * FROM test NATURAL JOIN battery')

            with open('./%s' %(args.filename), 'w') as f:
                writer = csv.writer(f, delimiter=',')
                for row in cur:
                    writer.writerow(row)

        # close the communication with the PostgresQL database
        conn.commit()


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
        connect()
