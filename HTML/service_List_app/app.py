from flask import Flask, render_template, request
import json

app = Flask(__name__)

lst = ['crud', 'ahs', 'ahr', 'l1t', 'l2t', 'mm', 'mcp']

@app.route('/')
def index():
    if request.method == 'GET':
        return render_template('select_services.html', services=lst)
    else:
        return "Invalid request method."


@app.route('/services', methods=['POST'])
def services():
    selected_services = request.form.getlist('service')
    services = lst
    return render_template('enter_options.html', services=services, selected_services=selected_services)

@app.route('/submit', methods=['POST'])
def submit():
    data = {}
    for service in request.form:
        if service != 'submit':
            data[service] = request.form.getlist(service)
    json_data = json.dumps(data)
    return render_template('result.html', json_data=json_data)

if __name__ == '__main__':
    app.run(debug=True)
