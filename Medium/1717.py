'''

Intuition

1)This is a tough problem and it took me awhile to figure out.
2)First you need to realize b can be in both options. So we want to be greedy with our b's. We always want to pick the bigger payout.
3)So if x>y then we want ab first and likewise ba first if y>x.
4)I create a helper function to keep the layout the same. If y is bigger than x then we reverse x and y and ab and ba. This way it stays in the same format.
5)Now go through once and look for all the bigger payout option which will now always be option a.
6)Then go through what is left of your stack again, looking for option b.
7)Return the total
8)How to come up with this approach? First I looked at the parameters and knew we couldn't do dp. Second I knew it was O(n) since sorting couldn't be done or binary search. Since it was O(n) then it had to be greedy as there were several choices. Then I thought about looking at elements in groups of 3 but realized the condensing was too much. Therefore the only option was to go through twice with greedy.

Space - O(n) from the stack which could have n options, n = len(s)
Time - O(2n) ~ O(n) since we go through s twice.

'''

class Solution:
    def goThrough(self,x,y,a,b,s):
        ans = 0
        for combo in (a,b):
            stack = []
            for i in range(len(s)):
                if stack and stack[-1] + s[i] == combo:
                    ans += x
                    stack.pop()
                else: stack.append(s[i])
            x = y
            s = "".join(stack)
        return ans
    def maximumGain(self, s: str, x: int, y: int) -> int:
        return self.goThrough(x,y, "ab", "ba", s) if x > y else self.goThrough(y,x,"ba", "ab", s)