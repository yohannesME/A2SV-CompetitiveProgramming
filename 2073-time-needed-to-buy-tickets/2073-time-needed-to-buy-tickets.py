class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        #add the values less to finish first and if equal check thier index becuase it he runs first they will run one less than the k value
        output = 0
        for index,ticket in enumerate(tickets):
            if ticket < tickets[k]:
                output += ticket
            else:
                if index <= k:
                    output += tickets[k]
                else:
                    output += tickets[k]-1
            
        return output