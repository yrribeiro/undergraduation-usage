package edu.coursera.distributed;

import edu.coursera.distributed.PCDPFilesystem;
import edu.coursera.distributed.PCDPPath;
import java.net.ServerSocket;
import java.net.Socket;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.OutputStream;
import java.io.File;

/**
 * A basic and very limited implementation of a file server that responds to GET
 * requests from HTTP clients.
 */
public final class FileServer {
    /**
     * Main entrypoint for the basic file server.
     *
     * @param socket Provided socket to accept connections on.
     * @param fs A proxy filesystem to serve files from. See the PCDPFilesystem
     *           class for more detailed documentation of its usage.
     * @throws IOException If an I/O error is detected on the server. This
     *                     should be a fatal error, your file server
     *                     implementation is not expected to ever throw
     *                     IOExceptions during normal operation.
     */
    public void run(final ServerSocket socket, final PCDPFilesystem fs) throws IOException {
        while (true) {
            Socket clientSocket = socket.accept();

            InputStream inputStream = clientSocket.getInputStream();
            OutputStream outputStream = clientSocket.getOutputStream();

            String request = getRequest(inputStream);
            String filePath = parseFilePath(request);

            PCDPPath path = new PCDPPath(filePath);
            String fileContents = fs.readFile(path);

            if (fileContents != null) {
                sendResponse(outputStream, "HTTP/1.0 200 OK\r\n\r\n" + fileContents);
            } else {
                sendResponse(outputStream, "HTTP/1.0 404 Not Found\r\n\r\n");
            }

            outputStream.close();
            clientSocket.close();
        }
    }

    private String getRequest(InputStream inputStream) throws IOException {
        // Read and parse the HTTP request from the input stream
        // Return the request as a string
        BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
        StringBuilder requestBuilder = new StringBuilder();
        String line;

        while ((line = reader.readLine()) != null && !line.isEmpty()) {
            requestBuilder.append(line).append("\r\n");
        }

        return requestBuilder.toString();
    }

    private String parseFilePath(String request) {
        // Parse the file path from the HTTP request string
        // Return the file path as a string
        int startIndex = request.indexOf("GET ") + 4;
        int endIndex = request.indexOf(" HTTP/1.");
        return request.substring(startIndex, endIndex);
    }

    private void sendResponse(OutputStream outputStream, String response) throws IOException {
        // Send the HTTP response to the output stream
        outputStream.write(response.getBytes());
        outputStream.flush();
    }
}
