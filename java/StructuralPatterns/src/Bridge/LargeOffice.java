package Bridge;

import common.Order;

public class LargeOffice extends Office {
    public LargeOffice(Order order) {
        super(order);
    }

    @Override
    public void processingOrder() {
        System.out.println("Large office processing order...");
        order.delivery();
    }
}
