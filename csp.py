from flask import Flask, make_response, request, render_template, send_from_directory
import os.path


app = Flask(__name__)
global csps
csps = {
    1: "script-src 'self' data:; object-src 'none'",
    2: "script-src https://google.com 'unsafe-inline';",
    3: "script-src *; object-src 'none'",
    4: "script-src 'self'",
    5: "script-src 'self' https://www.google.com; object-src 'none';",
    6: "script-src 'self'; object-src 'none'",
    7: "script-src https://google.com 'unsafe-eval';",
    8: "script-src 'self' https://google.com https: data *;" ,
    9: "script-src https://cdnjs.cloudflare.com 'unsafe-eval';",
    10: "default-src 'self'; connect-src 'self'; script-src 'self';",
    11: "script-src 'self' ajax.googleapis.com; object-src 'none' ;report-uri /Report-parsing-url;",
    12: ""
}


@app.get("/lab/<int:id>/search")
def search(id):
    item = request.args.get("search")
    response = make_response(f"<h2>'{item}' not found</h2>")
    csp = csps.get(id)

    if csp is not None:
        response.headers["Content-Security-Policy"] = csp
    return response

@app.route("/", methods=['GET', 'POST'])
def index():
    res = make_response(render_template("index.html", csps=csps))
    if request.args.get('csp'):
        csps[len(csps)+1] = request.args.get('csp')
        res = make_response(render_template("index.html", csps=csps))

    return res
@app.get("/uploads/<path:filename>")
def uploads(filename):
    return send_from_directory("C:\\tmp\\uploads", filename)


if __name__ == "__main__":
    app.run("127.0.0.1", "8001")




