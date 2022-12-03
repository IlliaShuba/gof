package memento;

public class SaveProjectRunner {
    public static void main(String[] args) throws InterruptedException {
        Project project = new Project();
        GithudRepo github = new GithudRepo();

        System.out.println("Creating new project. Version  1.0");
        project.setVersionAndDate("Version 1.0");

        System.out.println("Saving current version to GitHub...");
        github.setSave(project.save());

        System.out.println("updating project to version 1.1");

        System.out.println("Write poor code...");
        Thread.sleep(5000);


        project.setVersionAndDate("Version 1.1");

        System.out.println(project);

        System.out.println("Something went wrong...");

        System.out.println("Rolling back to version 1.0");
        project.load(github.getSave());

        System.out.println("Project after rollback.");
        System.out.println(project);
    }
}
