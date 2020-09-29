def solution(n):

    n = int(n)
    counter = 0

    while n > 1:

        n = int(n)

        if n == 1: return counter

        counter = counter +1

        #if the last bit is 0, then divide
        if bin(n)[len(bin(n))-1:] == "0":
            n = n/2
        elif bin(n)[len(bin(n))-2:] == "01" or n == 3:
            n = n-1
        else:
            n = n+1

    return counter

print(solution("9"+("0"*200)))