# HEAPSORT
# first = p
# s = p
# d = 1
# while s.next != None:
#     s = s.next
#     d += 1
# def przepiecia(a, b):
#     nonlocal first
#     if a > b:
#         b, a = a, b
#     if a == 0:
#         qa = first
#         if b == 1:
#             qb = qa.next
#             qa.next, qb.next = qb.next, qa
#             first = qb
#         else:
#             qb = qa
#             for _ in range(b-1):
#                 qb = qb.next
#             prevb = qb
#             qb = qb.next
#             qb.next, prevb.next, qa.next = qa.next, qa, qb.next
#             first = qb
#     else:
#         qa = first
#         for _ in range(a-1):
#             qa = qa.next
#         if b == a+1:
#             prewa = qa
#             qa = qa.next
#             qb = qa.next
#             prewa.next, qb.next, qa.next = qb, qa, qb.next
#         else:
#             prewa = qa
#             qa = qa.next
#             prewb = prewa
#             for _ in range(b-a):
#                 prewb = prewb.next
#             qb = prewb.next
#             prewa.next, qb.next, prewb.next, qa.next = qb, qa.next, qa, qb.next
#
# def wart(a):
#     nonlocal first
#     z = first
#     for _ in range(a):
#         z = z.next
#     return z.val
# def heapify(n, i):
#     max_ind = i
#     l = 2*i+1
#     r = 2*i+2
#     if l < n and wart(l) > wart(max_ind):
#         max_ind = l
#     if r < n and wart(r) > wart(max_ind):
#         max_ind = r
#     if max_ind != i:
#         przepiecia(i, max_ind)
#         heapify(n, max_ind)
# def heap_sort():
#     nonlocal d
#     n = d
#     for i in range(n, -1, -1):
#         heapify(n, i)
#     for i in range(n-1, 0, -1):
#         przepiecia(0, i)
#         heapify(i, 0)
# heap_sort()
#
# return first
# Heap Sort - z tablicą
# def przepiecia(a, b):
#     nonlocal first
#     if a > b:
#         b, a = a, b
#     qa = first
#     for _ in range(a-1):
#         qa = qa.next
#     if b == a+1:
#         prewa = qa
#         qa = qa.next
#         qb = qa.next
#         prewa.next, qb.next, qa.next = qb, qa, qb.next
#     else:
#         prewa = qa
#         qa = qa.next
#         prewb = prewa
#         for _ in range(b-a):
#             prewb = prewb.next
#         qb = prewb.next
#         prewa.next, qb.next, prewb.next, qa.next = qb, qa.next, qa, qb.next


# def przepnij_node_o_val(val, link):
#     pomocnik = link
#     while True:
#         if pomocnik.next == None:
#             return
#         if pomocnik.next.val == val:
#             link.next, pomocnik.next.next, pomocnik.next = pomocnik.next, link.next, pomocnik.next.next
#             return
#         pomocnik = pomocnik.next
#
#
# def heapify(i, n):
#     nonlocal tab
#     while True:
#         min_ind = i
#         l = 2*i+1
#         r = 2*i+2
#         if l < n and tab[min_ind] < tab[min_ind]:
#             min_ind = l
#         if r < n and tab[r] < tab[min_ind]:
#             min_ind = r
#         if min_ind == i:
#             break
#         tab[i], tab[min_ind] = tab[min_ind], tab[i]
#         i = min_ind
# if k!=1:
#     head = p
#     s = p
#     d = 1
#     while s.next != None:
#         s = s.next
#         d += 1
#     if k >= d:
#         k = d-1
#     tab = [None for _ in range(k+1)]
#     for i in range(k+1):
#         tab[i] = p.val
#         p = p.next
#     for i in range(k//2, -1, -1):
#         heapify(i, k+1)
#     p, q = head, p
#     for i in range(d-k-1):
#         p.val, tab[0] = tab[0], q.val
#         heapify(0, k+1)
#         p, q = p.next, q.next
#     for i in range(k, 0, -1):
#         p.val, tab[0] = tab[0], tab[i]
#         heapify(0, i)
#         p = p.next
#     p.val = tab[0]
#     return head