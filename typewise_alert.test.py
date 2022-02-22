import unittest
from typewise_alert import battery_check_and_alert

batteryChar = {}
typewiseAlerterControllerLst = []
typewiseAlerterEmailLst = []
batteryCoolingTypesList = ["PASSIVE_COOLING","MED_ACTIVE_COOLING","HI_ACTIVE_COOLING"]
controllerAlertList = ["TOO_HIGH","TOO_HIGH","NORMAL"]
recipient = "a.b.c@bosch.com"
class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    for i in range(0,3):
      with self.subTest(i=i):
        self.assertTrue(typewiseAlerterControllerLst[i].classify_temperature_breach() == controllerAlertList[i])
        self.assertTrue(typewiseAlerterEmailLst[i].classify_temperature_breach() == "TOO_LOW")
        
  def test_send_alert_email(self):
    send_alert_email_string = "To: "+recipient+"\nHi, the temperature is too low"
    self.assertEqual(typewiseAlerterEmailLst[0].send_to_email("TOO_LOW"),send_alert_email_string)
    send_alert_email_string = "To: "+recipient+"\nHi, the temperature is too high"
    self.assertEqual(typewiseAlerterEmailLst[0].send_to_email("TOO_HIGH"),send_alert_email_string)
  
  def test_send_alert_controller(self):
    send_alert_controller_string = "65261, TOO_HIGH"
    self.assertEqual(typewiseAlerterControllerLst[0].send_to_controller("TOO_HIGH"),send_alert_controller_string)
    send_alert_controller_string = "65261, TOO_LOW"
    self.assertEqual(typewiseAlerterControllerLst[0].send_to_controller("TOO_LOW"),send_alert_controller_string)
  
  def test_check_and_alert(self):
    self.assertTrue(typewiseAlerterControllerLst[0].check_and_alert() == ("TO_CONTROLLER","TOO_HIGH"))
    self.assertTrue(typewiseAlerterEmailLst[0].check_and_alert() == ("TO_EMAIL","TOO_LOW"))

if __name__ == '__main__':
  for batteryCoolingType in batteryCoolingTypesList:
    batteryChar["coolingType"] = batteryCoolingType
    typewiseAlerterControllerLst.append(battery_check_and_alert("TO_CONTROLLER",batteryChar,45))
    typewiseAlerterEmailLst.append(battery_check_and_alert("TO_EMAIL",batteryChar,-1,recipient))
  
  unittest.main()
