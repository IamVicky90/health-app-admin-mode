from dash import Dash
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
import dash_html_components as html
import dash_html_components as html
from flask import Flask,render_template,redirect
from layouts.web_layouts import create_layouts
server = Flask(__name__)
dash_app1 = Dash(__name__, server = server, url_base_pathname='/app/' )
dash_app2 = Dash(__name__, server = server, url_base_pathname='/cassanda_db/')
create_layouts_obj=create_layouts()
create_layouts_obj.return_app_graph(dash_app1)
create_layouts_obj.return_cassandra_db_graph(dash_app2)
# dash_app2.layout = html.Div([html.H1('Hi there, I am app2 for reports')])

@server.route('/')
@server.route('/hello')
def hello():
    
    return 'hello world!'

@server.route('/dashboard/',methods=['GET'])
def dashboard():
    return 'dashboard'
@server.route('/app',methods=['GET'])
def render_dashboard():
    return redirect('/app_dash')


@server.route('/cassanda_db',methods=['GET'])
def render_cassanda_db():
    return redirect('/cassanda_db_dash')

app = DispatcherMiddleware(server, {
    '/app_dash': dash_app1.server,
    '/cassanda_db_dash': dash_app2.server
})

run_simple('0.0.0.0', 8080, app, use_reloader=True, use_debugger=True)