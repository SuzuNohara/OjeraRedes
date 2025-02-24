import java.io.*;
import java.net.*;

public class TCPServer {
    public static void main(String[] args) {
        int port = 666;
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("Server listening in port: " + port);

            Socket socket = serverSocket.accept();
            System.out.println("Connected from: " + socket.getInetAddress());

            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

            String inputLine;
            while ((inputLine = in.readLine()) != null) {
                System.out.println("Received: " + inputLine);
                out.println(inputLine);
            }
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
