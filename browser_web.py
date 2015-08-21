import subprocess

from flask import Flask
app = Flask(__name__, static_folder='css')

@app.route('/registry/search')
def get_docker_registry():

    p = subprocess.Popen(['python', 'browser.py', 'localhost:9443', 'html', 'all', 'ssl'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out


@app.route('/css/<path:path>')
def send_js(path):
	print path
	return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(host='localhost', port=9001)
