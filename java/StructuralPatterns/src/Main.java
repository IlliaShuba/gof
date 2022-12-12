import Adapter.Adapter;
import Adapter.Database;
import common.Order;
import common.Letter;
import common.Parcel;
import Composite.*;
import Bridge.*;
import Decorator.*;
import Facade.*;
import Flyweight.OrderFactory;
import Proxy.Project;
import Proxy.ProxyProject;


import java.util.ArrayList;
import java.util.List;


public class Main {
    public static void main(String[] args) {Main.Flyweight();}

    public static void Adapter() {
        Database database = new Adapter();

        database.insert();
        database.update();
        database.select();
        database.remove();
    }
    public static void Bridge(){
        Office[] offices = {
                new LargeOffice(new Letter()),
                new SmallOffice(new Parcel())
        };

        for(Office office: offices) {
            office.processingOrder();
        }
    }
    public static void Composite() {
        Client client = new Client();

        Order firstOrder = new Parcel();
        Order secondOrder = new Letter();

        client.addOrder(firstOrder);
        client.addOrder(secondOrder);

        client.showOrder();
    }
    public static void Decorator(){
        Order order = new DecoratorParcel(new QuickOrder());
        order.delivery();
    }
    public static void Facade(){
        Workflow workflow = new Workflow();
        workflow.process();
    }
    public static void Flyweight(){
        OrderFactory orderFactory = new OrderFactory();

        List<Order> orders = new ArrayList<>();

        orders.add(orderFactory.getOrderByType("letter"));
        orders.add(orderFactory.getOrderByType("letter"));
        orders.add(orderFactory.getOrderByType("parcel"));
        orders.add(orderFactory.getOrderByType("parcel"));

        for(Order order: orders){
            order.delivery();
        }
    }
    public static void Proxy(){
        Project project = new ProxyProject("https://www.github.com/some/realProject");
        project.run();
    }
}
