
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public enum EnumSingleton {
    INSTANCE;

    private Set<String> db;

    private EnumSingleton() {
        db = new HashSet<>();
    }

    public void saveStudent(String s) {
        db.add(s);
    }

    public List<String> getAllStudents(){
        return new ArrayList<>(db);
    }
}