import requests
import time
import boto3
def fn(theater):  
  URL = "https://www.cineplex.com/api/v1/theatres/"+theater+"/availablemoviesoneposter/dates"
  #4114 4108
  r = requests.get(url = URL)
  data = r.json()
  n=0
  movies=""
  if theater == "4108":
    movies+="SouthLand :"+"\n"
  if theater == "4114":
    movies+="NormanView :"+"\n"
  while n < data['totalCount']:
    film=str(data['data'][n]['movie']['presentationType'])
    if film == "Film Presentation" and data['data'][n]['movie']['isNowPlaying']:
      movies+=str(data['data'][n]['movie']['name'])+".\n"
    n+=1
  sms(movies)


def sms(movies):
  client = boto3.client("sns",aws_access_key_id="AKIAI4NGYRIQVKZ3IT3Q",aws_secret_access_key="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",region_name="us-east-1")
  client.publish(PhoneNumber="+13065024823",Message=movies)

while True:  
  try:
      fn("4108")
      fn("4114")
  except:
      print('Linux function was not executed')
  time.sleep(172800)
