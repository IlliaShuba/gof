package Bridge;

public abstract class Office {
    protected Order order;

    protected Office(Order order) {
        this.order = order;
    }
    public abstract void processingOrder();
}
