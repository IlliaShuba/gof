import Adapter.Adapter;
import Adapter.Database;

public class Main {
    public static void main(String[] args) {
        Main.Adapter();
    }

    public static void Adapter() {
        Database database = new Adapter();

        database.insert();
        database.update();
        database.select();
        database.remove();
    }
}
