class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        tupob = set()
        for x,y in obstacles:
            tupob.add((x,y))
        # obstacles =  set(obstacles)
        direction = 0
        position = [0,0] #xcor = [0] ycor = [1]
        #0 is up 90 is right 180 is down 270 is left
        distance = 0
        for i in commands:
            if i == -1:
                direction +=90
                direction = direction%360
            elif i == -2:
                direction -=90
                direction = direction%360

            else:
                if direction == 0:
                    for j in range( position[1]+1 , (position[1]+i) +1): #movement up
                        # print(j)
                        if (position[0], j) in tupob:
                            position[1] = j-1
                            break
                        else:
                            position[1]+=1

                if direction == 180:
                    for j in range( position[1]-1 , (position[1]-i) -1, -1): #movement down
                        # print(j)
                        if (position[0], j) in tupob:
                            position[1] = j+1
                            break
                        else:
                            position[1]-=1

                if direction == 90:
                    for j in range( position[0]+1 , (position[0]+i) +1,): #movement right
                        # print(j)
                        if (j,position[1]) in tupob:
                            position[0] = j-1
                            break
                        else:
                            position[0]+=1        


                if direction == 270:
                    for j in range( position[0]-1 , (position[0]-i) -1, -1): #movement left
                        # print(j)
                        if (j,position[1]) in tupob:
                            position[0] = j+1
                            break
                        else:
                            position[0]-=1        

                distance = max((position[0]**2+position[1]**2), distance)
                print(position)
        return distance
