public class Main {
    public static void main(String[] args) {
        Cargo cargo = new Cargo(3.0, 4);
        Order order1 = new Prototype(cargo, 5, "some description");
        Order order2 = order1.clone();
        System.out.println(order1.getPrice());
        System.out.println(order1.getCargo().getVolume());
        System.out.println("\n");
        System.out.println(order2.getDescription());
        System.out.println(order2.getCargo().getVolume());
        System.out.println("\n");

        order2.getCargo().setVolume(5.0);
        order2.getCargo().setWeight(400);

        System.out.println(order1.getCargo().getWeight());
        System.out.println(order2.getPrice());
        System.out.println(order2.getCargo().getWeight());
        System.out.println(order2.getCargo().getVolume());
    }
}
