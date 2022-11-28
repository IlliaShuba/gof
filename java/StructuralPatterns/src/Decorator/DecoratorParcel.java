package Decorator;

import common.Order;

public class DecoratorParcel extends OrderDecorator {

    public DecoratorParcel(Order order) {
        super(order);
    }

    public String showDescription() {
        return "Parcel";
    }

    @Override
    public void delivery() {
        super.delivery();
        System.out.print(showDescription());
    }
}
