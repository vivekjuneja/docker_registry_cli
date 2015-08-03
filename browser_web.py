import subprocess

from flask import Flask
app = Flask(__name__, static_folder='css')

@app.route('/gravity/docker/registry')
def get_docker_registry():

    p = subprocess.Popen(['python', 'browser.py', '10.52.179.181:5000', 'list', 'all'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out


@app.route('/gravity/components')
def hello_world():

    p = subprocess.Popen(['python', 'browser.py', '10.52.179.181:5000', 'list', 'all'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out


@app.route('/css/<path:path>')
def send_js(path):
	print path
	return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(host='10.52.179.181', port=9001)
