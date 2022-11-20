public class Order {
    private Type type;
    private String description;
    private int price;

    public void setType(Type type) {
        this.type = type;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    @Override
    public String toString() {
        return "Order{" +
                "type=" + type +
                ", description='" + description + '\'' +
                ", price='" + price + '\'' +
                '}';
    }
}
