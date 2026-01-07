class Split:
    def solution(self):
        payment_summary={
            "hari":1200,
            "vipin":1400,
            "jhon":1000,
            "vishnu":0,
            "tom":120,
            "avinash":0,
            "jini":0,
            "asok":0
                    
        }
        total_amount=sum(payment_summary.values())
        amount_for_one_person=total_amount/len(payment_summary)
        result={k:amount_for_one_person-v for k,v in payment_summary.items()}
        print(result)
        
sp=Split()
sp.solution()