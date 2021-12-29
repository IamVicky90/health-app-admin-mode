from dash import Dash
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask import Flask,render_template,redirect,request
from layouts.web_layouts import create_layouts
from mongo_db_ops.db_management import mongo_db_atlas_ops
server = Flask(__name__)
server.jinja_env.globals.update(zip=zip)
app_dash = Dash(__name__, server = server, url_base_pathname='/app/' )
cassandra_app = Dash(__name__, server = server, url_base_pathname='/cassanda_db/')
common_utils_dash_app = Dash(__name__, server = server, url_base_pathname='/common_utils/')
create_medical_report_dash_app = Dash(__name__, server = server, url_base_pathname='/create_medical_report/')
credentials_handling_dash_app = Dash(__name__, server = server, url_base_pathname='/credentials_handling/')
credentials_validation_dash_app = Dash(__name__, server = server, url_base_pathname='/credentials_validation/')
db_operations_dash_app = Dash(__name__, server = server, url_base_pathname='/db_operations/')
emails_dash_app = Dash(__name__, server = server, url_base_pathname='/emails/')
generate_random_code_for_validation_dash_app = Dash(__name__, server = server, url_base_pathname='/generate_random_code_for_validation/')
kidney_disease_prediction_dash_app = Dash(__name__, server = server, url_base_pathname='/kidney_disease_prediction/')
predict_images_dash_app = Dash(__name__, server = server, url_base_pathname='/predict_images/')
create_layouts_obj=create_layouts()
create_layouts_obj.return_app_graph(app_dash)
create_layouts_obj.return_cassandra_db_graph(cassandra_app)
create_layouts_obj.return_common_utils_graph(common_utils_dash_app)
create_layouts_obj.return_create_medical_report_graph(create_medical_report_dash_app)
create_layouts_obj.return_credentials_handling_graph(credentials_handling_dash_app)
create_layouts_obj.return_credentials_validation_graph(credentials_validation_dash_app)
create_layouts_obj.return_db_operations_graph(db_operations_dash_app)
create_layouts_obj.return_emails_graph(emails_dash_app)
create_layouts_obj.return_generate_random_code_for_validation_graph(generate_random_code_for_validation_dash_app)
create_layouts_obj.return_kidney_disease_prediction_graph(kidney_disease_prediction_dash_app)
create_layouts_obj.return_predict_images_graph(predict_images_dash_app)

@server.route('/')
@server.route('/login')
def hello():
    
    return render_template('/login.html')
@server.route('/validation',methods=['GET','POST'])
def validation():
    if request.method == 'POST':
        username=request.form['username']
        password=request.form['pass']
        if username=='admin':
            if password=='123':
                mongo_obs=mongo_db_atlas_ops()
                client=mongo_obs.get_mongo_db_connection()
                fname,lname,email,state=mongo_obs.return_entries_from_db(client)
                return render_template('index.html',fname=fname,lname=lname,email=email,state=state,total_clients=len(email))
            else:
                print('Wrong Password')
        else: 
            print('Invalid username or password')
        return 'validate run successfully'
    return 'GET'

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
@server.route('/create_medical_report',methods=['GET'])
def create_medical_report_utils():
    return redirect('/create_medical_report_dash')
@server.route('/credentials_handling',methods=['GET'])
def credentials_handling():
    return redirect('/credentials_handling_dash')
@server.route('/credentials_validation',methods=['GET'])
def create_credentials_validation():
    return redirect('/credentials_validation_dash')
@server.route('/db_operations',methods=['GET'])
def db_operations():
    return redirect('/db_operations_dash')
@server.route('/emails',methods=['GET'])
def emails():
    return redirect('/emails_dash')
@server.route('/generate_random_code_for_validation',methods=['GET'])
def generate_random_code_for_validation():
    return redirect('/generate_random_code_for_validation_dash')
@server.route('/kidney_disease_prediction',methods=['GET'])
def kidney_disease_prediction():
    return redirect('/kidney_disease_prediction_dash')
@server.route('/predict_images',methods=['   GET'])
def predict_images():
    return redirect('/predict_images_dash')

app = DispatcherMiddleware(server, {
    '/app_dash': app_dash.server,
    '/cassanda_db_dash': cassandra_app.server,
    '/common_utils_dash': common_utils_dash_app.server,
    '/create_medical_report_dash': create_medical_report_dash_app.server,
    '/credentials_handling_dash': credentials_handling_dash_app.server,
    '/credentials_validation_dash': credentials_validation_dash_app.server,
    '/db_operations_dash': db_operations_dash_app.server,
    '/emails_dash': emails_dash_app.server,
    '/generate_random_code_for_validation_dash': generate_random_code_for_validation_dash_app.server,
    '/kidney_disease_prediction_dash': kidney_disease_prediction_dash_app.server,
    '/predict_images_dash': predict_images_dash_app.server,
})

run_simple('0.0.0.0', 8000, app, use_reloader=True, use_debugger=True)