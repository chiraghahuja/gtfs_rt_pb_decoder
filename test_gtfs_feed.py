from google.transit import gtfs_realtime_pb2
import urllib


# generic way to read .pb file : protoc --decode_raw < file.pb
# for gtfs specifc way to read .pb file, see below. Use gtfs_realtime_pb2 

        # fuck google for not using json and inventing the piece of shit that is protobuf
        # fuck google for incentivizing their engineers to complicate simple things for promotion


feed = gtfs_realtime_pb2.FeedMessage()

with open('StlRealTimeTrips.pb', 'rb') as f:
    feed.ParseFromString(f.read())

# feed object is a FeedMessage object. 
# FeedMessage has a field called entity which is a list of Entity objects
# Entity has a field called trip_update which is a TripUpdate object
# TripUpdate has a field called trip which is a TripDescriptor object
# TripDescriptor has a field called trip_id which is a string
# TripUpdate has a field called stop_time_update which is a list of StopTimeUpdate objects
# StopTimeUpdate has a field called stop_sequence which is an int
# StopTimeUpdate has a field called arrival which is a StopTimeEvent object
#    has a field called delay which is an int

# print(f'''trip_id: {feed.entity[0].trip_update.trip.trip_id}''')



print(f'''type of object: {type(feed)}''')
print(f'''type of entities: {type(feed.entity)}''')
print(f'''type of entity: {len(feed.entity)}''')

# response = urllib.urlopen('URL OF YOUR GTFS-REALTIME SOURCE GOES HERE')
# feed.ParseFromString(response.read())

# for entity in feed.entity:
#   if entity.HasField('trip_update'):
#     print (entity.trip_update)
