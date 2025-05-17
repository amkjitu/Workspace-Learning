public class Engineer extends Employee {
    int overTime;

    public Engineer(String name, double basicSalary, int overTime) {
        super(name, basicSalary);
        this.overTime = overTime;
    }

    protected double calculateSalary() {
        this.basicSalary = this.basicSalary + (this.basicSalary * this.overTime) / 8;
        return this.basicSalary;
    }
}
