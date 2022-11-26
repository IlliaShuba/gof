package Decorator;

public class Letter extends OrderDecorator {
    public Letter(Order order) {
        super(order);
    }

    public String showInfo(){
        return "Letter";
    }

    @Override
    public void delivery() {
        super.delivery();
        System.out.print(showInfo());
    }
}
