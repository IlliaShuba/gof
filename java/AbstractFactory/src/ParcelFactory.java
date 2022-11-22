public class ParcelFactory implements OrderFactory{
    @Override
    public Cargo getCargo(){
        return new Parcel();
    }
    @Override
    public Client getClient(){
        return new Company();
    }
    @Override
    public Office getOffice(){
        return new LargeOffice();
    }
}
