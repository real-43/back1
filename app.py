# import PIL.Image as Image
# from flask import Flask, request
# from flask_cors import CORS
# import json
# import face_rec as FaceRec
# import base64
# import io
# import os
# import shutil
# import time


# app = Flask(__name__)
# CORS(app)


# @app.route('/api', methods=['POST', 'GET'])
# def api():
# 	data = request.get_json()
# 	resp = 'Nobody'
# 	directory = './stranger'
# 	if data != '':
# 		if  os.path.exists(directory):
# 			shutil.rmtree(directory)

# 		if not os.path.exists(directory):
# 			try:
# 				os.mkdir(directory)
# 				time.sleep(1)
# 				result = data['data']
# 				b = bytes(result, 'utf-8')
# 				image = b[b.find(b'/9'):]
# 				im = Image.open(io.BytesIO(base64.b64decode(image)))
# 				im.save(directory+'/stranger.jpeg')
# 				resp = FaceRec.main("stranger/stranger.jpeg")
# 			except Exception as e:
# 				print(e)
# 	return resp


	







# if __name__ == '__main__':
# 	app.run()








import PIL.Image as Image
from flask import Flask, request
from flask_cors import CORS
import json
import face_rec as FaceRec
import comapare as Comp
import base64
import io
import os
import shutil
import time


app = Flask(__name__)
CORS(app)


@app.route('/api', methods=['POST', 'GET'])
def api():
	data = request.get_json()
	resp = []
	directory = './stranger'
	if data != '':
		if  os.path.exists(directory):
			shutil.rmtree(directory)

		if not os.path.exists(directory):
			try:
				os.mkdir(directory)
				time.sleep(1)
				result = data['data']
				b = bytes(result, 'utf-8')
				image = b[b.find(b'/9'):]
				im = Image.open(io.BytesIO(base64.b64decode(image)))
				im.save(directory+'/stranger.jpeg')
				matchs = Comp.main("stranger/stranger.jpeg")
				resp.append(FaceRec.main("stranger/stranger.jpeg"))
				resp.append(matchs[0])
				resp.append(matchs[1])
				print(resp)
			except Exception as e:
				print(e)
	try :
		ans = f"{resp[0]}_{resp[1][0]}_{resp[2][0]}"
		return ans
	except :
		return "Fail to compare"


	







if __name__ == '__main__':
	app.run()