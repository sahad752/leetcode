def furthestBuilding( heights, bricks: int, ladders: int) :
    for i in range(len(heights)-1):
        if heights[i]>=heights[i+1]:
            continue
        else:
            bricks_needed = heights[i+1] - heights[i]
            bricks-=bricks_needed
            if bricks>=0:
                continue
            elif ladders>0:
                ladders-=1
                bricks+=bricks_needed
                continue
            else:
                return i
    return i+1

result = furthestBuilding([1,5,1,2,3,4,10000]
,bricks=4,ladders=1)
print(result)