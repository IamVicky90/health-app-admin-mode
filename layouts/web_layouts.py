from db_management.cassandra_ops import CASSANDRRA_OPS
from graphs.Graphs import Graph_ops
import dash_html_components as html
import dash_core_components as dcc
class create_layouts:
    def __init__(self):
        self.cassandra_ops_obj=CASSANDRRA_OPS()
        self.cluster,self.session=self.cassandra_ops_obj.get_connection_to_cassandra_db('project_loggings')
        self.tables=self.cassandra_ops_obj.get_tables_from_cassandra_db('project_loggings',cluster=self.cluster,session=self.session)
        self.cassandra_ops_obj.convert_tables_into_pandas_csv(self.session,self.tables)
        self.graph_ops_obj=Graph_ops()
    def return_app_graph(self,dash_app):
        error_occured_in_func_fig,real_error_fig=self.graph_ops_obj.create_app_graph()
        dash_app.layout = html.Div(children=[
        html.H1(children='Vicky AI Priduction.'),
        html.Div(children='''
        app.py file dashboard
        '''),
        dcc.Graph(
        id='error_occured_in_func_fig',
        figure=error_occured_in_func_fig
        ),
        dcc.Graph(
        id='real_error_fig',
        figure=real_error_fig),]) 
    def return_cassandra_db_graph(self,dash_app):
        status_fig,logging_info_fig=self.graph_ops_obj.cassandra_db_graph()
        dash_app.layout = html.Div(children=[
        html.H1(children='Vicky AI Priduction.'),
        html.Div(children='''
        cassandra_db.py file dashboard
        '''),
        dcc.Graph(
        id='status_fig',
        figure=status_fig
        ),
        dcc.Graph(
        id='logging_info_fig',
        figure=logging_info_fig),]) 