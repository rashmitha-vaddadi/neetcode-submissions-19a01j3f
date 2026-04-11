class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ##greedy solution as we want min no of boats
        ##first we need to sort it
        people.sort()
        boats = 0
        l = 0
        r = len(people)-1
        while l<=r:
            if people[r] == limit:
                boats += 1
                r -= 1
            elif people[l]+people[r]<=limit:
                boats+=1
                l+=1
                r-=1
            else:
                boats+=1
                r-=1
        return boats

        