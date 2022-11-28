package Decorator;

import common.Order;

public class OrderDecorator implements Order {
    Order order;

    public OrderDecorator(Order order) {
        this.order = order;
    }

    @Override
    public void delivery() {
        order.delivery();
    }
}
