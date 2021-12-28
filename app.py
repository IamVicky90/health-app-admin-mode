from dash import Dash
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask import Flask,render_template,redirect
from layouts.web_layouts import create_layouts
server = Flask(__name__)
app_dash = Dash(__name__, server = server, url_base_pathname='/app/' )
cassandra_app = Dash(__name__, server = server, url_base_pathname='/cassanda_db/')
common_utils_dash_app = Dash(__name__, server = server, url_base_pathname='/common_utils/')
create_layouts_obj=create_layouts()
create_layouts_obj.return_app_graph(app_dash)
create_layouts_obj.return_cassandra_db_graph(cassandra_app)
create_layouts_obj.return_common_utils_graph(common_utils_dash_app)

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
@server.route('/common_utils',methods=['GET'])
def render_common_utils():
    return redirect('/common_utils_dash')

app = DispatcherMiddleware(server, {
    '/app_dash': app_dash.server,
    '/cassanda_db_dash': cassandra_app.server,
    '/common_utils_dash': common_utils_dash_app.server,
})

run_simple('0.0.0.0', 8080, app, use_reloader=True, use_debugger=True)