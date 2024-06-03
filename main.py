import os

from flask import Flask
from get_stories import get_stories

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"


@app.route("/pull_top_stories")
def hello_world2():
    """Example Hello World route."""
    get_stories()
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
