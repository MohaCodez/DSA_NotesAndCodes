def letterCombinations(self, digits: str) -> List[str]:
        res = []
        table = {'2':'abc', 
                '3':'def', 
                '4':'ghi', 
                '5':'jkl', 
                '6':'mno', 
                '7':'pqrs', 
                '8':'tuv', 
                '9':'wxyz'}

        if(len(digits)==0):
            return res
        
        def backtrack(i, cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            for c in table[digits[i]]:
                backtrack(i + 1, cur + c)

        backtrack(0, '')
        return res