import java.util.ArrayList;
import java.util.List;

public class Library {
    private List<Book> books;
    private List<User> users;
    private List<Loan> loans;

    public Library() {
        books = new ArrayList<>();
        users = new ArrayList<>();
        loans = new ArrayList<>();
    }

    public void addBook(Book book) {
        books.add(book);
    }

    public void removeBook(Book book) {
        books.remove(book);
    }

    public void registerUser(User user) {
        users.add(user);
    }

    public void borrowBook(String title, User user, int loanPeriodDays) {
        for (Book book : books) {
            if (book.getTitle().equalsIgnoreCase(title)) {
                if (!book.isBorrowed()) {
                    Loan loan = new Loan(book, user, loanPeriodDays);
                    loans.add(loan);
                    System.out.println(user.getName() + " emprestou o livro: " + title);
                } else {
                    System.out.println("O livro já está emprestado.");
                }
                return;
            }
        }
        System.out.println("Livro não encontrado.");
    }

    public void returnBook(String title, User user) {
        for (Loan loan : loans) {
            if (loan.getBook().getTitle().equalsIgnoreCase(title) && loan.getUser().equals(user)) {
                loan.returnBook();
                double fine = loan.calculateFine();
                if (fine > 0) {
                    System.out.println("Multa por atraso: R$ " + fine);
                }
                loans.remove(loan);
                System.out.println(user.getName() + " devolveu o livro: " + title);
                return;
            }
        }
        System.out.println("Empréstimo não encontrado.");
    }

    public void listBooks() {
        for (Book book : books) {
            System.out.println(book);
        }
    }

    public void listUsers() {
        for (User user : users) {
            System.out.println(user);
        }
    }

    public void searchBooksByTitle(String title) {
        for (Book book : books) {
            if (book.getTitle().equalsIgnoreCase(title)) {
                System.out.println(book);
            }
        }
    }

    public void searchBooksByAuthor(String author) {
        for (Book book : books) {
            if (book.getAuthor().equalsIgnoreCase(author)) {
                System.out.println(book);
            }
        }
    }

    public void listLoans() {
        for (Loan loan : loans) {
            System.out.println(loan);
        }
    }
}

