from google.transit import gtfs_realtime_pb2
import urllib

feed = gtfs_realtime_pb2.FeedMessage()

with open('StlRealTimeTrips.pb', 'rb') as f:
    feed.ParseFromString(f.read())


print(f'''type of object: {type(feed)}''')
print(f'''type of entities: {type(feed.entity)}''')

# response = urllib.urlopen('URL OF YOUR GTFS-REALTIME SOURCE GOES HERE')
# feed.ParseFromString(response.read())
# for entity in feed.entity:
#   if entity.HasField('trip_update'):
#     print entity.trip_update
