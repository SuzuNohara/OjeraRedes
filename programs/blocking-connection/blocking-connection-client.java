import java.io.*;
import java.net.*;

public class TCPClient {
    public static void main(String[] args) {
        String host = "127.0.0.1";
        int port = 666;
        try (Socket socket = new Socket(host, port);

             PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()))) {

            out.println("Helo server, I'm the client");
            String response = in.readLine();
            System.out.println("Received: " + response);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
