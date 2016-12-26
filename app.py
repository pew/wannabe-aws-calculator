from flask import Flask, render_template, request, jsonify, json

app = Flask(__name__)

file = open('assembled.json', 'r')
content = json.loads(file.read())

def locations(value=""):
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
        "sa-east-1": "South America (Sao Paulo)"
    }
    if not value:
        return location
    else:
        return location[value]

@app.route('/')
def index():
    return render_template('index.html', locations=locations())

@app.route('/v1/regions', methods=['GET'])
def regions():
    return jsonify(locations())

@app.route('/v1/get_pricing', methods=['GET'])
@app.route('/v1/get_pricing/<region>', methods=['GET'])
@app.route('/v1/get_pricing/<region>/<instanceType>', methods=['GET'])
def get_data(region=None, instanceType=None):
    if region and instanceType:
        filtered = []
        for k,v in locations().items():
            if k in region:
                for reg in content:
                    if reg['location'] == v and reg['instanceType'] == instanceType:
                        filtered.append(reg)
        return jsonify(filtered)

    if region:
        filtered = []
        for k,v in locations().items():
            if k in region:
                for reg in content:
                    if reg['location'] == v:
                        filtered.append(reg)
        return jsonify(filtered)

    else:
        return jsonify(content)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
