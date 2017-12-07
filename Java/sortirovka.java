public class sortirovka {
    public static void main(String[] args) {
        int[] num = {1,2,4,3,7,2,1};
        System.out.println(num.length);
        printArray(strir(num));
    }

    public static void printArray(int[] list) {
        int i;
        for (i = 0; i < list.length - 1; i++) {
            System.out.print(list[i] + ", ");
        }
        System.out.println(list[i]);
    }

    public static void swap(int[] list, Integer i, Integer j) {
        Integer k = list[i];
        list[i] = list[j];
        list[j] = k;
    }

    public static int[] strir(int[] num){
        for (int i = 0; i < 10; i++) {
            for (int j = num.length - 1; j > i; j--){
                if (num[j] > num[j-1]) {
                    swap(num,j,j-1);
                }
            }
        }
        return num;
    }

}
