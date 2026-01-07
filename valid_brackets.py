class ValidBrackets:
    def solution(self,input):
       
        symbol_dict={"{":"}","[":"]","<":">","(":")"}
        sample_stack=[]
        is_valid=True
        if len(input)%2!=0:
            is_valid=False
        else:
            for i in input:
                if i in symbol_dict.keys():
                    sample_stack.append(i)
                elif len(sample_stack)==0:
                    is_valid=False
                    break

                elif symbol_dict[sample_stack[-1]]!=i:
                    is_valid=False
                    break

                elif symbol_dict[sample_stack[-1]]==i:
                    sample_stack.pop()

        print(is_valid)
insatance=ValidBrackets()
insatance.solution("({})}")



                


