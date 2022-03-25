from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
from django.test import TestCase
from . models import Waypoint

user = User(
  username = 'user1'
)

# Create your tests here.
class WaypointTest(TestCase):
  def setUp(self):
    self.type = Waypoint(
      name = 'home',
      userId = user,
      address = "621 West Galer St. Seattle, WA 98119"
    )
  
  def test_tablename(self):
    self.assertEqual(str(self.type._meta.db_table), 'waypoint')
  
  def test_userId(self):
    self.assertTrue(self.type.userId)