package Decorator;

import common.Order;

public class DecoratorLetter extends OrderDecorator {
    public DecoratorLetter(Order order) {
        super(order);
    }

    public String showInfo(){
        return "Letter";
    }

    @Override
    public void delivery() {
        super.delivery();
        System.out.print(showInfo());
    }
}
