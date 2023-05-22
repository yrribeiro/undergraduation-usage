package edu.coursera.distributed;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import org.apache.spark.api.java.JavaPairRDD;
import scala.Tuple2;

public final class PageRank {
    private PageRank() {
    }

    public static JavaPairRDD<Integer,Double> sparkPageRank(
            final JavaPairRDD<Integer, Website> sites,
            final JavaPairRDD<Integer, Double> ranks) {

        // Compute contributions of each page to the rank of other pages
        JavaPairRDD<Integer, Double> contributions = sites.join(ranks)
                .flatMapToPair(join -> {
                    int websiteId = join._1();
                    Tuple2<Website, Double> value = join._2();
                    Website website = value._1();
                    double rank = value._2();
                    int outCount = website.getNEdges();

                    // Distribute rank to outbound links
                    List<Tuple2<Integer, Double>> results = new ArrayList<>();
                    Iterator<Integer> edgesList = website.edgeIterator();
                    while (edgesList.hasNext()){
                        Integer link = edgesList.next();
                        results.add(new Tuple2<>(link, rank / outCount));
                    }
                    return results;
                });

        // Calculate new ranks by summing up contributions and applying damping factor
        JavaPairRDD<Integer, Double> newRanks = contributions.reduceByKey(
                (v1,  v2) -> v1 + v2
        ).mapValues(sum -> 0.15 + (0.85 * sum));

        return newRanks;
    }
}
