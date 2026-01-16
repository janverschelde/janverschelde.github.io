# L-3 MCS 472 Fri 16 Jan 2026 : meantbfail.jl

"""
    mtbf(means::Vector{Float64}, deviations::Vector{Float64}, N::Int,
         verbose::Bool=false)

returns the expected lifespan and the standard deviation 
of a multicomponent product, given the means and standard deviations
of its components in the two vectors on input,
using N trials in the simulation.
If verbose, then each sample is written.
"""
function mtbf(means::Vector{Float64}, deviations::Vector{Float64}, N::Int,
             verbose::Bool=false)
   (m1, m2) = (0, 0)                       # first and second moment
   sample = [0.0 for j=1:length(means)]    # work space for each sample
   for i=1:N                               # run N simulations
       for j=1:length(means)               # randn() has mean 0, sigma 1
           sample[j] = means[j] + deviations[j]*randn()
       end
       if verbose                          # for debugging purposes ...
           println("sample : ", sample)
       end
       lifespan = minimum(sample)
       m1 = m1 + lifespan/N                # update the average
       m2 = m2 + lifespan*lifespan/N       # update second moment
   end
   return (m1, sqrt(m2 - m1*m1))           # mean and deviation
end

# We have three components:
# (1) The means are 11, 12, and 13.
# (2) The standard deviations are 1, 2, and 3.
# Let us take 10,000 samples in a simulation.

(mu, sigma) = mtbf([11.0, 12.0, 13.0], [1.0, 2.0, 3.0], 10000)
println("expected life span : ", mu)
println("standard deviation : ", sigma)
