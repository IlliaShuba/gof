package Facade;

public class Workflow {
    Courier courier = new Courier();
    Worker worker = new Worker();
    Order order = new Order();

    public void process() {
        worker.packing();
        order.start();
        courier.deliver(order);
    }
}
