from boto import s3
from boto.s3.key import Key
from boto.s3.connection import Location
from boto.s3.connection import S3Connection

class BotoxException(Exception): pass

class Botox(object):
  def __init__(self, access_key, secret_key):
    """Constructor to connect to AWS s3"""
    try:
      self.conn = S3Connection(access_key, secret_key)
    except Exception, e:
      raise BotoxException(e)

  def create_bucket(self, bucket, location):
    """Create bucket in a specified location """
    if location in self.get_locations:
      try:
        return self.conn.create_bucket(bucket, location=location)
      except Exception, e:
        raise BotoxException(e)
    else:
      raise BotoxException("[%s] not a valid location" %location)

  def set_contents(self, bucket, key, value):
    """store new data in S3 bucket"""
    try:
      __bucket__ = self.conn.get_bucket(bucket)
      __k__ = Key(__bucket__)
      __k__.key = key
      __k__.set_contents_from_string(value)
    except Exception, e:
      raise BotoxException(e)

  def get_contents(self, bucket, key):
    """Get value from S3 bucket """
    try:
      __bucket__ = self.conn.get_bucket(bucket)
      __k__ = Key(__bucket__)
      __k__.key = key
      return __k__.get_contents_from_string()
    except Exception, e:
      raise BotoxException(e)

  def get_regions(self):
    """Get all available regions for the Amazon S3 service."""
    return s3.regions()

  def get_locations(self):
    """Get all the locations"""
    return [i for i in dir(Location) if i[0].isupper()]
