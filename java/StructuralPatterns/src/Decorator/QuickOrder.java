package Decorator;

import common.Order;

public class QuickOrder implements Order {
    @Override
    public void delivery() {
        System.out.print("Delivery quick order ");
    }
}
