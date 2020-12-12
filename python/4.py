from array import *

                                                                    # 1
                                                                    # 22
                                                                    # 333
                                                                    # 4444
                                                                    # 55555
# for i in range(1,6):
#     for j in range(1,6):
#         if j<=i:
#             print(i,end="")
#     print("")

                                                                    # 0
                                                                    # 12
                                                                    # 345
                                                                    # 6789
                                                                    # 01234
# k=0
# for i in range(1,6):
#     for j in range(1,6):
#         if j<=i:
#             print(k,end="")
#             if k==9:
#                 k=0
#             else:
#                 k+=1
#     print("")

                                                                    # A
                                                                    # AB
                                                                    # ABC
                                                                    # ABCD
                                                                    # ABCDE
# arr=array('u',['A','B','C','D','E'])
# for i in range(1,6):
#     for j in range(1,6):
#         if j<=i:
#             print(arr[j-1],end="")
#     print("")

                                                                    # *
                                                                    # ***
                                                                    # *****
                                                                    # *******
                                                                    # *********
# for i in range(1,11,2):
#     for j in range(1,11):
#         if j<=i:
#             print("*",end="")
#     print("")

                                                                    # 1
                                                                    # 123
                                                                    # 12345
                                                                    # 1234567
                                                                    # 123456789
# for i in range(1,10,2):
#     for j in range(1,10):
#         if j<=i:
#             print(j,end="")
#     print("")

                                                                    #     *
                                                                    #    ***
                                                                    #   *****
                                                                    #  *******
                                                                    # *********
# k=5
# for i in range(1,10,2):
#     for j in range(1,k):
#         print(" ",end="")
#     for l in range(1,i+1):
#         print("*",end="")
#     k-=1
#     print("")

                                                                    #     1
                                                                    #    123
                                                                    #   12345
                                                                    #  1234567
                                                                    # 123456789
# k=5
# for i in range(1,10,2):
#     for j in range(1,k):
#         print(" ",end="")
#     for l in range(1,i+1):
#         print(l,end="")
#     k-=1
#     print("")

                                                                    # 1
                                                                    # 12
                                                                    # 123
                                                                    # 1234
                                                                    # 12345
# for i in range(1,6):
#     for j in range(1,6):
#         if j<=i:
#             print(j,end="")
#     print(end="\n")

                                                                    # 0
                                                                    # 10
                                                                    # 101
                                                                    # 0101
                                                                    # 01010
# k=0
# for i in range(1,6):
#     for j in range(1,6):
#         if j<=i:
#             print(k,end="")
#             if k==0:
#                 k=1
#             else:
#                 k=0
#     print(end="\n")

                                                                    # 9
                                                                    # 87
                                                                    # 654
                                                                    # 3210
                                                                    # 98765
# k=9
# for i in range(1,6):
#     for j in range(1,6):
#         if j<=i:
#             print(k,end="")
#             if k==0:
#                 k=9
#             else:
#                 k-=1
#     print(end="\n")

                                                                    # I
                                                                    # IN
                                                                    # IND
                                                                    # INDI
                                                                    # INDIA
# a="INDIA"
# for i in range(5):
#     for j in range(5):
#         if j<=i:
#             print(a[j],end="")
#     print("")

                                                                    # 1
                                                                    # 121
                                                                    # 12321
                                                                    # 1234321
                                                                    # 123454321
# for i in range(0,10,2):
#     n=1
#     for j in range(0,i+1):
#         print(n, end="")
#         if j>=i/2:
#             n-=1
#         else:
#             n+=1
#     print(end="\n")

                                                                    # 1
                                                                    # 222
                                                                    # 33333
                                                                    # 4444444
                                                                    # 555555555
# for i in range(1,11,2):
#     for j in range(1,i+1):
#         print((i+1)//2, end="")
#     print(end="\n")

                                                                    #     1
                                                                    #    121
                                                                    #   12321
                                                                    #  1234321
                                                                    # 123454321
# l=4
# for i in range(0,10,2):
#     n=1
#     for k in range(l):
#         print(" ",end="")
#     for j in range(0,i+1):
#         print(n, end="")
#         if j>=i/2:
#             n-=1
#         else:
#             n+=1
#     l-=1
#     print("")

                                                                    #     1
                                                                    #    222
                                                                    #   33333
                                                                    #  4444444
                                                                    # 555555555
# l=4
# for i in range(1,11,2):
#     for k in range(l):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print((i+1)//2, end="")
#     l-=1
#     print(end="\n")


