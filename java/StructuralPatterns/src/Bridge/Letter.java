package Bridge;

public class Letter implements Order {
    @Override
    public void delivery() {
        System.out.println("Letter delivery...");
    }
}

