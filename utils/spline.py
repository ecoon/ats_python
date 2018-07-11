"""Simple spline functor"""

class Spline(object):
    def __init__(self, x1,y1,dy1,x2,y2,dy2):
        self.x1 = x1
        self.y1 = y1
        self.dy1 = dy1

        self.x2 = x2
        self.y2 = y2
        self.dy2 = dy2

        assert x1 < x2
        if (y2 >= y1):
            assert dy1 >= 0.
            assert dy2 >= 0.

        if (y1 >= y2):
            assert dy1 <= 0.
            assert dy2 <= 0.

    def value(self, x):
        assert self.x1 <= x <= self.x2
        t = (x - self.x1) / (self.x2 - self.x1)

        return pow(1-t,2) * ((1+2*t) * self.y1 + t * (self.x2 - self.x1) * self.dy1) \
            + pow(t,2) * ((3-2*t) * self.y2 + (t-1) * (self.x2 - self.x1) * self.dy2);

    def derivative(self, x):
        assert self.x1 <= x <= self.x2
        t = (x - self.x1) / (self.x2 - self.x1)
        dtdx = 1./(self.x2 - self.x1)
        dydt = (6*pow(t,2) - 6*t)* self.y1 \
               + (3*pow(t,2) - 4*t + 1) * (self.x2 - self.x1) * self.dy1 \
               + (-6*pow(t,2) + 6*t) * self.y2 \
               + (3*pow(t,2) - 2*t) * (self.x2 - self.x1) * self.dy2
        return dydt * dtdx

        
        

