import java.util.ArrayList;

public class Main {
  public static void main(String[] args) {

    // creating a list for clients and adding new clients 
    ArrayList<Client> clients = new ArrayList<Client>();
    clients.add(new Client(100001, "Anna"));
    clients.add(new Client(100002, "Oskars"));
    clients.add(new Client(100003, "Jennifer"));

    System.out.println("Total number of clients: " + Client.numberOfClients);

    // accessing Oskars id
    System.out.println("Oskar's ID is: " + clients.get(1).ID);

    // accessing every clients name
    for (Client client : clients) {
      System.out.println("Client's name: " + client.name);
    }

    // creating and adding an account for a each client
    clients.get(0).addAccount(new Account("EE547852366654", "EUR", 1000.00));
    clients.get(0).addAccount(new Account("JP568768458466", "JPY", 25000.00));
    clients.get(0).addAccount(new Account("US447589005252", "USD"));

    clients.get(1).addAccount(new Account("PL444400010016", "PLN", 47800.00));
    clients.get(1).addAccount(new Account("SE656565640401", "SEK", 200.18));

    clients.get(2).addAccount(new Account("FR444779898980", "EUR"));

    // printing out each client and their list of accounts
    for (Client client : clients) {
      System.out.println(client.name + " has the following accounts: " );
      for (Account account : client.accounts) {
        System.out.println("  " + account.accountNumber + " (" + account.currency + "), balance " + account.balance);
      }
    }

    // make transactions
    clients.get(0).accounts.get(0).makeDeposit(1200.00, "salary");
    clients.get(0).accounts.get(0).makeWithdrawal(50, "groceries");
    clients.get(0).accounts.get(0).makeWithdrawal(140, "clothes");
    clients.get(0).accounts.get(0).makeWithdrawal(20, "dinner");


    for (Client client : clients) {
      System.out.println(client.name);
      for (Account account : client.accounts) {
        System.out.println("  " + account.accountNumber);
        try {
          for (Transaction transaction : account.transactions) {          
              if (!account.transactions.isEmpty()) {
              System.out.println("    " + transaction.currentDateTime + " " + transaction.currency + " " + transaction.amount + " " + transaction.note);
              }
          }
        } catch (Exception e) {
            System.out.print("");
        }        
      }
    }
  }
}
