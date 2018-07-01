from chalice import Chalice, Response
from botocore.vendored import requests


app = Chalice(app_name='backend')
app.debug = True

bysykkel_api = "https://oslobysykkel.no/api/v1/"
bysykkel_key = "ad9164a3bb6fea78ff68574ac03e54cb"
bysykkel_header = {"Client-Identifier": bysykkel_key}


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route("/bikes/{stationId}", cors=True)
def stationIdInfo(stationId):
    content = requests.get(bysykkel_api + "stations", headers=bysykkel_header)
    stations = content.json()["stations"]
    station = None
    bikes = 0
    locks = 0
    for s in stations:
        if s["id"] == int(stationId):
            station = s
            break
    if not station:
        return Response(body={"msg": "Not found"}, status_code=404)

    content = requests.get(
        bysykkel_api + "stations/availability", headers=bysykkel_header)
    stations = content.json()["stations"]
    for s in stations:
        if s["id"] == int(stationId):
            bikes = s["availability"]["bikes"]
            locks = s["availability"]["locks"]
            break

    return {"name": station["title"],
            "subtitle": station["subtitle"],
            "nLocks": station["number_of_locks"],
            "availableBikes": bikes,
            "availableLocks": locks,
            }


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
