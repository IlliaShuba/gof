public class Main {
    public static void main(String[] args) {
        Director director = new Director();
        director.setBuilder(new LetterBuilder());

        Order order = director.buildOrder();
        System.out.println(order);
    }
}
