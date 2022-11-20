public class LetterBuilder extends OrderBuilder{

    @Override
    void setType(){
        order.setType(Type.Letter);
    }

    @Override
    void setDescription(){
        order.setDescription("some description for letter");
    }
    @Override
    void setPrice(){
        order.setPrice(10);
    }
}
