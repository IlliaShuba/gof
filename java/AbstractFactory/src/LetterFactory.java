public class LetterFactory implements OrderFactory {
    @Override
    public Cargo getCargo(){
        return new Letter();
    }
    @Override
    public Client getClient(){
        return new NaturalPerson();
    }
    @Override
    public Office getOffice(){
        return new SmallOffice();
    }

}
