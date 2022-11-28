package Facade;

public class Workflow {
    Courier courier = new Courier();
    Worker worker = new Worker();
    FacadeOrder order = new FacadeOrder();

    public void process() {
        worker.packing();
        order.start();
        courier.deliver(order);
    }
}
