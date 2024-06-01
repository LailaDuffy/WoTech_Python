import java.util.ArrayList;

public class Client {
  public static int numberOfClients = 0;

  public String name;
  public int ID;
  public ArrayList<Account> accounts;

  public Client(int ID, String name) {
    this.ID = ID;
    this.name = name;
    accounts = new ArrayList<Account>();
    numberOfClients++;
  }

  public void addAccount(Account account) {
    accounts.add(account);
  }
}
