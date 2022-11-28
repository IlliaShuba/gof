package Composite;

import common.Order;

import java.util.ArrayList;
import java.util.List;

public class Client {
    private List<Order> orders = new ArrayList<Order>();

    public void addOrder(Order order) {
        orders.add(order);
    }

    public void removeOrder(Order order){
        orders.remove(order);
    }

    public void showOrder(){
        System.out.println("Show client order...\n");
        for(Order developer: orders){
            developer.delivery();
        }
    }
}
