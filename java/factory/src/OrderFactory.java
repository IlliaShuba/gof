import java.util.HashMap;
import java.util.Map;

public class OrderFactory {
    public static Order create(IOrder order) {
        Map<IOrder, Order> dictionary = new HashMap<IOrder, Order>() {{
            put(IOrder.Letter, new Letter());
            put(IOrder.Documents, new Documents());
            put(IOrder.Parcel, new Parcel());
        }};

        return dictionary.get(order);
    }
}
