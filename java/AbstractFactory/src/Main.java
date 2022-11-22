public class Main {
    public static void main(String[] args) {
        OrderFactory orderFactory = new LetterFactory();
        Cargo cargo = orderFactory.getCargo();
        Client client = orderFactory.getClient();
        Office office = orderFactory.getOffice();

        System.out.println("Start");

        cargo.showDescription();
        client.payment();
        office.processingOrder();

        System.out.println("Finish!");

    }
}