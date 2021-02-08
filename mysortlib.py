#!/bin/python3
# This file contains my implementation of a sorting library

# first is selection sort, input is a list
def selection_sort(inList):
    r_list = list() 
    for i in range(len(inList)):
        r_list.append(min(inList))
        inList.remove(r_list[i])
    return r_list

def insertion_sort(inList):
    r_list=list()
    # insert first item into r_list
    r_list.append(inList[0])
    inList.pop(0)
    for item in inList:
        i = 0
        while i < len(r_list) and item > r_list[i]:
            i+=1
        r_list.insert(i, item)
    return r_list
# In place insertion sort
def insertion_sort_ip(inList):
    # first item to compare
    work_idx = 1
    while work_idx < len(inList):
        temp = inList[work_idx]
        comp_idx = work_idx-1
        while comp_idx >= 0 and temp < inList[comp_idx]:
            comp_idx-=1
        # shift everything right from comp_idx to tempIdx
        shift_idx = work_idx
        while shift_idx > comp_idx+1:
            inList[shift_idx] = inList[shift_idx-1]
            shift_idx-=1
        # This should be the insertion spot
        inList[shift_idx] = temp
        work_idx+=1


# Merge in place sort
def merge_sort(inList):
    return merge_helper(inList, 0, len(inList)-1)


    
def merge_helper(inList, start, end):
    # Base case, nothing left to split
    if start < end:
        middle = start + (end - start)//2
        # sort LHS
        merge_helper(inList, start, middle)
        # sort RHS
        merge_helper(inList, middle+1, end)        
        # merge sorted lists
        merge(inList, start, middle, end)
        

# In place merge
def merge(inList, start, middle, end):
    start2 = middle+1
    # check to see if already sorted
    if inList[middle] <= inList[start2]:
        return
    while start <= middle and start2 <= end:
        temp_val = inList[start2]
        if temp_val < inList[start]:
            #shift all values from start to start2
            index = start2
            while index != start:
                inList[index] = inList[index-1]
                index-=1
            inList[start] = temp_val
            start2+=1
            start+=1
            middle+=1
        else:
            start+=1
        


# swap values at two indices
def swap(inList, idx1, idx2):
    temp = inList[idx1]
    inList[idx1] = inList[idx2]
    inList[idx2] = temp
    return inList

# Bubble sort
def bubble_sort(inList):
    sorted_idx = len(inList) - 1
    while sorted_idx >= 0:
        swap_idx=0
        while swap_idx < sorted_idx:
            if inList[swap_idx] > inList[swap_idx+1]:
                swap(inList, swap_idx, swap_idx+1)
            swap_idx+=1
        sorted_idx-=1
    return inList





