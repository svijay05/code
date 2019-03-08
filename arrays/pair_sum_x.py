

"""


Find a pair in an array of size 'n', whose sum is X

There are at most 2 operations performed on every element: 
(a) the element is added to the curr_sum 
(b) the element is subtracted from curr_sum. 
So the upper bound on number of operations is 2n which is O(n).


"""



def find_sub_array(a,sum):
    curr_sum = 0

    i,j= 0,0

    while i < len(a):

        curr_sum = curr_sum  + a[i]
        #print(curr_sum)
        if curr_sum == sum:
            return (i,j)
        elif curr_sum > sum:
            while(curr_sum > sum and j<i):
                print("{} - {} - {}".format(i,j,curr_sum))
                curr_sum = curr_sum - a[j]
                j=j+1
                if(curr_sum == sum):
                    return i,j
        else:
            i=i+1

    return (i,j)


"""

def find_all_sub_arrays(a,sum):
    curr_sum = 0

    i,j= 0,0

    while i < len(a):

        curr_sum = curr_sum  + a[i]
        #print(curr_sum)
        if curr_sum == sum:
            print (j,i)
            curr_sum = curr_sum - a[j]
            j=j+1
            i=i+1

        elif curr_sum > sum:
            while(curr_sum > sum and j<i):
                print("{} - {} - {}".format(i,j,curr_sum))
                curr_sum = curr_sum - a[j]
                j=j+1
                if(curr_sum == sum):
                    return i,j
        else:
            i=i+1

    return (i,j)
"""

if __name__ == "__main__":
    a = [1,5,10,100,1000]
    sum =  115
    i,j = find_sub_array(a,sum)

    print("Found {} - {} ".format(j,i))


