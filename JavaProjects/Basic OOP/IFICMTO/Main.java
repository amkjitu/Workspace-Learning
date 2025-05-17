import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("Starting the Payroll...\n");
    /// Account Class
    //     Account account = new Account();

    //     Scanner scanner = new Scanner(System.in);

    //     int accountNumber;
    //     accountNumber = scanner.nextInt();
    //     scanner.nextLine();

    //     account.setterAccountNumber(accountNumber);

    //     String holderName;
    //     holderName = scanner.nextLine();
    //     account.accountHolderName = holderName;

    //     System.out.println("Account Number: " + account.getterAccountNumber());
    //     System.out.println("Account Holder: " + account.accountHolderName);
        
    //     System.out.println("Your Initial Balance: " + account.getBalance());
        
    //     System.out.println("Enter the amount to deposit");

    //     double damount = scanner.nextDouble();
    //     account.deposit(damount);
        
    //     System.out.println("Your Balance after deposit: " + account.getBalance());

    //     System.out.println("Enter the amount to withdraw: ");
    //     double wamount = scanner.nextDouble();
    //     account.withdraw(wamount);
    //     System.out.println("Your Current Balance: " + account.getBalance());

    /// Manager Class + Engineer Class
    // Manager manager = new Manager("Alice", 200.0, 20.0);
    // System.out.println("Manager Your Basic Salary: " + manager.basicSalary);

    // manager.calculateSalary(100.0);
    // System.out.println("Your Basic Salary after Percentage " + manager.basicSalary);

    // manager.calculateSalary();
    // System.out.println("Your Basic Salary after Bonus " + manager.basicSalary);

    // Engineer engineer = new Engineer("Bob", 100.0, 2);
    // System.out.println("Engineer Your Basic Salary: " + engineer.basicSalary);

    // engineer.calculateSalary(30);
    // System.out.println("Your Basic Salary after Increment " + engineer.basicSalary);

    // engineer.calculateSalary();
    // System.out.println("Your Basic Salary after Overtime " + engineer.basicSalary);

    /// Manager Class + Engineer Class stored in array list
    ArrayList<Employee> employees = new ArrayList<>();
    employees.add(new Manager("Alice", 200.0, 20.0));
    employees.add(new Engineer("Bob", 100.0, 2));

    for (Employee employee : employees) {

    System.out.println(employee.name +", Your Basic Salary: " + employee.basicSalary);
    employee.calculateSalary(100.0);
    System.out.println("Basic Salary after Percentage: " + employee.basicSalary);
    employee.calculateSalary();
    System.out.println("Basic Salary after Bonus or Overtime: " + employee.basicSalary);
    System.out.println();
    }

    }
}