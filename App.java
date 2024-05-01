import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int pilihan;

        do {
            System.out.println("Menu Program");
            System.out.println("1. Pilihan 1");
            System.out.println("2. Pilihan 2");
            System.out.println("3. Pilihan 3");
            System.out.println("4. Keluar");
            System.out.print("Pilih opsi (1/2/3/4): ");
            
            // Membaca pilihan pengguna
            pilihan = input.nextInt();

            // Memproses pilihan
            switch (pilihan) {
                case 1:
                    System.out.println("Anda memilih Pilihan 1");
                    // Tambahkan kode untuk pilihan 1 di sini
                    break;
                case 2:
                    System.out.println("Anda memilih Pilihan 2");
                    // Tambahkan kode untuk pilihan 2 di sini
                    break;
                case 3:
                    System.out.println("Anda memilih Pilihan 3");
                    // Tambahkan kode untuk pilihan 3 di sini
                    break;
                case 4:
                    System.out.println("Terima kasih telah menggunakan program ini. Selamat tinggal!");
                    break;
                default:
                    System.out.println("Pilihan tidak valid. Silakan pilih kembali.");
                    break;
            }

        } while (pilihan != 4);

        input.close();
    }
}
