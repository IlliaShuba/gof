package Facade;

public class Order {
    private boolean isDelivered;

    public boolean isDelivered() {
        return isDelivered;
    }

    public void start() {
        System.out.println("Order is active.");
        isDelivered = false;
    }

    public void finish() {
        System.out.println("Order is not active.");
        isDelivered = true;
    }
}
