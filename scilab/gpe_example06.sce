function z = phi1(y)
    z = (1-y*cos(y*(%pi / 2)))*(%pi)^y
endfunction

function z = phi2(x)
    z = %pi^x
endfunction

function z = phi3(y)
    z = %pi^(1-y)*exp(y)
endfunction

function z = phi4(x)
    z = %pi^(1-x)*exp(sin(x*%pi/2))
endfunction

function z = A(x, y)
    z = y * exp(((x^2+y^2)/2))
endfunction

function z = C(x, y)
    z = x * exp(((x^2+y^2)/2))
endfunction

function z = phiF(x, y)
    z = phi1(x) + phi2(y)
endfunction

function [] = plotF(alpha1, alpha2, beta1, beta2, m, n, f)
    h = (alpha2 - alpha1) / m
    k = (beta2 - beta1) / n
    //[X,Y]=meshgrid(alpha1:h:alpha2,beta1:k:beta2);
    X=alpha1:h:alpha2
    Y=beta1:k:beta2
    Z=feval(X,Y,f)
    mesh(Z)
endfunction


function [X, Y, phi1Y, phi2X, phi3Y, phi4X, Z] = boundcondsPlot(alpha1, alpha2, beta1, beta2, m, n)
    h = (alpha2 - alpha1) / m
    k = (beta2 - beta1) / n
    X=alpha1:h:alpha2
    Y=beta1:k:beta2
    phi1Y=feval(Y, phi1)
    phi2X=feval(X, phi2)
    phi3Y=feval(Y, phi3)
    phi4X=feval(X, phi4)
    Z=zeros(m+1, n+1)
    Z(1,1:1:n+1)=phi1Y
    Z(m+1,1:1:n+1)=phi3Y
    Z(1:1:m+1, 1)=phi2X'
    Z(1:1:m+1, n+1)=phi4X'
    mesh(Z)
endfunction
