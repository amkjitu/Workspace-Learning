public class Account {
   private int accountNumber;
   public String accountHolderName;
   private double balance;

   public void setterAccountNumber(int accountNumber) {
      this.accountNumber = accountNumber;
   }

   public int getterAccountNumber() {
      return this.accountNumber;
   }

   public void withdraw(double amount) {
      if (amount < 0.0D) {
         System.out.println("Invalid amount");
      } else if (amount > this.balance) {
         System.out.println("Insufficient funds");
      } else {
         this.balance -= amount;
      }
   }

   public void deposit(double amount) {
      if (amount < 0.0D) {
         System.out.println("Invalid amount");
      } else {
         this.balance += amount;
      }
   }

   public double getBalance() {
      return this.balance;
   }
}
