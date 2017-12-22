import org.jsoup.Jsoup;
import java.io.IOException;

public class test {
    public static void main(String[] args) throws IOException {
        String r = AllNews.getresp("q");
        System.out.println(r);
    }
}
