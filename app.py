from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

file = open('assembled.json', 'r')
content = json.loads(file.read())

location = {
    "us-east-1": "US East (N. Virginia)",
    "us-east-2": "US East (Ohio)",
    "us-west-1": "US West (N. California)",
    "us-west-2": "US West (Oregon)",
    "ca-central-1": "Canada (Central)",
    "ap-south-1": "Asia Pacific (Mumbai)",
    "ap-northeast-2": "Asia Pacific (Seoul)",
    "ap-southeast-1": "Asia Pacific (Singapore)",
    "ap-southeast-2": "Asia Pacific (Sydney)",
    "ap-northeast-1": "Asia Pacific (Tokyo)",
    "eu-central-1": "EU (Frankfurt)",
    "eu-west-1": "EU (Ireland)",
    "eu-west-2": "EU (London)",
    "sa-east-1": "South America (São Paulo)"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_pricing', methods=['GET'])
@app.route('/get_pricing/<region>', methods=['GET'])
def get_data(region=None):
    if not region:
        return jsonify(content)

    if region:
        filtered = []
        for k,v in location.items():
            if k in region:
                for reg in content:
                    if reg['location'] == v:
                        filtered.append(reg)
        return jsonify(filtered)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
