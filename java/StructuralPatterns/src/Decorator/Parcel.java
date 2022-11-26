package Decorator;

public class Parcel extends OrderDecorator {

    public Parcel(Order order) {
        super(order);
    }

    public String showDescription() {
        return "Parcel";
    }

    @Override
    public void delivery() {
        super.delivery();
        System.out.print(showDescription());
    }
}
