def vedic_cross_multiplication(a, b):
    def accept_numbers(a, b):
        sa = str(a)
        sb = str(b)
        lsa = len(sa)
        lsb = len(sb)
        while lsa > lsb:
            sb = "0" + sb
            lsb = len(sb)
        while lsb > lsa:
            sa = "0" + sa
            lsa = len(sa)
        return sa, sb
    def process_numbers(sa, sb):
        ls = len(sa)
        s = [[],
             []]
        unfinished_answer = []
        for i in range(ls):
            s[0] += sa[i]
            s[1] += sb[i]
            sum1 = 0
            up = 0
            down = len(s[1]) - 1
            for a in range(len(s[0])):
                sum1 += int(s[0][up]) * int(s[1][down])
                up += 1
                down -= 1
            unfinished_answer.append(sum1)

        for i in range(ls - 1):
            s[0].pop(0)
            s[1].pop(0)
            sum1 = 0
            up = 0
            down = len(s[1]) - 1
            for a in range(len(s[0])):
                sum1 += int(s[0][up]) * int(s[1][down])
                up += 1
                down -= 1
            unfinished_answer.append(sum1)
        return unfinished_answer
    def finish(ans):
        ans2 = []
        pos = 0
        power = len(ans) - 1
        for n in range(len(ans)):
            ans2.append(ans[pos]*(10**power))
            power -= 1
            pos += 1
        return sum(ans2)
    stringA, stringB = accept_numbers(a, b)
    answer1 = process_numbers(stringA, stringB)
    return finish(answer1)
