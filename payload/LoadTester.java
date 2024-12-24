import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class LoadTester {

    private static final int THREAD_COUNT = 50; // Number of concurrent threads
    private static final int REQUEST_COUNT = 100; // Requests per thread
    private static final String TARGET_URL = "http://tf-autoscaling-alb-624675329.us-east-1.elb.amazonaws.com"; // Replace with your target URL

    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(THREAD_COUNT);

        for (int i = 0; i < THREAD_COUNT; i++) {
            executor.submit(() -> {
                for (int j = 0; j < REQUEST_COUNT; j++) {
                    long startTime = System.currentTimeMillis();
                    int responseCode = sendRequest(TARGET_URL);
                    long elapsedTime = System.currentTimeMillis() - startTime;

                    System.out.println("Response Code: " + responseCode + " | Time: " + elapsedTime + "ms");
                }
            });
        }

        executor.shutdown();
        while (!executor.isTerminated()) {
            // Wait for all tasks to finish
        }

        System.out.println("Load test completed.");
    }

    private static int sendRequest(String targetUrl) {
        try {
            URL url = new URL(targetUrl);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setConnectTimeout(5000); // 5 seconds timeout
            connection.setReadTimeout(5000);

            return connection.getResponseCode();
        } catch (IOException e) {
            System.err.println("Request failed: " + e.getMessage());
            return -1; // Indicates failure
        }
    }
}
