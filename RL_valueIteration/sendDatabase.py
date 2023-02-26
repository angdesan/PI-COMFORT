import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db

cred = credentials.Certificate(
    './energy-coach-f5270-firebase-adminsdk-o4rki-881d6550e6.json')
app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://energy-coach-f5270-default-rtdb.firebaseio.com/'
})
print(app.name)

dbF = firestore.client()


def sendToFirestoreRecomendationsNState(status_ac, temp_ext, time, comfort, state, new_state, action):
    data = {
        u'date': time,
        u'status_ac': status_ac,
        u'temp_ext': temp_ext,
        u'comfort': comfort,
        u'state': state,
        u'new_state': new_state,
        u'action': action
    }
    dbF.collection(u'historicalCollection').add(data)
    return None


ref = db.reference("recomendation")
