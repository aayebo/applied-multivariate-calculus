E=dblquad(lambda yy,xx:2+.5*xx+yy**2,0,3,0,2)[0]
M=quad(lambda xx:1+xx,0,2)[0]
Mx=quad(lambda xx:xx*(1+xx),0,2)[0]
print('exposure',E,'average',E/6)
print('mass',M,'centroid',(Mx/M,.5))
