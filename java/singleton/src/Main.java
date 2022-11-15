import java.util.List;

public class Main {
    public static void main(String[] args) {
        var user1 = "Ivan";
        var user2 = "Denis";
        saveStudent(user1);
        saveStudent(user2);
        List<String> allStudents = getAllStudents();
        System.out.println(allStudents);
    }


    private static void saveStudent(String student) {
        Singleton.getInstance().saveStudent(student);
        EnumSingleton.INSTANCE.saveStudent(student);
    }

    private static List<String> getAllStudents() {
        return EnumSingleton.INSTANCE.getAllStudents();
    }
}