import java.time.LocalDateTime;

public class Transaction {

  String currency;
  double amount;
  String note;
  LocalDateTime currentDateTime;
  
  public Transaction(String currency, double amount, String note) {
    this.currency = currency;
    this.amount = amount;
    this.note = note;
    currentDateTime = LocalDateTime.now();
  }  
}
