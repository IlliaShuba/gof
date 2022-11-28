package Flyweight;

import common.Letter;
import common.Order;
import common.Parcel;

import java.util.HashMap;
import java.util.Map;

public class OrderFactory {
    private static final Map<String, Order> orders = new HashMap<>();

    public Order getOrderByType(String type){
        Order order = orders.get(type);

        if(order == null) {
            switch (type){
                case "letter":
                    System.out.println("Create letter...");
                    order = new Letter();
                    break;
                case "parcel":
                    System.out.println("Create parcel...");
                    order = new Parcel();
            }
            orders.put(type, order);
        }
        return order;
    }
}
