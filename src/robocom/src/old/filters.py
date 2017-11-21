
import math

# Exponential (one-pole) smoothing filter
class ExpFilter:
    def __init__(self, ts, fc, th=None):
        self.th = th
        self.fs = -1.0
        self.ts = ts
        
        self.tau = -1.0
        self.wc = -1.0
        self.fc = fc
        
        self.a = -1.0
        self.b = -1.0
        
        self.setSamplingTime(ts)
        self.setFrequency(fc)
        self.update()

    def _clamp(self, value):
        return max(0.000000001, min(float(value), 1000000000.0))

    def setThreshold(self, th):
        self.th = abs(float(th)) if th else None
        return self
        
    def setTimeConstant(self, tau):
        self.tau = self._clamp(tau)
        self.wc = 1.0 / self.tau
        self.fc = self.wc * (1.0 / (2.0 * math.pi))
        return self

    def setPulsation(self, wc):
        self.setTimeConstant(1.0 / self._clamp(wc))
        return self

    def setSettlingTime(self, tt):
        self.setTimeConstant(0.2 * self._clamp(tt))
        return self

    def setFrequency(self, fc):
        self.setTimeConstant(1.0 / ((2.0 * math.pi) * self._clamp(fc)))
        return self

    def setSamplingTime(self, ts):
        self.ts = self._clamp(ts)
        self.fs = 1.0 / self.ts
        return self

    def setSamplingRate(self, fs):
        self.setSamplingTime(1.0 / self._clamp(fs))
        return self

    def update(self):
        self.b = 1.0 / (self.fs * (self.tau + (1.0 / self.fs)))
        self.a = 1.0 - self.b
        return self
    
    def process(self, current, previous):
        current = self.b * current + self.a * previous
        if self.th and abs(current) < self.th: return 0.0
        return current


# Smoothed 3D vector
class SmoothedVec3:
    def __init__(self, smoother, v0):
        assert isinstance(smoother, ExpFilter)
        self._smoother = smoother
        self._h3 = [ [ float(v0[0]) ] * 2,
                     [ float(v0[1]) ] * 2,
                     [ float(v0[2]) ] * 2 ]

    def last(self):
        return ( self._h3[0][0], self._h3[1][0], self._h3[2][0] )
    
    def process(self, setpoint):
        for i in range(3):
            self._h3[i][1] = self._h3[i][0]
            self._h3[i][0] = self._smoother.process(setpoint[i], self._h3[i][0])
        return self.last()

