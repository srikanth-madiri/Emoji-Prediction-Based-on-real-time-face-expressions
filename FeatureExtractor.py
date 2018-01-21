import urllib, json
import requests

img_filename = "z_Image.png"
with open(img_filename, 'rb') as f:
    img_data = f.read()

# Replace the subscription_key string value with your valid subscription key.
subscription_key = '56bc3a421fb4406e8383d0f00e6a7ac7'

## Request headers.
header = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

# Request parameters.
params = urllib.parse.urlencode({
     'returnFaceId': 'true',
     'returnFaceLandmarks': 'false',
     'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
})

api_url = "https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize?%s"%params

r = requests.post(api_url,
#                  params=params,
                  headers=header,
                  data=img_data)

data_1 = r.json()

#data_1 = json.loads(data)
types=["anger", 'contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise']
counter_types = 0
Result_dictionary = {}
Intermediate_dictionary = {}
#arr=[]
for i in types:
    if counter_types <= 7:
        score_1=data_1[0]['scores'][i]
        Intermediate_dictionary[i]=float('%f'%score_1)
            #arr.append('%f'%score_1)
        Result_dictionary.update(Intermediate_dictionary)
        counter_types+=1
    #print(max(arr))
    #Max_value_found=max(Result_dictionary.values())
Emoji_text=list(Result_dictionary.keys())[list(Result_dictionary.values()).index(max(Result_dictionary.values()))]
#print(Emoji_text)


