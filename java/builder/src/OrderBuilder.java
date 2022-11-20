public abstract class OrderBuilder {
    Order order;

    void createOrder(){
        order = new Order();
    }

    abstract void setType();
    abstract void setDescription();
    abstract void setPrice();

    Order getOrder(){
        return order;
    }
}
