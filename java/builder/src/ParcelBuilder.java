public class ParcelBuilder extends OrderBuilder{

    @Override
    void setType(){
        order.setType(Type.Parcel);
    }

    @Override
    void setDescription(){
        order.setDescription("some description for parcel");
    }
    @Override
    void setPrice(){
        order.setPrice(100);
    }
}
