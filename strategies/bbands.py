import backtrader as bt

from strategy import Strategy


class Aberration(Strategy):
    """Bollinger Bands Strategy
    """

    params = (
        ('period', 20),
        ('devfactor', 2),
    )

    def __init__(self):
        # Add a BBand indicator
        self.bband = bt.indicators.BBands(self.datas[0],
                                          period=self.p.period,
                                          devfactor=self.p.devfactor)
        super(Aberration, self).__init__()

    def next(self):
        super(Aberration, self).next()

        # Check if an order is pending ... if yes, we cannot send a 2nd one
        if self.order:
            return

        if self.orefs:
            return

        if self.dataclose < self.bband.lines.bot and not self.position:
            self.buy()

        if self.dataclose > self.bband.lines.top and self.position:
            self.sell()
