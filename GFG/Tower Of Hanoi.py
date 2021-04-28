class Solution:
    def toh(self, N, fromm, to, aux):
        # Your code here
        ans = 0
        def innertower(ans, N, fromm, to, aux):
            if N == 1:
                print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
                ans += 1
                return ans
            else:
                x = innertower(ans, N-1, fromm, aux, to)
                print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to) )
                y = innertower(ans, N-1, aux, to, fromm)
                ans = x + y + 1
            return ans
        return innertower(ans, N, fromm, to, aux)