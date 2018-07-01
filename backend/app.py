from chalice import Chalice, Response
from botocore.vendored import requests
import datetime


app = Chalice(app_name='backend')
app.debug = True

bysykkel_api = "https://oslobysykkel.no/api/v1/"
bysykkel_key = "ad9164a3bb6fea78ff68574ac03e54cb"
bysykkel_header = {"Client-Identifier": bysykkel_key}

entur_header = {"ET-Client-Name": "espens-infoskjerm"}


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route("/bikes/{stationId}", cors=True)
def station_id_info(stationId):
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


@app.route("/ruter/stopp/{stopId}", cors=True)
def get_departures_from_stop(stopId):
    now = datetime.datetime.now().isoformat()
    print(now)
    query = '''
{
  stopPlace(id: "''' + stopId + '''") {
    id
    name
    estimatedCalls(startTime:"''' + now + '''" timeRange: 72100, numberOfDepartures: 10) {     
      realtime
      aimedArrivalTime
      aimedDepartureTime
      expectedArrivalTime
      expectedDepartureTime
      actualArrivalTime
      actualDepartureTime
      date
      forBoarding
      destinationDisplay {
        frontText
      }
      quay {
        id
      }
      serviceJourney {
        journeyPattern {
          line {
            id
            name
            transportMode
          }
        }
      }
    }
  }
}

'''

    request = requests.post(
        "https://api.entur.org/journeyplanner/2.0/index/graphql", json={"query": query}, headers=entur_header)

    return request.json()
