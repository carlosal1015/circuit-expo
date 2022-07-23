#!/usr/bin/lua

function trunc(num, digits)
    local mult = 10 ^ (digits)
    return math.modf(num * mult) / mult
end

start = 0

function difference(increment)
    increment = start
    diff = increment - start
    return trunc(diff, 2)
end

--[[ Take the initial time --]]
-- io.read()
-- io.write("¡Inicio!")
-- tstart = os.time()

--[[ Take the final time --]]
-- io.read()
-- tend = os.time()
-- io.write("¡Fin!\n")

--[[ Print the differences of time --]]
-- delta_t = trunc(os.difftime(tend , tstart)/60, 2)
-- io.write("Duración: ", delta_t, " minuto(s).\n")
