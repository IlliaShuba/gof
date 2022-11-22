public class Main {
    public static void main(String[] args) {
        var pool = new OrderPool();
        var order = pool.getOrder();

        pool.getOrder().startProcessing();
        pool.releaseOrder(order);
        pool.getOrder().startProcessing();
    }
}
