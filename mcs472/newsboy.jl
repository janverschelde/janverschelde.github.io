# L-3 MCS 472 Fri 16 Jan 2026 : newsboy.jl

using Printf
Base.show(io::IO, f::Float64) = @printf(io, "%.2f", f)

"""
A newspaper seller has on average 100 customers a day
as 5000 people are passing by the shop each day.

The seller has to buy each paper at 50 cents a copy,
sells it at 75 cents, with no returns. 
For each sold paper, the seller makes a profit of 25 cents,
the loss is 75 cents for each unsold paper.

To maximize profit, how many copies should the seller buy?
"""
function newsboy()
    (maxprofit, maxidx) = (0, 0)
    for nbpapers = 90:110
        sumday = 0
        for day=1:365
            profit = -nbpapers*0.50
            nbsold = 0
            for passerby=1:5000
                if nbsold < nbpapers
                    if rand() <= 1.0/50
                        profit = profit + 0.75
                        nbsold = nbsold + 1
                    end
                end
            end
            sumday = sumday + profit
        end
        avgday = sumday/365
        println("profit from ", nbpapers, " : \$", avgday)
        if maxprofit < avgday
            maxprofit = avgday
            maxidx = nbpapers
        end
    end
    print(" maximum profit : \$", maxprofit)
    println(" at ", maxidx)
end

newsboy()
