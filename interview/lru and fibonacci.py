fibonacci

1, 1, 2, 3, 5, 8, 13, ...


def fibonacci(n):
    a = 1
    b = 1
    final_val = a

    count = 1

    # n = 4
    # f = 3
    # a = 5
    # b = 3
    # f = 5
    # count = 4
    while count < n:
        a = a + b
        b = final_val
        final_val = a
        count += 1
    return final_val

# LRU Cache
# max number of elements
# least recently used gets booted out when max elements gets hit
# least recently used = read, write(update / insert)

# {a: 1, b: 2, c: 3}
# [a, b, c]

# [d, c, a]
    del dict[b]
    dict[d] = v
    {a: 1, b: 2, c: 3}

#get(K, V)


def get(K, V):
    val = dic.get(K, Null)  # O(1)
    if (val):
                   # update LRU item in the list
                       # move the list by 1 (circular list)
        # [6,1,2,3,4,5] O(n)

        put(K, V)
        # see if it exist O(1)
        # update LRU item in the list
        # move the list by 1 (circular list)
        # [6,1,2,3,4,5] O(n)

        # else
        # if the size of the dict is at its max O(1f)
            a = lru_q.pop() O(1)
            # add to the LRU in both list & dic
                dict[k] = V   O(1)
                    lru_q.append(K)  O(1)

                    # else
                        dict[k] = V O(1)
                            lru_q.append(K) O(1)

                                K put(V)

                                    1 < n, but how?
                                    log(n) < n - -> bst
