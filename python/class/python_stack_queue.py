class Solution:
    def __init__(self):
        self.stack = list()
        self.queue = list()

    def pushCharacter(self, char):
        self.stack.append(char)

    def popCharacter(self):
        return self.stack.pop(-1)

    def enqueueCharacter(self, char):
        self.stack.append(char)

    def dequeueCharacter(self):
        return self.stack.pop(0)

s = 'madam'
obj = Solution()

for i in range(len(s)):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True

for i in range(len(s) // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break

if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")