import Adapter.Adapter;
import Adapter.Database;
import Composite.Client;
import Composite.Letter;
import Composite.Order;
import Composite.Parcel;

public class Main {
    public static void main(String[] args) {
        Main.Composite();
    }

    public static void Adapter() {
        Database database = new Adapter();

        database.insert();
        database.update();
        database.select();
        database.remove();
    }

    public static void Composite() {
        Client client = new Client();

        Order firstOrder = new Parcel();
        Order secondOrder = new Letter();

        client.addOrder(firstOrder);
        client.addOrder(secondOrder);

        client.showOrder();
    }
}
