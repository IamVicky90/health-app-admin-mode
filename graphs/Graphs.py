import pandas as pd
import plotly.express as px
class Graph_ops:
    def __init__(self,):
        pass
    def create_app_graph(self):
        csv = pd.read_csv('csv_data/app.csv')
        csv['date']=pd.to_datetime(csv['date'], format='%d-%m-%y %H:%M:%S')
        csv=csv.sort_values(by='date').reset_index().drop('index',axis=1)
        error_occured_in_func=list()
        for i in range(csv.shape[0]):
            error_occured_in_func.append(csv['logging_info'].str.split()[i][5])
        csv['error_occured_in_func']=error_occured_in_func
        real_error=[]
        for item in csv.logging_info.str.split(','):
            if str(item).find('[Errno 2]')>0:
                real_error.append('file not find')
                continue
            real_error.append(item[-1])
        csv['real_error']=real_error
        error_occured_in_func_fig = px.pie(csv, names='error_occured_in_func',title=f"Errors occured in functions from {csv['date'][0]} to {csv['date'][csv.shape[0]-1]}, total errors are {csv.shape[0]}",hole=0.6)
        real_error_fig = px.pie(csv, names='real_error',title=f"Errors in real_error column from {csv['date'][0]} to {csv['date'][csv.shape[0]-1]}, total errors are {csv.shape[0]}",hole=0.6)
        return error_occured_in_func_fig,real_error_fig
    def cassandra_db_graph(self):
        csv = pd.read_csv('csv_data/cassandra_db.csv')
        csv['date']=pd.to_datetime(csv['date'], format='%d-%m-%y %H:%M:%S')
        csv=csv.sort_values(by='date').reset_index().drop('index',axis=1)
        status_fig=px.histogram(csv,'status',color='status',title=f"Success V/S Errors  Status from {csv['date'][0]} to {csv['date'][csv.shape[0]-1]}, total entries are {csv.shape[0]}")
        csv['logging_info']=csv.logging_info.replace('Error occured while connecting to cassandra database error: ("Unable to connect to any servers", {"514caa44-afed-47d4-ac69-911205845a27-ap-southeast-1.db.astra.datastax.com:29042:dd2489c0-72b1-4e5a-a545-15a017f68ab6": AuthenticationFailed("Failed to authenticate to 514caa44-afed-47d4-ac69-911205845a27-ap-southeast-1.db.astra.datastax.com:29042:dd2489c0-72b1-4e5a-a545-15a017f68ab6: Error from server: code=0100 [Bad credentials] message="We recently improved your database security. To find out more and reconnect, see https://docs.datastax.com/en/astra/docs/manage-application-tokens.html""), "514caa44-afed-47d4-ac69-911205845a27-ap-southeast-1.db.astra.datastax.com:29042:016912d1-f0df-4577-9bc8-58f1f1999218": AuthenticationFailed("Failed to authenticate to 514caa44-afed-47d4-ac69-911205845a27-ap-southeast-1.db.astra.datastax.com:29042:016912d1-f0df-4577-9bc8-58f1f1999218: Error from server: code=0100 [Bad credentials] message="We recently improved your database security. To find out more and reconnect, see https://docs.datastax.com/en/astra/docs/manage-application-tokens.html""), "514caa44-afed-47d4-ac69-911205845a27-ap-southeast-1.db.astra.datastax.com:29042:7beb840f-c076-4769-bd68-01acc5725524": AuthenticationFailed("Failed to authenticate to 514caa44-afed-47d4-ac69-911205845a27-ap-southeast-1.db.astra.datastax.com:29042:7beb840f-c076-4769-bd68-01acc5725524: Error from server: code=0100 [Bad credentials] message="We recently improved your database security. To find out more and reconnect, see https://docs.datastax.com/en/astra/docs/manage-application-tokens.html"")})','connection Error')
        csv['logging_info']=csv.logging_info.replace('Error occured while connecting to cassandra database error: ("Unable to connect to any servers", {"514caa44-afed-47d4-ac69-911205845a27-ap-southeast-1.db.astra.datastax.com:29042:dd2489c0-72b1-4e5a-a545-15a017f68ab6": OperationTimedOut("errors=None, last_host=None"), "514caa44-afed-47d4-ac69-911205845a27-ap-southeast-1.db.astra.datastax.com:29042:7beb840f-c076-4769-bd68-01acc5725524": OperationTimedOut("errors=None, last_host=None"), "514caa44-afed-47d4-ac69-911205845a27-ap-southeast-1.db.astra.datastax.com:29042:016912d1-f0df-4577-9bc8-58f1f1999218": OperationTimedOut("errors=None, last_host=None")})','connection Error')
        csv['logging_info']=csv.logging_info.replace('Could occured remove the file credentials_validation.log from path Project_Logs/credentials_validation.log error: [Errno 2] No such file or directory: "Project_Logs/credentials_validation.log"','File not found Error')
        logging_info_fig = px.pie(csv, names='logging_info',title=f"Success V/S Errors  Status from {csv['date'][0]} to {csv['date'][csv.shape[0]-1]}, total entries are {csv.shape[0]}",)
        logging_info_fig.update_layout(autosize=False,
            width=1500,
            height=500,)
        return status_fig,logging_info_fig