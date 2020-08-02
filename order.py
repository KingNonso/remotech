import unittest

class OrderBook:
    def __init__(self):
        self.orders = {}
        self.best_sell = {'price': 0}
        self.best_buy = {'price': 0}

    # Given a side (BUY or SELL) and a price, add a new open order,
    # and return its unique order id (or a struct containing it).
    def addOpenOrder(self, side, price):
        key = len(self.orders)
        order = {
            'id': key,
            'side': side,
            'price': price
        }
        self.orders[key] = order
        if side == 'BUY' and price >= self.best_buy['price']:
            self.best_buy = order

        if side == 'SELL':
            if self.best_sell['price'] == 0:
                self.best_sell = order
            elif price <= self.best_sell['price']:
                self.best_sell = order

        print(self.orders)
        print(self.best_buy)
        print(self.best_sell)
        return order

    # Given an order id, delete the order from list of open orders.
    # Behavior is undefined if there is no order with this id.
    def deleteOpenOrder(self, orderId):
        del self.orders[orderId]
        print(self.orders)

    # Return the "best" open order on the given side. The result should
    # include all of the details for the order, including price and order id.
    # - The "best" buy order is the buy order with the highest price
    # - The "best" sell order is the sell order with the lowest price
    # - For ties (multiple orders with best price), return order added most recently
    # @staticmethod
    def bestOpenOrder(self, side):
        if side == 'BUY':
            return self.best_buy
        if side == 'SELL':
            return self.best_sell


class TestOrder(unittest.TestCase):

    def test_buy(self):
        bk = OrderBook()
        order1 = bk.addOpenOrder('BUY', 10)
        order2 = bk.addOpenOrder('BUY', 10)
        order3 = bk.addOpenOrder('BUY', 12)
        order4 = bk.addOpenOrder('SELL', 11)
        order5 = bk.addOpenOrder('SELL', 20)
        self.assertEqual(bk.bestOpenOrder('BUY')['id'], order3['id'])

    def test_sell(self):
        bk = OrderBook()
        order1 = bk.addOpenOrder('BUY', 10)
        order2 = bk.addOpenOrder('BUY', 10)
        order3 = bk.addOpenOrder('BUY', 12)
        order4 = bk.addOpenOrder('SELL', 11)
        order5 = bk.addOpenOrder('SELL', 20)

        self.assertEqual(bk.bestOpenOrder('SELL')['price'], 11)


if __name__ == '__main__':
    unittest.main()

