import random, time, sys

# function was copied from Chapter 5 of Problem Solving with Algorithms and Data Structures by Miller and Ranum
def sequential_search(a_list, item):
    start = time.time() # modified function: capture start time to determine length of time of function operating
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1

    end = time.time() # modified function: capture end time to determine length of time of function operating
    return found, end-start # modified function: returned difference to report length of time of function operating
#returns if values is found or not

# function was copied from Chapter 5 of Problem Solving with Algorithms and Data Structures by Miller and Ranum
def ordered_sequential_search(a_list, item):
    start = time.time() # modified function: capture start time to determine length of time of function operating
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1

    end = time.time() # modified function: capture end time to determine length of time of function operating
    return found, end-start # modified function: returned difference to report length of time of function operating
#returns if values is found or not

# function was copied from Chapter 5 of Problem Solving with Algorithms and Data Structures by Miller and Ranum
def binary_search_iterative(a_list, item):
    start = time.time() # modified function: capture start time to determine length of time of function operating
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end = time.time() # modified function: capture end time to determine length of time of function operating
    return found, end-start # modified function: returned difference to report length of time of function operating
#returns if values is found or not

# function was copied from Chapter 5 of Problem Solving with Algorithms and Data Structures by Miller and Ranum
def binary_search_recursive(a_list, item, start=time.time()): # modified function: capture start time to determine length of time of function operating
# placed start value in parameters so that the same value would be passed regardless of the function recursively calling itself again
    if len(a_list) == 0:
        end = time.time() # modified function: capture end time to determine length of time of function operating
        return False, end-start # modified function: returned difference to report length of time of function operating
        #returns if values is found or not
    else:
        midpoint = len(a_list) // 2

    if a_list[midpoint] == item:
        end = time.time() # modified function: capture end time to determine length of time of function operating
        return True, end-start # modified function: returned difference to report length of time of function operating
        #returns if values is found or not
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item, start) # passing the same constant start value along with recursively calling the function again for half the list
        else:
            return binary_search_recursive(a_list[midpoint + 1:], item, start) # passing the same constant start value along with recursively calling the function again for half the list

# makes the lists required for searches and stores them within a bigger list; size dictates how many elements in the smaller lists; amount dictates number of lists in the bigger list
def makeLists(size, amount):

    allRandList = list() # this list will contain the 100 lists required within itself to later calculate an average between the results of all the lists

    for y in range(0, amount):
        randList = list() # list of random integer values

        for x in range(0, size):
            randList.append(random.randint(0, sys.maxint)) # places an integer from 0 to the maximum integer by the system

        allRandList.append(randList)

    return allRandList # returns the list that contains the lists of random positive integers

# will perform sequential search, ordered sequential search, binary searches (iterative and recursive) on a specified list of lists
# calculates averages of run times on all the lists
def doAllSearches(lists):

    numberOfLists = len(lists)

    # will store run times for the searching in this list for each list within the bigger list
    calcSSAvg = list()
    calcOSSAvg = list()
    calcBSIAvg = list()
    calcBSRAvg = list()

    # one iteration represents one list
    for z in range(0, numberOfLists):

        # copies the list being observed to avoid tampering with the original list
        listSorted = list()
        for a in range(0,len(lists[z])):
            listSorted.append(lists[z][a])
        listSorted.sort()

        # perform searches for an element that does not exist in any list, -1, since lists only contain positive integers
        ssTuple = sequential_search(lists[z], -1)
        ossTuple = ordered_sequential_search(listSorted, -1)
        bsiTuple = binary_search_iterative(listSorted, -1)
        bsrTuple = binary_search_recursive(listSorted, -1)

        #add run times to a new list
        calcSSAvg.append(ssTuple[1]) # runtimes were return in the second element [1]
        calcOSSAvg.append(ossTuple[1])
        calcBSIAvg.append(bsiTuple[1])
        calcBSRAvg.append(bsrTuple[1])

    # calculate average runtimes based on runtimes for individual lists among a sample size of 100
    SSAvg = sum(calcSSAvg)/len(calcSSAvg)
    OSSAvg = sum(calcOSSAvg)/len(calcOSSAvg)
    BSIAvg = sum(calcBSIAvg)/len(calcBSIAvg)
    BSRAvg = sum(calcBSRAvg)/len(calcBSRAvg)


    # print out average results
    print "COMPARING THE SEARCHES OF LISTS OF SIZE %i" % len(lists[0])
    print "Sequential Search took%10.7f seconds to run, on average" % SSAvg
    print "Ordered Sequential Search took%10.7f seconds to run, on average" % OSSAvg
    print "Iterative Binary Search Search took%10.7f seconds to run, on average" % BSIAvg
    print "Recursive Binary Search took%10.7f seconds to run, on average" % BSRAvg
    print "\n"


def main():
    numberOfLists = 100

    # making and populating lists with random positive integers
    list500 = makeLists(500, numberOfLists)
    list1000 = makeLists(1000, numberOfLists)
    list10000 = makeLists(10000, numberOfLists)

    # search helper function
    doAllSearches(list500)
    doAllSearches(list1000)
    doAllSearches(list10000)


main()
