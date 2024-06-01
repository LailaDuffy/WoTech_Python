import java.util.ArrayList;

public class Account {

  String accountNumber;
  String currency;
  double balance;
  ArrayList<Transaction> transactions;

  public Account(String accountNumber, String currency, double balance){
    this.accountNumber = accountNumber;
    this.currency = currency;
    this.balance = balance;
    transactions = new ArrayList<Transaction>();
  }

  // constructor with default balance value
  public Account(String accountNumber, String currency) {
    this.accountNumber = accountNumber;
    this.currency = currency;
    this.balance = 0.0;
  }

  public void makeDeposit(double amount, String note) {
    transactions.add(new Transaction(this.currency, amount, note));
    this.balance += amount;
  }

  public void makeWithdrawal(double amount, String note) {
    transactions.add(new Transaction(this.currency, -amount, note));
    if (this.balance >= amount) {
      this.balance -= amount;
    } else {
      System.out.println("Insufficient funds!");
    }
  }
}
