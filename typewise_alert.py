batteryChar = {'coolingType':"PASSIVE_COOLING"}

class send_alert:
  
  send_alert_dcn = {'TO_CONTROLLER':"send_to_contoller", 'TO_EMAIL':"send_to_email"}
  breach_dcn = {'TOO_LOW':'Hi, the temperature is too low','TOO_HIGH':'Hi, the temperature is too high'}

  def send_to_controller(self,breachType):
    header = 0xfeed
    print(f'{header}, {breachType}')

  def send_to_email(self,breachType):
    print(f'To: {self.recepient}')
    print(self.breach_dcn[breachType])

class battery_check_and_alert(send_alert):
  coolingType_dcn = {'PASSIVE_COOLING':(0,35),'HI_ACTIVE_COOLING':(0,45),'MED_ACTIVE_COOLING':(0,40)}
  def __init__(self,alertTarget, batteryChar, temperatureInC,recepient):
    self.alertTarget = alertTarget
    self.coolingType = batteryChar["coolingType"]
    self.temperatureInC = temperatureInC
    self.recepient = recepient

  def classify_temperature_breach(self):
    return self.infer_breach(self.coolingType_dcn[self.coolingType][0], self.coolingType_dcn[self.coolingType][1])
  
  def infer_breach(self,lowerLimit,upperLimit ):
    if self.temperatureInC in range(lowerLimit,upperLimit):
      return 'NORMAL'
    if self.temperatureInC > upperLimit:
      return 'TOO_HIGH'
    return("TOO_LOW")

  def check_and_alert(self):
    breachType = self.classify_temperature_breach()
    getattr(self,self.send_alert_dcn[self.alertTarget])(breachType)
  

myAlerter = battery_check_and_alert("TO_EMAIL",batteryChar,45,"a.b@c.com")
myAlerter.check_and_alert()
