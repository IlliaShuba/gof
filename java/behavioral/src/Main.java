import chainOfResponsibities.*;
import iterator.Iterator;
import iterator.JavaDeveloper;
import mediator.Admin;
import mediator.SimpleTextChat;
import mediator.SimpleUser;
import mediator.User;
import сommand.*;

public class Main {
    public static void main(String[] args) {
        Main.Mediator();
    }

    public static void Chain() {
        Notifier reportNotifier = new SimpleReportNotifier(Priority.ROUTINE);
        Notifier emailNotifier = new EmailNotifier(Priority.IMPORTANT);
        Notifier smsNotifier = new SMSNotifier(Priority.ASAP);

        reportNotifier.setNextNotifier(emailNotifier);
        emailNotifier.setNextNotifier(smsNotifier);

        reportNotifier.notifyManager("Everything is OK.", Priority.ROUTINE);
        reportNotifier.notifyManager("Something went wrong!", Priority.IMPORTANT);
        reportNotifier.notifyManager("Houston, we`ve had a problem here!!!", Priority.ASAP);
    }
    public static void Command() {
        Database database = new Database();

        Developer developer = new Developer(
                new InsertCommand(database),
                new UpdateCommand(database),
                new SelectCommand(database),
                new DeleteCommand(database)
        );

        developer.insertRecord();
        developer.updateRecord();
        developer.selectRecord();
        developer.deleteRecord();
    }
    public static void Iterator() {
        String[] skills = {"Java", "Python", "PostgreSQL"};

        JavaDeveloper javaDeveloper = new JavaDeveloper("Illia Shuba", skills);

        Iterator iterator = javaDeveloper.getIterator();
        System.out.println("Developer: " + javaDeveloper.getName());
        System.out.println("Skills: ");

        while (iterator.hasNext()) {
            System.out.print(iterator.next().toString() + " ");
        }
    }

    public static void Mediator(){
        SimpleTextChat chat = new SimpleTextChat();

        User admin = new Admin(chat, "Admin");
        User user1 = new SimpleUser(chat, "User 1");
        User user2 = new SimpleUser(chat, "User 2");

        chat.setAdmin(admin);
        chat.addUserToChat(user1);
        chat.addUserToChat(user2);

        user1.sendMessage("Hello, I am user 1!!!");
        admin.sendMessage("Roger that. I am admin!");
    }

}
