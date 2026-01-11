# L-1 MCS 472 Mon 12 Jan 2026 : arrival.jl

"""
    A market has 60 customers per hour on average.

What is the probability that more than 20 customers
check out in one quarter hour?
"""
function arrival()
    q = 0           # sum of probabilities
    m = 20          # number of arrivals
    lT = 15         # arrivals per quarter hour is lambda*T
    p = 1           # accumulates the product
    for k=1:m
        p = p*lT/k  # update the product
        q = q + p   # update the sum
    end
    q = q*exp(-lT)  # normalization 
    p = 1 - q
    println("probability : ", p)
end

arrival()
