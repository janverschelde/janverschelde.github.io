# L-5 MCS 472 Fri 23 Jan 2026 : sortdata.jl

# Simple program to illustrating sorting of data
# using a data frame.
# Requires the file tempChicago100years.txt to be present.

using DelimitedFiles
using DataFrames

A = readdlm("tempChicago100years.txt")
df = DataFrame()
df.year = A[2:end,1]
df.Dec = A[2:end,13]
sorted = sort(df, :Dec)
println("five coolest Decembers :")
println(sorted[1:5, :])
println("five warmest Decembers :")
println(sorted[96:100, :])

