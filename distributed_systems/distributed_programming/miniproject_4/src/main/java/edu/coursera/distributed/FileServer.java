package edu.coursera.distributed;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;

public final class FileServer {
    public void run(final ServerSocket socket, final PCDPFilesystem fs, final int ncores) throws IOException {
        while (true) {
            Socket clientSocket = socket.accept();

            Thread thread = new Thread(() -> {
                try {
                    InputStream inputStream = clientSocket.getInputStream();
                    OutputStream outputStream = clientSocket.getOutputStream();

                    // Read the HTTP request from the input stream
                    BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
                    String requestLine = reader.readLine();
                    if (requestLine != null) {
                        String[] requestParts = requestLine.split(" ");
                        if (requestParts.length == 3 && requestParts[0].equals("GET")) {
                            String filePath = URLDecoder.decode(requestParts[1], StandardCharsets.UTF_8);

                            byte[] fileContents = fs.readFile(new PCDPPath(filePath)).getBytes(StandardCharsets.UTF_8);

                            if (fileContents != null) {
                                String response = "HTTP/1.0 200 OK\r\n" +
                                        "Server: FileServer\r\n" +
                                        "\r\n";
                                byte[] responseBytes = response.getBytes(StandardCharsets.UTF_8);
                                outputStream.write(responseBytes);
                                outputStream.write(fileContents);
                            } else {
                                String response = "HTTP/1.0 404 Not Found\r\n" +
                                        "Server: FileServer\r\n" +
                                        "\r\n";
                                byte[] responseBytes = response.getBytes(StandardCharsets.UTF_8);
                                outputStream.write(responseBytes);
                            }
                        }
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                } finally {
                    try {
                        clientSocket.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            });

            thread.start();
        }
    }
}
