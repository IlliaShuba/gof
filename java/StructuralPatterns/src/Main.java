import Adapter.Adapter;
import Adapter.Database;
import Composite.*;
import Composite.Order;
import Bridge.*;

public class Main {
    public static void main(String[] args) {
        Main.Bridge();
    }

    public static void Adapter() {
        Database database = new Adapter();

        database.insert();
        database.update();
        database.select();
        database.remove();
    }

    public static void Bridge(){
        Office[] offices = {
                new LargeOffice(new Bridge.Letter()),
                new SmallOffice(new Bridge.Parcel())
        };

        for(Office office: offices) {
            office.processingOrder();
        }
    }

    public static void Composite() {
        Client client = new Client();

        Order firstOrder = new Composite.Parcel();
        Order secondOrder = new Composite.Letter();

        client.addOrder(firstOrder);
        client.addOrder(secondOrder);

        client.showOrder();
    }
}
