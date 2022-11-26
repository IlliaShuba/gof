import Adapter.Adapter;
import Adapter.Database;
import Composite.*;
import Bridge.*;
import Decorator.*;
import Decorator.Order;
import Facade.*;


public class Main {
    public static void main(String[] args) {
        Main.Facade();
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

        Composite.Order firstOrder = new Composite.Parcel();
        Composite.Order secondOrder = new Composite.Letter();

        client.addOrder(firstOrder);
        client.addOrder(secondOrder);

        client.showOrder();
    }
    public static void Decorator(){
        Order order = new Decorator.Parcel(new QuickOrder());
        order.delivery();
    }

    public static void Facade(){
        Workflow workflow = new Workflow();
        workflow.process();
    }
}
