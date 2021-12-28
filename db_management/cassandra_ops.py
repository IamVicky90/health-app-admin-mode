import os
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import pandas as pd
class CASSANDRRA_OPS:
    def __init__(self):
        pass
    def get_connection_to_cassandra_db(self,keyspace):
        try:
            cloud_config= {
                    'secure_connect_bundle': 'secure-connect-health-app.zip'
            }
            CASSANDRA_USERNAME=os.environ.get('CASSANDRA_USERNAME')
            CASSANDRA_Password=os.environ.get('CASSANDRA_Password')
            auth_provider = PlainTextAuthProvider(CASSANDRA_USERNAME,CASSANDRA_Password )
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            session = cluster.connect(keyspace)
            return cluster, session
        except Exception as e:
            raise e
    def get_tables_from_cassandra_db(self,keyspace='project_loggings',cluster=None,session=None):
        session.execute(f'use {keyspace};')
        tables=cluster.metadata.keyspaces['project_loggings'].tables
        return list(tables.keys())
    def convert_tables_into_pandas_csv(self,session,tables):
        for table in tables:
            df=pd.DataFrame(session.execute(f'select * from {table};'))
            df.to_csv(os.path.join(os.getcwd(),'csv_data',f'{table}.csv'),index=False)