from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        ind = [i for i in range(n)]
        ind.sort(key=lambda x: positions[x])
        s = []
        for x in ind:
            if directions[x] == 'L':
                while s:
                    y = s[-1]
                    if healths[x] == healths[y]:
                        healths[x] = healths[y] = 0
                        s.pop()
                        break
                    if healths[x] > healths[y]:
                        healths[x] -= 1
                        healths[y] = 0
                        s.pop()
                    else:
                        healths[x] = 0
                        healths[y] -= 1
                        break
            else:
                s.append(x)
        r = [x for x in healths if x]
        return r


"""
lass Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:

        L, R, RLoc, Lmin = [], defaultdict(), set(), float('inf')
        for i, (pos, hp, drt)in enumerate(zip(positions, healths, directions)):
            if drt == "R":
                L.append((-pos, hp, i))
                Lmin = min(Lmin, pos)
            else:
                R[pos] = [hp, i]
                RLoc.add(pos)
        heapify(L)


        def robotFight(hp, enemyHp, pos, extra):
            if hp > enemyHp:
                hp -= 1
                RLoc.remove(pos + extra )
                R.pop(pos + extra)
            elif hp == enemyHp:
                RLoc.remove(pos + extra)
                R.pop(pos + extra)
                hp = 0
            else:
                R[pos + extra][1] -= 1
                if R[pos + extra][1] == 0:
                    RLoc.remove(pos + extra)
                    R.pop(pos + extra)
            return hp
        print(RLoc)
        while L and RLoc and max(RLoc) > Lmin:
            Lmin = float('inf')
            temp_L = []
            while L:
                pos, hp, i = heappop(L)
                pos = -pos
                print(pos)
                if pos + 1 in RLoc:
                    hp = robotFight(hp, R[pos+ 1][0],pos, 1 )
                if pos + 2 in RLoc and hp > 0:
                    hp = robotFight(hp, R[pos+2][0],pos, 2)
                if hp >0:
                    heappush(temp_L, (-pos - 1, hp , i + 1))
                    Lmin = min(Lmin, pos + 1)
            temp_R = set()
            for pos in RLoc:
                temp_R.add(pos - 1)
                hp1, i1 = R.pop(pos)
                R[pos -1] = [hp1,i]
            RLoc = temp_R
            L = temp_L

        print(RLoc, L)
        r = sorted([(0, R[num][0], R[num][1])for num in RLoc])
        ans = sorted(L + r, key = lambda x: x[2])
        return [b for a,b,c in ans]
        """
