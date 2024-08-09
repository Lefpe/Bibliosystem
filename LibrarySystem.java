import java.util.Scanner;

public class LibrarySystem {
    public static void main(String[] args) {
        Library library = new Library();
        Scanner scanner = new Scanner(System.in);

        // Adicionando livros à biblioteca
        library.addBook(new Book("O Senhor dos Anéis", "J.R.R. Tolkien"));
        library.addBook(new Book("Harry Potter e a Pedra Filosofal", "J.K. Rowling"));
        library.addBook(new Book("1984", "George Orwell"));

        // Registrando usuários
        User user1 = new User("Alice");
        User user2 = new User("Bob");
        library.registerUser(user1);
        library.registerUser(user2);

        // Interação por linha de comando
        while (true) {
            System.out.println("\nEscolha uma opção:");
            System.out.println("1. Listar livros");
            System.out.println("2. Buscar livro por título");
            System.out.println("3. Buscar livro por autor");
            System.out.println("4. Listar usuários");
            System.out.println("5. Emprestar livro");
            System.out.println("6. Devolver livro");
            System.out.println("7. Listar empréstimos");
            System.out.println("0. Sair");

            int choice = scanner.nextInt();
            scanner.nextLine();  // Consumir nova linha

            switch (choice) {
                case 1:
                    library.listBooks();
                    break;
                case 2:
                    System.out.print("Digite o título do livro: ");
                    String title = scanner.nextLine();
                    library.searchBooksByTitle(title);
                    break;
                case 3:
                    System.out.print("Digite o autor do livro: ");
                    String author = scanner.nextLine();
                    library.searchBooksByAuthor(author);
                    break;
                case 4:
                    library.listUsers();
                    break;
                case 5:
                    System.out.print("Digite o título do livro: ");
                    String borrowTitle = scanner.nextLine();
                    System.out.print("Digite o nome do usuário: ");
                    String userName = scanner.nextLine();
                    System.out.print("Digite o período de empréstimo em dias: ");
                    int days = scanner.nextInt();
                    scanner.nextLine();  // Consumir nova linha
                    User userBorrow = library.getUsers().stream()
                        .filter(user -> user.getName().equalsIgnoreCase(userName))
                        .findFirst().orElse(null);
                    if (userBorrow != null) {
                        library.borrowBook(borrowTitle, userBorrow, days);
                    } else {
                        System.out.println("Usuário não encontrado.");
                    }
                    break;
                case 6:
                    System.out.print("Digite o título do livro: ");
                    String returnTitle = scanner.nextLine();
                    System.out.print("Digite o nome do usuário: ");
                    String returnUser = scanner.nextLine();
                    User userReturn = library.getUsers().stream()
                        .filter(user -> user.getName().equalsIgnoreCase(returnUser))
                        .findFirst().orElse(null);
                    if (userReturn != null) {
                        library.returnBook(returnTitle, userReturn);
                    } else {
                        System.out.println("Usuário não encontrado.");
                    }
                    break;
                case 7:
                    library.listLoans();
                    break;
                case 0:
                    System.out.println("Saindo...");
                    scanner.close();
                    return;
                default:
                    System.out.println("Opção inválida.");
            }
        }
    }
}
