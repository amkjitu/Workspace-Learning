public abstract class Employee {
    protected String name;
    protected double basicSalary;

    protected Employee(String name, double basicSalary) {
        this.name = name;
        this.basicSalary = basicSalary;
    }

    protected abstract double calculateSalary();

    protected double calculateSalary(int increment) {
        this.basicSalary = this.basicSalary + increment;
        return this.basicSalary;
    }

    protected double calculateSalary(double percentage) {
        this.basicSalary = this.basicSalary + (percentage*this.basicSalary)/100;
        return this.basicSalary;
    }
}