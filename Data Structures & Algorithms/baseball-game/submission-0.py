class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in range(0, len(operations)):
            if operations[i] == "+":
                res.append(res[len(res) - 1] + res[len(res) - 2])
            elif operations[i] == "D":
                n = res[len(res) - 1]
                res.append(n *2)
            elif operations[i] == "C":
                res.pop()
            else:
                res.append(int(operations[i]))
                
        return sum(res)


            

        