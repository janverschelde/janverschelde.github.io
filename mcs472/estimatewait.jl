# L-3 MCS 472 Fri 16 Jan 2026 : estimatewait.jl

using Statistics
using StatsKit

using Printf
Base.show(io::IO, f::Float64) = @printf(io, "%.2f", f)

"""
    process_requests(arrivals::Vector{Float64}, jobs::Vector{Int},
                     speed::Float64, verbose::Bool=true)

returns the waiting times for the jobs with given arrival times
and sizes.  If verbose, then the algorithm will print the simulation.
"""
function process_requests(arrivals::Vector{Float64}, jobs::Vector{Int},
                          speed::Float64, verbose::Bool=true)
   wait = [0.0 for i=1:length(arrivals)]
   busy = jobs[1]*speed
   for i=2:length(arrivals)
       elapsed = arrivals[i] - arrivals[i-1]
       if elapsed >= busy
           busy = 0
       else
           busy = busy - elapsed
       end
       wait[i] = busy
       busy = busy + jobs[i]*speed
   end
   return wait
end

"""
    simulate(lambda::Int, maxsizejob::Int, speed::Float64, N::Int,
             verbose::Bool=true)

returns the average waiting time and its standard deviation,
given the lambda parameter in the Poisson distribution,
the maximum size of a job, the speed of the processor,
and the number N of time steps.
"""
function simulate(lambda::Int, maxsizejob::Int, speed::Float64,
                  N::Int, verbose::Bool=true)
    p = Poisson(lambda)
    arrivalslist = []
    jobslist = []
    elapsed = 0.0
    for i=1:N
        nbr = rand(p, 1)[1]
        if verbose
            println("at step ", i, " : ", nbr, " jobs")
        end
        dt = 1.0/nbr
        for j=1:nbr
            push!(arrivalslist, elapsed)
            size = rand(1:maxsizejob, 1)
            push!(jobslist, size[1])
            elapsed = elapsed + dt
        end
    end
    if verbose
        println("total number of arrivals : ", length(arrivalslist))
        println("total number of jobs : ", length(jobslist))
    end
    arrivals = Vector{Float64}(arrivalslist)
    jobs = Vector{Int}(jobslist)
    if verbose
        println("The arrivals : ", arrivals)
        println("The jobs : ", jobs)
    end
    w = process_requests(arrivals, jobs, speed, verbose)
    if verbose
        println("The wait times : ", w)
    end
    return mean(w), std(w)
end

mu, sigma = simulate(10, 7, 0.02, 1000, false)
println("Lambda : 10, max#items : 7, speed : 0.02.");
println("Simulation with 1000 trials :")
println(" the average wait time : ", mu)
println("the standard deviation : ", sigma)
