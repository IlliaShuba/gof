import java.util.Arrays;
import java.util.List;

public class OrderPool {
    private List<Order> pool = Arrays.asList(
            Order.builder().description("some description 1").price(100).status(Status.READY).build(),
            Order.builder().description("some description 2").price(200).status(Status.READY).build()
    );

    public Order getOrder() {
        if (hasFree()) {
            var order = pool.stream().filter(el -> el.getStatus() == Status.READY).findFirst().get();
            order.setStatus(Status.RUNNING);
            return order;

        } else {
            System.out.println("No free order now");
            return null;
        }
    }

    public void releaseOrder(Order webMeeting) {
        webMeeting.setStatus(Status.READY);
    }

    private boolean hasFree() {
        return pool.stream().anyMatch(el -> el.getStatus() == Status.READY);
    }
}
