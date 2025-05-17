class Manager extends Employee{
    double bonus;

    Manager(String name, double basicSalary, double bonus){
        super(name, basicSalary);
        this.bonus = bonus;
    }

    protected double calculateSalary() {
        this.basicSalary = this.basicSalary + this.bonus;
        return this.basicSalary;
    }
}