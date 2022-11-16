public class Main {
    public static void main(String[] args) {
        for (IOrder order : IOrder.values()) {
            Order newOrder = OrderFactory.create(order);
            System.out.println("New order is " + order + " and it's price is " + newOrder.getPrice());
        }
    }
}
