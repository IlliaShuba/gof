public class Director {
    OrderBuilder builder;

    public void setBuilder(OrderBuilder builder) {
        this.builder = builder;
    }

    Order buildOrder(){
        builder.createOrder();
        builder.setType();
        builder.setDescription();
        builder.setPrice();

        return builder.getOrder();
    }
}
