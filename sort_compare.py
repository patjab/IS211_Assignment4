import time, sys, random

# function was copied from Chapter 5 of Problem Solving with Algorithms and Data Structures by Miller and Ranum
def insertion_sort(a_list):
    start = time.time()     # modified capture start time to determine length of time of function operating
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value

    end = time.time() # modified function: capture end time to determine length of time of function operating
    return a_list, end-start # modified function: returned difference to report length of time of function operating
#returns sorted list

# function was copied from Chapter 5 of Problem Solving with Algorithms and Data Structures by Miller and Ranum
def shell_sort(a_list):
    start = time.time() # modified capture start time to determine length of time of function operating
    sublist_count = len(a_list) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2

    end = time.time() # modified function: capture end time to determine length of time of function operating
    return a_list, end-start # modified function: returned difference to report length of time of function operating
#returns sorted list

# function was copied from Chapter 5 of Problem Solving with Algorithms and Data Structures by Miller and Ranum
# helper function of the shell sort
def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value


def python_sort(a_list):
    start = time.time() # modified capture start time to determine length of time of function operating
    a_list.sort()
    end = time.time() # modified function: capture end time to determine length of time of function operating

    return a_list, end-start # modified function: returned difference to report length of time of function operating
#returns sorted list

# makes the lists required for searches and stores them within a bigger list; size dictates how many elements in the smaller lists; amount dictates number of lists in the bigger list
def makeLists(size, amount):

    allRandList = list() # this list will contain the 100 lists required within itself to later calculate an average between the results of all the lists

    for y in range(0, amount):
        randList = list() # list of random integer values

        for x in range(0, size):
            randList.append(random.randint(0, sys.maxint)) # places an integer from 0 to the maximum integer by the system

        allRandList.append(randList)

    return allRandList # returns the list that contains the lists of random positive integers

# will perform insertion, shell, and python's built-in sort on a specified list of lists
# calculates averages of run times on all the lists
def doAllSorts(lists):

    numberOfLists = len(lists)

    # will store run times for the sorting in this list for each list within the bigger list
    calcInsertionSortAvg = list()
    calcShellSortAvg = list()
    calcPythonSortAvg = list()

    # one iteration represents one list
    for z in range(0, numberOfLists):

    # copies the list being observed to avoid tampering with the original list
        listSortedByInsertion = list()
        for a in range(0,len(lists[z])):
            listSortedByInsertion.append(lists[z][a])

        listSortedByShell = list()
        for a in range(0,len(lists[z])):
            listSortedByShell.append(lists[z][a])

        listSortedByPython = list()
        for a in range(0,len(lists[z])):
            listSortedByPython.append(lists[z][a])

        # sort using three different sorts
        insertionSortTuple = insertion_sort(listSortedByInsertion)
        shellSortTuple = shell_sort(listSortedByShell)
        pythonSortTuple = python_sort(listSortedByPython)

        #add run times to a new list
        calcInsertionSortAvg.append(insertionSortTuple[1]) # runtimes were return in the second element [1]
        calcShellSortAvg.append(shellSortTuple[1])
        calcPythonSortAvg.append(pythonSortTuple[1])

    # calculate average runtimes based on runtimes for individual lists among a sample size of 100
    insertionSortAvg = sum(calcInsertionSortAvg)/len(calcInsertionSortAvg)
    shellSortAvg = sum(calcShellSortAvg)/len(calcShellSortAvg)
    pythonSortAvg = sum(calcPythonSortAvg)/len(calcPythonSortAvg)

    # calculate average runtimes based on runtimes for individual lists among a sample size of 100
    print "COMPARING THE SORTS OF LISTS OF SIZE %i" % len(lists[0])
    print "Insertion Sort took%10.7f seconds to run, on average" % insertionSortAvg
    print "Shell Sort took%10.7f seconds to run, on average" % shellSortAvg
    print "Python Sort took%10.7f seconds to run, on average" % pythonSortAvg
    print "\n"


def main():
    numberOfLists = 100

    # making and populating lists with random positive integers
    list500 = makeLists(500, numberOfLists)
    list1000 = makeLists(1000, numberOfLists)
    list10000 = makeLists(10000, numberOfLists)

    # sorting helper function
    doAllSorts(list500)
    doAllSorts(list1000)
    doAllSorts(list10000)


main()
