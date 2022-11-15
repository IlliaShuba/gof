import java.util.HashSet;
import java.util.Set;

public class Singleton {
    private static Singleton INSTANCE;
    private Set<String> db; //db simulator

    private Singleton() {
        db = new HashSet<>();
    }

    public static Singleton getInstance() {
        if (INSTANCE == null) {
            INSTANCE = new Singleton();
        }
        return INSTANCE;
    }

    public void clear() {
        db.clear();
    }

    public void saveStudent(String s) {
        db.add(s);
    }

}