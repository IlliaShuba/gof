package Decorator;

public class QuickOrder implements Order {
    @Override
    public void delivery() {
        System.out.print("Delivery quick order ");
    }
}
