class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(s_arr,i):
            if len(s_arr) == len(digits):
                res.append("".join(s_arr))
                return
            for letter in digit_to_letters[digits[i]]:
                s_arr.append(letter)
                backtrack(s_arr,i+1)
                s_arr.pop()
        backtrack([],0)
        return res
            
