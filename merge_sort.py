def merge(l1, l2):
    final = []

    i = 0
    j = 0

    while len(final) < (len(l1) + len(l2)):

        if (i) == len(l1):
            final.extend(l2[j:])
            break
        elif (j) == len(l2):
            final.extend(l1[i:])
            break

        if l1[i] < l2[j]:
            final.append(l1[i])
            i += 1
        elif l2[j] < l1[i]:
            final.append(l2[j])
            j += 1
        else:
            final.append(l1[i])
            final.append(l2[j])
            i += 1
            j += 1

    return final


l1 = [4,8,9,10,30]
l2 = [-2,-1,3,4,7,9,20,40]

print(merge(l1, l2))