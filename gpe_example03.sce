function z = phi1(y)
    z = y * exp(-1*((1+y^2)/2))
endfunction

function z = phi2(x)
    z = x * exp(-1*((1+x^2)/2))
endfunction

function y = phi3(y)
    z = 2 * y * exp(-1*((4+y^2)/2))
endfunction

function z = phi4(x)
    z = 2 * x * exp(-1*((4+x^2)/2))
endfunction

function z = A(x, y)
    z = y * exp(((x^2+y^2)/2))
endfunction

function z = C(x, y)
    z = x * exp(((x^2+y^2)/2))
endfunction
