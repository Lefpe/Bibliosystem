import java.time.LocalDate;

public class Loan {
    private Book book;
    private User user;
    private LocalDate borrowDate;
    private LocalDate dueDate;

    public Loan(Book book, User user, int loanPeriodDays) {
        this.book = book;
        this.user = user;
        this.borrowDate = LocalDate.now();
        this.dueDate = borrowDate.plusDays(loanPeriodDays);
        book.borrowBook();
    }

    public Book getBook() {
        return book;
    }

    public User getUser() {
        return user;
    }

    public LocalDate getBorrowDate() {
        return borrowDate;
    }

    public LocalDate getDueDate() {
        return dueDate;
    }

    public boolean isOverdue() {
        return LocalDate.now().isAfter(dueDate);
    }

    public double calculateFine() {
        if (isOverdue()) {
            long daysOverdue = LocalDate.now().toEpochDay() - dueDate.toEpochDay();
            return daysOverdue * 2.0; // Exemplo: R$2,00 por dia de atraso
        }
        return 0.0;
    }

    public void returnBook() {
        book.returnBook();
    }

    @Override
    public String toString() {
        return "Livro: " + book.getTitle() + ", Usuário: " + user.getName() +
               ", Data de Empréstimo: " + borrowDate + ", Data de Devolução: " + dueDate;
    }
}
