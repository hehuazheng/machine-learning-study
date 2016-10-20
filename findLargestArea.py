def largestArea(heights):
    heights.append(0)
    size = len(heights)
    no_drease_size_stack = [0]
    max_size = heights[0]
    i = 0
    while i < size:
        cur_num = heights[i]
        if(not no_drease_size_stack or cur_num > heights[no_drease_size_stack[-1]]):
            no_drease_size_stack.append(i)
            i += 1
        else:
            index = no_drease_size_stack.pop()
            if no_drease_size_stack:
                width = i - no_drease_size_stack[-1] - 1
            else :
                width = i
            max_size = max(max_size, width * heights[index])
    return max_size
import  pdb
#pdb.set_trace()
height=[2,1,5,6,2,3,4,6,6,2,1]
print largestArea(height)

#print reduce(lambda (x, y) : x+y, sum(a, b))
