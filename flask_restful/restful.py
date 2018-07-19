"""
flask restful 
"""

from flask import Flask,jsonify
from flask_restful import Resource,Api
from faker import Faker

app = Flask(__name__)
api = Api(app)
faker = Faker()

def fake_data():
	data = []
	for i in range(10):
		tmp = {
			"name":faker.name(),
			"address":faker.address(),
			"job":faker.job()
		}
		data.append(tmp)
	return data


class Data(Resource):
	def get(self):
		data = {
			"data":fake_data()
		}
		return jsonify(data)

api.add_resource(Data,'/')


if __name__ == '__main__':
	app.run(debug=True)




