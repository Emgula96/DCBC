array = [5,1,22,25,6,-1,8,10]
seq = [1,6,-1,10]

def funk(arr, sub):

    ### FIRST VERSION
    # for i in sub:
    #     if i in arr:
    #         continue
    #     else:
    #         return False
    # return True

    ### SECOND VERSION
    results = []
    for i in range(len(sub)):
        print(sub[i])
        for j in range(len(arr)):
            if sub[i] == arr[j]:
                results.append(True)
            else:
                continue
    if len(results) == len(sub):
        return True
    else:
        return False


print(funk(array,seq))