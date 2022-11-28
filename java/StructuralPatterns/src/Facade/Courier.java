package Facade;

public class Courier {
    public  void deliver(FacadeOrder order){
        if(order.isDelivered()){
            System.out.println("The courier delivered the order!");
        } else {
            System.out.println("The courier delivers the order...");
        }
    }
}
