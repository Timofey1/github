import java.util.ArrayList;
import java.util.Date;

public class AllNews {
    /**
     * get list of sourses of user
     * @param userId user number
     * @return user's sourses
     * @author andtun
     */
    public static String[] getSbs(Integer userId) {}

    /**
     * swap two objects
     * @param list list
     * @param i index number one
     * @param j index number two
     */
    public static void swap(ArrayList<Post> list, Integer i, Integer j) {
        Post k = list.get(i);
        list.set(i, list.get(j));
        list.set(j, k);
    }

    /**
     * sort, that sorts first two posts by date
     * @param postObjs array of Post objects
     */
    public static void sortDate(ArrayList<Post> postObjs){
        for (int i = 0; i < 10; i++) {
            for (int j = postObjs.size() - 1; j > i; j--){
                if (postObjs.get(j).date.after(postObjs.get(j - 1).date)) {
                    swap(postObjs, j, j - 1);
                }
            }
        }
    }

    /**
     * sort, that sorts first two posts by date
     * @param postObjs array of Post objects
     */
    public static void sortRate(ArrayList<Post> postObjs){
        for (int i = 0; i < 10; i++) {
            for (int j = postObjs.size() - 1; j > i; j--){
                if ((postObjs.get(j).likes + postObjs.get(j).reposts) >
                        (postObjs.get(j - 1).likes + postObjs.get(j-1).reposts)) {
                    swap(postObjs, j, j - 1);
                }
            }
        }
    }

    /**
     * выдает 10 последних новостей
     * @param userId номер пользователя
     * @return ретурн
     */
    public static Post[] getLastNews(Integer userId) {
        String[] subs = getSbs(userId);
        ArrayList<Post> postObjs = new ArrayList<Post>();
        for (String sub: subs) {
            postObjs.add(PARSER);
        }
        sortDate(postObjs);
        Post[] result = new Post[10];
        for (int j = 0; j < 10; j++) {
            result[j] = postObjs.get(j);
        }
        return result;
    }

    /**
     * выдает 10 лучших новостей
     * @param userId номер пользователя
     * @return ретурн
     */
    public static Post[] getBestNews(Integer userId) {
        String[] subs = getSbs(userId);
        ArrayList<Post> postObjs = new ArrayList<Post>();
        for (String sub: subs) {
            postObjs.add(PARSER);
        }
        sortRate(postObjs);
        Post[] result = new Post[10];
        for (int j = 0; j < 10; j++) {
            result[j] = postObjs.get(j);
        }
        return result;
    }

}

class Post {
    protected String sourse;
    protected String pid;
    protected Date date;
    protected String link;
    protected String description;
    protected String imageUrl;
    protected Integer likes;
    protected Integer reposts;

    Post(String sourse, String pid, Date date,String description, String link, String imageUrl, Integer likes, Integer reposts) {

        this.date = date;
        this.description = description;
        this.imageUrl = imageUrl;
        this.link = link;
        this.pid = pid;
        this.likes = likes;
        this.reposts = reposts;
        this.sourse = sourse;

    }
}
