package Composite;

public class Parcel implements Order {
    @Override
    public void delivery() {
        System.out.println("Parcel delivery...");
    }
}
