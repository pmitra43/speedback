class Pair:
    def __init__(self, member1, member2):
        self.member1=member1
        self.member2=member2
    
    def __repr__(self):
        return str(self.member1 + "-" + self.member2)
    
    def containsCommonMember(self, other):
        return (self.__class__ == other.__class__ and
        (self.member1==other.member1 or
        self.member1==other.member2 or
        self.member2==other.member1 or
        self.member2==other.member2))


class SpeedbackMatrix:
    def generatePairs(self, members):
        pairs = []
        for i in range(len(members)):
            for j in range(i+1, len(members)):
                pairs.append(Pair(members[i], members[j]))
        return pairs

    def defineGrid(self, memberCount):
        grid=[[None for y in range(int(memberCount/2))]for x in range(memberCount-1)]
        return grid

    def isSafe(self, pair, grid, rowIndex):
        result = False
        for element in grid[rowIndex]:
            if(pair.containsCommonMember(element)):
                result = False
                break
            if(element is None):
                result = True
        return result

    def placeElementInGrid(self, grid, pairs, index):
        if(index>=len(pairs)):
            return (True, grid)
        for rowIndex in range (len(grid)):
            if(self.isSafe(pairs[index], grid, rowIndex)):
                for columnIndex in range(0, len(grid[rowIndex])):
                    if grid[rowIndex][columnIndex] is None:
                        grid[rowIndex][columnIndex]=pairs[index]
                        break
                if(self.placeElementInGrid(grid, pairs, index+1)[0]):
                    return (True, grid)
                grid[rowIndex][columnIndex]=None
        return (False, grid)
    
    def populateGrid(self, members):
        if((len(members)&1) == 1):
            members.append('None')
        pairs=self.generatePairs(members)
        grid=self.defineGrid(len(members))
        finalGrid=self.placeElementInGrid(grid, pairs, 0)
        return finalGrid[1]