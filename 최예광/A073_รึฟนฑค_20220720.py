class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        li = []
        for i in range(n):
            num = i+1
            if num%3 == 0 and num%5 == 0:
                li.append('FizzBuzz')
            elif num%3 == 0:
                li.append('Fizz')
            elif num%5 == 0:
                li.append('Buzz')
            else:
                li.append(str(num))
        return li
            