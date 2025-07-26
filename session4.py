'''
consultation:
weight, fever, sugar, remarks, medicines, followup, created_on, bp

'''
import datetime

class consultaion:
      def __init__(self, weight=0, sugar =80, fever= 98.4, bphigh=120,bplow = 80, remarks='', 
                 medicines='', followup='', doctor_id='', patient_id = ''):
            self.weight = weight
            self.sugar = sugar
            self.fever = fever
            self.bphigh = bphigh
            self.bplow = bplow
            self.remarks = remarks
            self.medicines = medicines
            self.followup = followup
            self.doctor_id = doctor_id
            self.patient_id = patient_id
            self.create_on = datetime.datetime.now()
            
      def to_document(self):
         return vars(self) 