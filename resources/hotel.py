from flask_restful import Resource

class Hoteis(Resource):
    def get(self):
        return {'hoteis': 'meus_hoteis'}