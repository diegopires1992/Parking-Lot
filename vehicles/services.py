from datetime import datetime,timezone
from pricings.models import Price
from pricings.serializers import PriceSerializers



class PaymentAmountServices():
    def __init__(self,paid_at,arrived_at):
        self.paid_at = paid_at
        self.arrived_at = arrived_at
    
    def amount_paid(self):
        price = Price.objects.all().last()
        price = PriceSerializers(price)

        diff_time = self.paid_at - self.arrived_at
        seconds = diff_time.total_seconds()
        hours = seconds/60
        
        value = price.data['a_coefficient'] + price.data['b_coefficient'] * hours//24
        return value