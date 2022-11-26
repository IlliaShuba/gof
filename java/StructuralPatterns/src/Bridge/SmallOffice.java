package Bridge;

public class SmallOffice extends Office {
    public SmallOffice(Order order) {
        super(order);
    }

    @Override
    public void processingOrder() {
        System.out.println("Small office processing order...");
        order.delivery();
    }
}
