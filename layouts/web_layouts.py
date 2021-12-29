from db_management.cassandra_ops import CASSANDRRA_OPS
from graphs.Graphs import Graph_ops
from dash import html
from dash import dcc
class create_layouts:
    def __init__(self):
        cassandra_ops_obj=CASSANDRRA_OPS()
        cluster,session=cassandra_ops_obj.get_connection_to_cassandra_db('project_loggings')
        tables=cassandra_ops_obj.get_tables_from_cassandra_db('project_loggings',cluster=cluster,session=session)
        cassandra_ops_obj.convert_tables_into_pandas_csv(session,tables)
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
    def return_common_utils_graph(self,dash_app):
        status_fig,logging_info_fig=self.graph_ops_obj.common_utils_graph()
        dash_app.layout = html.Div(children=[
        html.H1(children='Vicky AI Priduction.'),
        html.Div(children='''
        common_utils.py file dashboard
        '''),
        dcc.Graph(
        id='status_fig',
        figure=status_fig
        ),
        dcc.Graph(
        id='logging_info_fig',
        figure=logging_info_fig),]) 
    def return_create_medical_report_graph(self,dash_app):
        status_fig,logging_info_fig=self.graph_ops_obj.create_medical_report_graph()
        dash_app.layout = html.Div(children=[
        html.H1(children='Vicky AI Priduction.'),
        html.Div(children='''
        create_medical_report.py file dashboard
        '''),
        dcc.Graph(
        id='status_fig',
        figure=status_fig
        ),
        dcc.Graph(
        id='logging_info_fig',
        figure=logging_info_fig),]) 
    def return_credentials_handling_graph(self,dash_app):
        status_fig,logging_info_fig=self.graph_ops_obj.credentials_handling_graph()
        dash_app.layout = html.Div(children=[
        html.H1(children='Vicky AI Priduction.'),
        html.Div(children='''
        credentials_handling.py file dashboard
        '''),
        dcc.Graph(
        id='status_fig',
        figure=status_fig
        ),
        dcc.Graph(
        id='logging_info_fig',
        figure=logging_info_fig),]) 
    def return_credentials_validation_graph(self,dash_app):
        status_fig,logging_info_fig=self.graph_ops_obj.credentials_validation_graph()
        dash_app.layout = html.Div(children=[
        html.H1(children='Vicky AI Priduction.'),
        html.Div(children='''
        credentials_validation.py file dashboard
        '''),
        dcc.Graph(
        id='status_fig',
        figure=status_fig
        ),
        dcc.Graph(
        id='logging_info_fig',
        figure=logging_info_fig),]) 
    def return_db_operations_graph(self,dash_app):
        status_fig,logging_info_fig=self.graph_ops_obj.db_operations_graph()
        dash_app.layout = html.Div(children=[
        html.H1(children='Vicky AI Priduction.'),
        html.Div(children='''
        db_operations.py file dashboard
        '''),
        dcc.Graph(
        id='status_fig',
        figure=status_fig
        ),
        dcc.Graph(
        id='logging_info_fig',
        figure=logging_info_fig),]) 
    def return_emails_graph(self,dash_app):
        status_fig,logging_info_fig=self.graph_ops_obj.emails_graph()
        dash_app.layout = html.Div(children=[
        html.H1(children='Vicky AI Priduction.'),
        html.Div(children='''
        emails.py file dashboard
        '''),
        dcc.Graph(
        id='status_fig',
        figure=status_fig
        ),
        dcc.Graph(
        id='logging_info_fig',
        figure=logging_info_fig),]) 
    def return_generate_random_code_for_validation_graph(self,dash_app):
        status_fig,logging_info_fig=self.graph_ops_obj.generate_random_code_for_validation_graph()
        dash_app.layout = html.Div(children=[
        html.H1(children='Vicky AI Priduction.'),
        html.Div(children='''
        generate_random_code_for_validation.py file dashboard
        '''),
        dcc.Graph(
        id='status_fig',
        figure=status_fig
        ),
        dcc.Graph(
        id='logging_info_fig',
        figure=logging_info_fig),]) 
    def return_kidney_disease_prediction_graph(self,dash_app):
        status_fig,logging_info_fig=self.graph_ops_obj.kidney_disease_prediction_graph()
        dash_app.layout = html.Div(children=[
        html.H1(children='Vicky AI Priduction.'),
        html.Div(children='''
        kidney_disease_prediction.py file dashboard
        '''),
        dcc.Graph(
        id='status_fig',
        figure=status_fig
        ),
        dcc.Graph(
        id='logging_info_fig',
        figure=logging_info_fig),]) 
    def return_predict_images_graph(self,dash_app):
        status_fig,logging_info_fig=self.graph_ops_obj.predict_images_graph()
        dash_app.layout = html.Div(children=[
        html.H1(children='Vicky AI Priduction.'),
        html.Div(children='''
        predict_images.py file dashboard
        '''),
        dcc.Graph(
        id='status_fig',
        figure=status_fig
        ),
        dcc.Graph(
        id='logging_info_fig',
        figure=logging_info_fig),]) 