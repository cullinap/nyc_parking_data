import pandas as pd 
from sodapy import Socrata
from dataclasses import dataclass


@dataclass
class Ticket:
    data: float
    
    @property 
    def calc_payments(self):
        return ( 
            (
                self.data 
                .payment_amount
                .astype(float)
                .sum()
            )
        )

    @staticmethod
    def get_results(licensePlate):
        client = Socrata("data.cityofnewyork.us", None) 
        query = f"""select * where plate = '{licensePlate}' """

        results = client.get(
            "nc67-uf89"
            , query=query
        )

        results_df = pd.DataFrame.from_records(results)

        return Ticket(
            data = (
                results_df
            )
        )

ticket = Ticket.get_results('P91HUV')
print(ticket.calc_payments)