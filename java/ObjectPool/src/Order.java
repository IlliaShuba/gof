import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;

@Data
@ToString
@Builder
@NoArgsConstructor
public class Order {
    private String description;
    private int price;
    private Status status;

    public Order(String description, int price, Status status){
        this.description = description;
        this.price = price;
        this.status = status;
    }

    public void startProcessing() {
        System.out.println(this);
    }
}
