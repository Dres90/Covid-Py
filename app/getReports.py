import json
import requests
from app import db, app
from app.models import Report, Date
from datetime import datetime


def load_reports():
    r = requests.get(app.config['API_URL'])
    if r.status_code != 200:
        return 'Error: the information request failed.'
    if not r.content:
        return 'Error: response is empty.'
    j = json.loads(r.content)
    c = j['countries']
    for key in c:
        country = c[key]
        existingC = Report.query.get(key)
        if not existingC:
            new = Report(id=key, name=country['name'], flag=country['flag'],
                         reports=country['reports'], cases=country['cases'],
                         deaths=country['deaths'],
                         recovered=country['recovered'],
                         lat=country['lat'], lng=country['lng'],
                         deltaCases=country['deltaCases'],
                         deltaDeaths=country['deltaDeaths'])
            db.session.add(new)
        else:
            existingC.name = country['name']
            existingC.flag = country['flag']
            existingC.reports = country['reports']
            existingC.cases = country['cases']
            existingC.deaths = country['deaths']
            existingC.recovered = country['recovered']
            existingC.lat = country['lat']
            existingC.lng = country['lng']
            existingC.deltaCases = country['deltaCases']
            existingC.deltaDeaths = country['deltaDeaths']
        time = Date.query.get('lu')
        if not time:
            newTime = Date(id='lu', timestamp=datetime.utcnow())
            db.session.add(newTime)
        else:
            time.timestamp = datetime.utcnow()
        db.session.commit()
    return 'Updated Correctly'
