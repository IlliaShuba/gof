class Cargo {
    private double weight;
    private double volume;

    public Cargo(double weight, double volume) {
        this.weight = weight;
        this.volume = volume;
    }

    public double getVolume() {
        return volume;
    }

    public void setVolume(double volume) {
        this.volume = volume;
    }

    public double getWeight() {
        return weight;
    }

    public void setWeight(double weight) {
        this.weight = weight;
    }
}

abstract class Order {
    private Cargo engine;
    private int price;
    private String description;

    public Cargo getCargo() {
        return engine;
    }

    public void setEngine(Cargo engine) {
        this.engine = engine;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public abstract Order clone();
}

public class Prototype extends Order {
    private Cargo cargo;
    private int price;
    private String description;

    public Prototype(Cargo cargo, int price, String description) {
        this.cargo = cargo;
        this.price = price;
        this.description = description;
    }

    public Cargo getCargo() {
        return cargo;
    }

    public void setCargo(Cargo cargo) {
        this.cargo = cargo;
    }

    public int getPrice() {
        return price;
    }
    public void setPrice(int price) {
        this.price = price;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    @Override
    public Order clone() {
        return new Prototype(new Cargo(this.cargo.getWeight(), this.cargo.getVolume()),
                this.price, this.description);
    }
}
