# while calculating all time complexities, 
# time taken to perform operations +,-,*,/,// and time taken to append = O(1) is assumed

import math
pi = math.pi

def taylor_sin(x,n):
    # initialisation
    i = 1 # we begin with index i == 1 
    i_term = x # first term is x
    sum = i_term # sum of the first i terms
    # — ASSERT i_term contains xi / (2*i-1)!
    # — ASSERT sum contains sum of first i terms
    # Can iteratively compute next term and summand
    while i <= n: # TERMINATION: n-i decreases
        # — INVARIANT i_term == x^i / (2*i-1)!
        # — INVARIANT sum == sum of first i terms
        # the i+1th term is ith term times(-1)(i+1) * x2/(2*i*(2i+1))
        i_term *= x*x / ((2*i)*(2*i+1)) # compute next term
        if (i % 2) == 1:
            sum -= i_term # subtract if previous i is odd
        else:
            sum += i_term # add if previous i is even
        i += 1 # increment i
    # — CHECK INVARIANT i_term == x^i / (2*i-1)!
    # — CHECK INVARIANT sum == sum of first i terms
    return sum

def fact(n):
    ans=1
    for i in range (1,n+1):
        ans = ans*i  
    return ans # T = O(n) as n iterations

#---------------------------------------------------------------------------------

def expn(x,n):
    # Initialisation 
    i = 1
    i_term = 1
    sum = i_term

    # Assert i_term contains x^(i-1)/(i-1)!
    # Assert sum contains first i terms
    # We can iteratively compute the next terms and the sum 

    while i < n : 
        # TERMINATION (n-i) decreases
        # INVARIANT i_term = x^(i-1)/(i-1)!
        # INVARIANT sum = sum of first i terms

        i_term *= (x)/(i)
        i += 1
        sum += i_term   
        # print('adding ', i_term, 'to sum')                                 

        # CHECK INVARIANT i_term = x^(i-1)/(i-1)!
        # CHECK INVARIANT sum = sum of first i terms
        # EXIT condition = i>n i.e. i=n+1
        # T = O(n) as n iterations run within the loop, all other processes like
        # adding multiplying initialising are taken to have T = O(1)
    return sum
print(expn(2,0))

def cosine(x,n):
    # Initialisation 
    i = 1
    i_term = 1
    sum = i_term

    # Assert i_term contains [(-1)^(i-1)]*[(x)^(2i-2)] // (2i-2)!
    # Assert sum contains first i terms
    # We can iteratively compute the next terms and the sum 

    while i < n : 
        # TERMINATION (n-i) decreases
        # INVARIANT i_term = [(-1)^(i-1)]*[(x)^(2i-2)] / (2i-2)!
        # INVARIANT sum = sum of first i terms

        i_term *= (x*x)/((2*i)*(2*i-1))
        i += 1

        if i%2 == 0:
            sum -= i_term
            # print('subtracting', i_term, 'from sum')

        else: # i%2 = 1
            sum += i_term
            # print('adding', i_term, 'to sum')

        # CHECK INVARIANT i_term [(-1)^(i-1)]*[(x)^(2i-2)] // (2i-2)!
        # CHECK INVARIANT sum = sum of first i terms
        # EXIT condition = i>n i.e. i=n+1
        # T = O(n) as n iterations run within the loop, all other processes like
        # adding multiplying initialising are taken to have T = O(1)

    return sum

def inverse(x,n):
    # Initialisation 
    i = 1
    i_term = 1
    sum = i_term

    # Assert i_term contains x^(i-1)
    # Assert sum contains first i terms
    # We can iteratively compute the next terms and the sum 

    while i < n : 
        # TERMINATION (n-i) decreases
        # INVARIANT i_term = x^(i-1)
        # INVARIANT sum = sum of first i terms

        i_term *= x
        i += 1
        sum += i_term
        # print('adding', i_term, 'to sum')

        # CHECK INVARIANT i_term x^(i-1)
        # CHECK INVARIANT sum = sum of first i terms
        # EXIT condition = i>n i.e. i=n+1
        # T = O(n) as n iterations run within the loop, all other processes like
        # adding multiplying initialising are taken to have T = O(1)

    return sum

def natural_log(x,n):
    # Initialisation 
    i = 1
    i_term = x
    sum = i_term

    # Assert i_term contains 
    # Assert sum contains first i terms
    # We can iteratively compute the next terms and the sum 
    while  i < n : 
        # TERMINATION (n-i) decreases
        # INVARIANT i_term = ([(-1)^(i-1)]*x)/ i
        # INVARIANT sum = sum of first i terms

        i_term *= ((x)*(i))/(i+1)
        i += 1

        if i%2 == 0:
            sum -= i_term
            # print('subtracting', i_term, 'from sum')

        else: # i%2 = 1
            sum += i_term
            # print('adding', i_term, 'to sum')

        # CHECK INVARIANT i_term ([(-1)^(i-1)]*x)/ i
        # CHECK INVARIANT sum = sum of first i terms
        # EXIT condition = i>n i.e. i=n+1
        # T = O(n) as n iterations run within the loop, all other processes like
        # adding multiplying initialising are taken to have T = O(1)

    return sum

def tan_inv(x,n):
    # Initialisation 
    i = 1
    i_term = x
    sum = i_term

    # Assert i_term contains 
    # Assert sum contains first i terms
    # We can iteratively compute the next terms and the sum 
    while  i < n : 
        # TERMINATION (n-i) decreases
        # INVARIANT i_term = ([(-1)^(i-1)]*x)/ (2i+1)
        # INVARIANT sum = sum of first i terms

        i_term *= (x*x)*(2*i-1)/(2*i+1)
        i += 1

        if i%2 == 0:
            sum -= i_term
            # print('subtracting', i_term, 'from sum')

        else: # i%2 = 1
            sum += i_term
            # print('adding', i_term, 'to sum')

        # CHECK INVARIANT i_term ([(-1)^(i-1)]*x)/ i
        # CHECK INVARIANT sum = sum of first i terms
        # EXIT condition = i>n i.e. i=n+1
        # T = O(n) as n iterations run within the loop, all other processes like
        # adding multiplying initialising are taken to have T = O(1)

    return sum

#---------------------------------------------------------------------------------

def bisect(a,b,eps):
    # 2021EE30741 -> 0741 % 4 = 1 
    # INPUT f(x) = e^(-x) - sin(x) 
    # INPUT f: float -> float 
    # INPUT a < b
    # INPUT f(a)≤0.0 & f(b)≥0.0 which implies f(a).f(b) < 0
    # INPUT ASSUMPTION f has one root in interval [a, b].
    # INPUT eps > 0.0 and eps ~ 0.0 — tolerance on output
    # OUTPUT (found, mid) s.t. found == True implies |f(mid)| ≤ eps

    #Initialisation
    approx = []
    # approx will be the documentation of the iterations in the loop 
    # when the ans converges within the tolerance limit
    mid = a 
    # to avoid an error in the return statement
    found = False 
    # found == False can imply anything so mid == a is ok

    # INVARIANT: f(a)≤0.0 & f(b)≥0.0 & 
    #            found == True implies |f(mid)| ≤ eps
    #            and f has one root in interval [a, b]
    # INVARIANT: first i approximations as we move towards the result

    while (a < b) and (not found): 
        # (b - a) decreases
        mid = (a + b)/2 
        # bisect the interval

        val = math.exp(-mid) - math.sin(mid)
        if abs(val) <= eps:
            found = True 
            # found == True implies |f(mid)| ≤ eps
        elif val < 0: 
            a = mid 
            # move a boundary of interval
        else:
            b = mid 
            # move b boundary of interval
        approx.append(mid)

    # CHECK invariant is maintained
    # LOOP EXIT: Either (found == True) or (a ≥ b)
    # T = O(log(n)) as the search space is getting halved. The size of these 
    # intervals eventually comes within tolerance range 'tol'. 
    # if x is the true answer, a & b are search spaces and tol is the deviation from
    # x then (x - tol) <= (b-a)/2^k <= (x + tol) where k is the no. of iterations in loop.
    # adding multiplying initialising are taken to have T = O(1)

    return (found,mid,approx)

#---------------------------------------------------------------------------------

def expn_coeff(n):
    return 1/(fact(n)) # T = O(n) as fact(n) runs n iterations within the loop

def cosine_coeff(n): 
    if n%2==1:
        # there are no odd order terms in cosine expansion 
        return 0
    else: 
        # for even order terms, the expansion is an alternating series
        if n%4==0:
            return 1/fact(n) # T = O(n) as fact(n) runs n iterations within the loop
        else:
            return -1/fact(n) # T = O(n) as fact(n) runs n iterations within the loop

def inverse_coeff(n):
    return 1 # T = O(1) 

def natural_log_coeff(n):
    if n==0:
        return 0
    elif n%2==0:
        return -1/n # T = O(1)
    else:
        return 1/n # T = O(1)

def tan_inv_coeff(n):
    if n==0:
        return 0
    elif n%2==0:
        return 0 # no even power term
    elif (n+1)%4==0:
        return -1/n # T = O(1)
    else:
        return 1/n # T = O(1)

#---------------------------------------------------------------------------------

def expn_t(x,n):
    # to get sum till x^0, open till 1st term
    #        sum till x^1, open till 2nd term
    #        sum till x^n, open till (n+1)th term 
    return expn(x,n+1) # T = O(n) as expn runs n iterations within the loop

def cosine_t(x,n):
    # to get sum till x^0 (n=1), open till 1st term
    #        sum till x^1(n=2), open till 1st term (as x^odd terms dont exist)
    #        sum till x^2(n=3), open till 2nd term
    #        sum till x^3(n=4), open till 2nd term
    #        sum till x^4(n=5), open till 3rd term
    #        sum till x^n(n=n+1), open till ((n//2)+1)th term
    return cosine(x,n//2+1) # T = O(n) as cosine runs n iterations within the loop

def inverse_t(x,n):
    # same logic as expn_t
    return inverse(x,n+1) # T = O(n) as inverse runs n iterations within the loop

def natural_log_t(x,n):
    # similar logic as expn_t
    if n==0:
        return 0
    else:
        return natural_log(x,n) # T = O(n) as natural_log runs n iterations within the loop

def tan_inv_t(x,n):
    #similar logic as cosine_t
    return tan_inv(x,(n+1)//2) # T = O(n) as tan_inv runs n iterations within the loop

#---------------------------------------------------------------------------------
#2021EE30741 -> 1) e^-x and 1/(1-x)

def add_coeff(n):
    if n%2==0:
        return expn_coeff(n) + inverse_coeff(n) # T = O(n) as both expn_coeff and inverse_coeff run n iterations within their loops
    else: #n%2==1
        return -expn_coeff(n) + inverse_coeff(n) # T = O(n) as both expn_coeff and inverse_coeff run n iterations within their loops 

def expn_coeff_helper(n):
    # is a helper function for mul_coeff to write the (-x) expansion of the cofficient correctly w.r.t. power n
    if n%2==0:
        return 1/fact(n) # T = O(n) as fact(n) runs n iterations within the loop
    else:
        return -1/fact(n) # T = O(n) as fact(n) runs n iterations within the loop

def mul_coeff(n):
        # run a while loop that gives the coefficient which resembles the sum of the expansion e^-x upto the 'i'th term
        # Inititalisation
        i=0
        ans = expn_coeff_helper(i) # ans holds the value of the invariant

        while i<n:
            # TERMINATION = (n-i) decreases
            # Assert INVARIANT expn_coeff_helper(i) (this is the 1/i! term)

            ans += expn_coeff_helper(i+1)
            # we keep adding the next 1/(i+1)! term to the invariant in order to proceed to the next term inside the coeff
            i+=1

            # Check INVARIANT is maintained
            # EXIT condition is when i>n

         # T = O(n^2) as expn_coeff_helper has T = O(n) and mul_coeff also runs n iterations in the while loop

         # If f (n) is O(h(n)) and g(n) is O(k(n)), then
         # f(n) + g(n) is O(h(n) + k(n)),
         # f(n)g(n) is O(h(n)k(n))

         # # O(n)*O(n) = O(n^2) 
        return ans
 
def diff_coeff(n):
    if n%2==0:
        return -1/fact(n) # T = O(n) as fact(n) runs n iterations within the loop
    else:
        return 1/fact(n) # T = O(n) as fact(n) runs n iterations within the loop

#---------------------------------------------------------------------------------

def limit_diff(x,epsilon):
     # T of taylor_sin = O(n) (as n iterations run within its while loop)
     # T of expn = O(n) (as n iterations run within its while loop)

     # If f (n) is O(h(n)) and g(n) is O(k(n)), then
     # f(n) + g(n) is O(h(n) + k(n)),
     # f(n)g(n) is O(h(n)k(n))

     # THEN T of limit_diff = O(n*n) = O(n^2)

    return (expn(-x-epsilon,20)*taylor_sin(x+epsilon,20) - expn(-x,20)*taylor_sin(x,20))/epsilon

#---------------------------------------------------------------------------------
#==================================End============================================