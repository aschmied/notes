# Based on Knative's helloworld-python example:
#     https://knative.dev/docs/serving/samples/hello-world/helloworld-python/

import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def root_route():
    return '42\n'

def main():
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)

if __name__ == "__main__":
    main()
