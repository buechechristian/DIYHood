########### Python 2.7 #############
import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'd2fda28c6dbd4a979a7382e321546376',
}

params = urllib.urlencode({
    # Request parameters
    'visualFeatures': 'Categories, Tags, Description, Faces, ImageType, Color, Adult',
})

def outputInfo(picurl):
	try:
   		with open( picurl, 'rb' ) as f:
			data = f.read()
		conn = httplib.HTTPSConnection('api.projectoxford.ai')
		conn.request("POST", "/vision/v1.0/analyze?%s" % params, data, headers)
		response = conn.getresponse()
		data = response.read()
		# print data
		data = data.lower()
		return data
		conn.close()
	except Exception as e:
		print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################
