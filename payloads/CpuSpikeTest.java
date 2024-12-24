import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;


/**
 * Core Detection: The program detects the number of available CPU cores using Runtime.getRuntime().availableProcessors().
 * Target CPU Usage: You define the desired CPU usage (e.g., 80%).
 * Thread Workload: The program spawns threads performing a busy computation (Math.sqrt(Math.random())) to consume CPU.
 * Duration: The simulation runs for 30 seconds and then shuts down.
 */
public class CpuSpikeTest {

    public static void main(String[] args) {
        // Number of CPU cores available
        int availableCores = Runtime.getRuntime().availableProcessors();

        // Target CPU usage (e.g., 80%)
        double targetCpuUsage = 0.8;

        // Number of threads to simulate workload
        int numThreads = (int) (availableCores * targetCpuUsage);

        System.out.println("Starting CPU spike simulation...");
        System.out.println("Available Cores: " + availableCores);
        System.out.println("Spawning " + numThreads + " threads for computation.");

        // ExecutorService to manage threads
        ExecutorService executorService = Executors.newFixedThreadPool(numThreads);

        // Submit tasks that perform busy computations
        for (int i = 0; i < numThreads; i++) {
            executorService.submit(() -> {
                while (true) {
                    // Busy loop to consume CPU
                    Math.sqrt(Math.random());
                }
            });
        }

        // Keep the main thread running
        try {
            Thread.sleep(30000); // Simulate spike for 30 seconds
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        // Shutdown the executor service
        System.out.println("Shutting down CPU spike simulation...");
        executorService.shutdownNow();
    }
}